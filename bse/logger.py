# -*- coding: utf-8 -*-

import logging
from bse import defaults
from bse.transform import Jsonable
from typing import Any, Dict, List


class BSELogger(logging.getLoggerClass()):  # type: ignore
    def _context(self, kwargs: Dict[str, Any]) -> None:
        kwargs["extra"] = kwargs.get("extra", {})
        kwargs["extra"]["context"] = kwargs["extra"].get("context", "")

    def _tryjsonify(self, msg: Any) -> Any:
        if isinstance(msg, dict):
            # make a copy to mask values
            msg = dict(msg)
            for k in defaults.MASK_KEYS:
                v = msg.get(k)
                if v and isinstance(v, str):
                    msg[k] = "*" * len(v)
            try:
                msg = Jsonable.dump(msg)
            except Exception:
                pass
        elif isinstance(msg, list) or isinstance(msg, Jsonable):
            try:
                msg = Jsonable.dump(msg)
            except Exception:
                pass
        return msg

    def info(self, msg: Any, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        self._context(kwargs)
        msg = self._tryjsonify(msg)
        super().info(msg, *args, **kwargs)

    def warning(self, msg: Any, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        self._context(kwargs)
        msg = self._tryjsonify(msg)
        super().warning(msg, *args, **kwargs)

    def error(self, msg: Any, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        self._context(kwargs)
        msg = self._tryjsonify(msg)
        super().error(msg, *args, **kwargs)

    def critical(self, msg: Any, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        self._context(kwargs)
        msg = self._tryjsonify(msg)
        super().critical(msg, *args, **kwargs)

    def exception(self, msg: Any, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        self._context(kwargs)
        msg = self._tryjsonify(msg)
        super().exception(msg, *args, **kwargs)

    def debug(self, msg: Any, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        self._context(kwargs)
        msg = self._tryjsonify(msg)
        super().debug(msg, *args, **kwargs)


logging.setLoggerClass(BSELogger)

Logger = logging.Logger


def new(name: str) -> Logger:
    # Create a custom logger
    logger = logging.getLogger(name)

    log_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s%(context)s - %(message)s"
    )
    log_level = logging.DEBUG
    logger.setLevel(log_level)
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            handler.setLevel(log_level)
            handler.setFormatter(log_format)
            break
    else:
        c_handler = logging.FileHandler(filename=defaults.LOG)
        c_handler.setLevel(log_level)
        c_handler.setFormatter(log_format)
        logger.addHandler(c_handler)
    return logger
