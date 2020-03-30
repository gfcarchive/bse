# -*- coding: utf-8 -*-

import abc
from typing import Any, Dict


class Scope(abc.ABC):
    @abc.abstractmethod
    def scope(self) -> Dict[str, Any]:
        """
        Extracts the subsect of the global context that is used for this scope
        """
        pass

    @abc.abstractmethod
    def validate(self) -> None:
        """
        Validates the scope
        """
        pass
