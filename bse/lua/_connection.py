# -*- coding: utf-8 -*-

import attr
import requests
from bse import logger
from typing import Any, Dict, Tuple, Union
from urllib import parse


class ResponseError(Exception):
    pass


@attr.s
class Connection(object):

    _log: logger.Logger = attr.ib()
    _baseurl: str = attr.ib(default=attr.Factory(str))
    _cookiestr: str = attr.ib(default=attr.Factory(str))
    _session: requests.Session = attr.ib(default=attr.Factory(requests.Session))
    useragent: str = attr.ib(default=requests.utils.default_user_agent())  # type: ignore
    language: str = attr.ib(default="en-US")

    @_log.default
    def _initlog(self) -> logger.Logger:
        return logger.new(self.__class__.__name__)

    def get(self, url: str) -> Tuple[str, str, str, str, Dict[str, str]]:
        return self.request("GET", url)

    def post(self,
             url: str,
             post_content: Union[str, Dict[str, Any]] = None,
             post_content_type: str = None) -> Tuple[str, str, str, str, Dict[str, str]]:
        return self.request("POST", url, post_content=post_content, post_content_type=post_content_type)

    def request(
        self,
        method: str,
        url: str,
        post_content: Union[str, Dict[str, Any]] = None,
        post_content_type: str = None,
        headers: Dict[str, str] = None,
    ) -> Tuple[str, str, str, str, Dict[str, str]]:
        self._log.debug(f"Request [{method}]: {url}")

        url = self._parse_url(url)

        self._check_http_method(method)

        headers = self._topydict(headers)
        if self._cookiestr:
            headers["Cookie"] = self._cookiestr
        headers.update({"Accept-Language": self.language, "User-Agent": self.useragent})

        post_content = self._parse_content(post_content)

        resp = self._request(method, url, post_content, headers)
        self._log.debug(f"Cookies: {self._session.cookies}")

        self._log.debug(f"Response status code: {resp.status_code}")
        self._check_response(resp, headers, url)

        # content-type: 'application/json; charset=utf8'
        mime_type = resp.headers["content-type"].split(";")[0]
        filename = resp.headers.get("Content-Dispositon", "")
        charset = (resp.encoding or resp.apparent_encoding or "").upper()

        # content, charset, mimeType, filename, headers
        return (resp.text, charset, mime_type, filename, self._topydict(resp.headers))

    def close(self) -> None:
        self._session.close()

    def getBaseURL(self) -> str:
        return self._baseurl

    def setCookie(self, cookiestr: str) -> None:
        self._cookiestr = cookiestr

    def getCookies(self) -> Dict[str, str]:
        return self._session.cookies.get_dict()  # type: ignore

    def _parse_url(self, url: str) -> str:
        if not self._baseurl:
            self._baseurl = url
            self._log.debug(f"Future BaseUrl: {url}")
        else:
            self._baseurl = parse.urljoin(self._baseurl, url)
            if self._baseurl != url:
                self._log.debug(f"URL merging: {url} -> {self._baseurl}")
            url = self._baseurl
        return url

    def _request(
        self,
        method: str,
        url: str,
        post_content: Dict[str, str],
        headers: Dict[str, str],
    ) -> requests.Response:
        req = getattr(self._session, method.lower())
        if post_content:
            resp = req(url, data=post_content)
        else:
            resp = req(url)
        return resp

    def _topydict(
        self, d: Union[Dict[str, Any], requests.structures.CaseInsensitiveDict, None]
    ) -> Dict[str, str]:
        """
        The headers object return by Lua is not a fully functional dictionary and some methods
        do ont exist. This method performs the conversion
        """
        if d:
            return {k: v for k, v in d.items()}
        return {}

    def _parse_content(
        self, post_content: Union[str, Dict[str, Any], None]
    ) -> Dict[str, str]:
        """
        if a string, post_content comes in the form: a=this%20is%20a%20test&abc=ddd
        """
        if not post_content:
            return {}
        if isinstance(post_content, str):
            post_content = parse.parse_qs(
                post_content, keep_blank_values=True, strict_parsing=False
            )
        return self._topydict(post_content)

    def _check_http_method(self, method: str) -> None:
        if method not in ("GET", "POST", "PUT", "DELETE"):
            raise ValueError(f"Unsupported HTTP method {method}")

    def _check_response(
        self, resp: requests.Response, headers: Dict[str, str], url: str
    ) -> None:
        if resp.status_code != 200:
            if headers.get("Accept", "") != "application/json":
                raise ResponseError(
                    f"Request to {url} failed with error {resp.status_code}"
                )
