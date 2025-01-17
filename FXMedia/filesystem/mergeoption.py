"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from enum import auto, Enum


class MergeOption(Enum):

    """Enumeration describing a set of merge strategies for updating data
    where the target data already exists.

    :var RAISE: Raise an exception.
    :var IGNORE: Ignore (discard) new data.
    :var REPLACE: Overwrite the target with new data.
    :var APPEND: Append new data to the target (Duplicates OK).
    :var MERGE: Append new data to the target (No Duplicates).
    :var REMOVE: Remove target values where they exist in new data.
    """

    RAISE = auto()
    IGNORE = auto()
    REPLACE = auto()
    APPEND = auto()
    MERGE = auto()
    REMOVE = auto()
