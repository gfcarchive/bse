# -*- coding: utf-8 -*-

import logging

Logger = logging.Logger


def new(name: str) -> Logger:
    # Create a custom logger
    logger = logging.getLogger(name)

    log_format = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
    log_level = logging.DEBUG
    logger.setLevel(log_level)
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            handler.setLevel(log_level)
            handler.setFormatter(log_format)
            break
    else:
        c_handler = logging.StreamHandler()
        c_handler.setLevel(log_level)
        c_handler.setFormatter(log_format)
        logger.addHandler(c_handler)
    return logger
