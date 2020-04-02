# -*- coding: utf-8 -*-

import attr
import requests
from bse import logger
from typing import Dict, Tuple


@attr.s
class Connection(object):

    _log: logger.Logger = attr.ib()

    @_log.default
    def _initlog(self) -> logger.Logger:
        return logger.new(Connection.__class__.__name__)

    def request(
        self,
        method: str,
        url: str,
        post_content: str = None,
        post_content_type: str = None,
        headers: Dict[str, str] = None,
    ) -> Tuple[str, str, str, str, Dict[str, str]]:
        self._log.debug(f"Request [{method}]: {url}")
        self._check_http_method(method)
        req = getattr(requests, method.lower())
        resp = req(url)

        # content-type: 'application/json; charset=utf8'
        mime_type = resp.headers["content-type"].split(";")[0]
        filename = resp.headers.get("Content-Dispositon", "")
        charset = (resp.encoding or resp.apparent_encoding or "").upper()

        # content, charset, mimeType, filename, headers
        return (resp.text, charset, mime_type, filename, resp.headers)

    def _check_http_method(self, method: str) -> None:
        if method not in ("GET", "POST", "PUT", "DELETE"):
            raise ValueError(f"Unsupported HTTP method {method}")
