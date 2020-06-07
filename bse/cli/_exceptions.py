# -*- coding: utf-8 -*-
import click
from bse import logger, model
from bse.transform import Jsonable
from functools import update_wrapper
from typing import Any, Callable, Dict, List


def jsonexception(f: Callable[..., Any]) -> Any:
    """
    Converts all uncaught exceptions to JSON
    """

    def _f(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.new(f.__name__).exception(e)
            click.echo(Jsonable.dump(model.Error(e)))
            raise e

    return update_wrapper(_f, f)
