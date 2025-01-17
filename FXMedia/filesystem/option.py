"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from typing import Any
from utility import check


class Option:

    """The Option class provides additional information for the loading and
    saving of files.
    """

    def __init__(self, nullable: bool = False):
        """"Create a new Option object.

        :param nullable: True if None may be returned, False otherwise.
        """
        assert isinstance(nullable, bool), check()
        # ----------
        self._nullable = nullable

    @property
    def nullable(self) -> bool:
        """True if None may be returned, False otherwise."""
        return self._nullable

    def __str__(self) -> str:
        # Example: 'Option'
        return self.__class__.__name__

    def __eq__(self, other: Any) -> bool:
        # Check equality against another Option.
        if type(self) is type(other):
            if self._nullable == other.nullable:
                return True
        return False
