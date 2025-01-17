"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from pathlib import Path
from types import NoneType
from typing import Any, Optional, Union
from utility import check
from .mergeoption import MergeOption
from .option import Option


class Store:

    """The store abstract base class that provides common save and load
    support to derived classes.

    :var EXTENSION: Default extension for unknown document types.
    """

    EXTENSIONS: tuple[str] = ('.bin',)

    @classmethod
    def parse(cls, data: Union[str, bytes, bytearray],
              option: Optional[Option] = None) -> Any:
        """Load an object from the given string type data. Override this
        method to implement in derived classes.

        :param data: Data as a string or in bytes.
        :param option: Optional elements for formatting and saving.
        """
        assert isinstance(data, (str, bytes, bytearray)), check()
        assert isinstance(option, (Option, NoneType)), check()
        # ----------
        raise NotImplementedError(f'Parse is not supported [{cls.__name__}].')

    @classmethod
    def load(cls, full_path: Path, option: Optional[Option] = None) -> Any:
        """ Load an object from the given full_path. If the file does no exist
        then the following will occur based on the LoadOption. If the option
        includes the NULLABLE flag then None is returned, otherwise an
        exception is raised.

        :param full_path: File or path to load from.
        :param option: Optional elements for formatting and saving.
        """
        assert isinstance(full_path, Path), check()
        assert isinstance(option, (Option, NoneType)), check()
        # ----------
        if full_path.exists:
            return cls._load(full_path, option)
        elif option and option.nullable:
            return None
        else:
            raise Exception(f'File [{full_path}] does not exist.')

    @classmethod
    def save_as(cls, value: Any, full_path: Path,
                merge_option: MergeOption = MergeOption.RAISE,
                option: Optional[Option] = None):
        """Save the value in the full_path specified.

        :param value: The value to save.
        :param full_path: File or path to save to.
        :param merge_option: Option to take where full_path already exists.
        :param option: Optional elements for formatting and saving.
        """
        assert isinstance(full_path, Path), check()
        assert isinstance(merge_option, MergeOption), check()
        assert isinstance(option, (Option, NoneType)), check()
        # ----------
        if full_path.exists:
            if merge_option is MergeOption.IGNORE:
                # Ignore means leave the existing file.
                return
            elif merge_option is MergeOption.REPLACE:
                pass
            elif merge_option is MergeOption.APPEND:
                cls._append(value, full_path)
            elif merge_option is MergeOption.APPEND:
                cls._merge(value, full_path)
            else:
                raise Exception(f'File [{full_path}] already exists.')
        cls._save(value, full_path, option)
        # Update the full_path.
        if isinstance(value, Store):
            value.full_path = full_path

    def __init__(self, full_path: Optional[Path] = None,
                 option: Optional[Option] = None):
        """Create a new Store object.

        :param full_path: Path to file on local system to save to.
        :param option: Optional elements for formatting and saving.
        """
        assert isinstance(full_path, (Path, NoneType)), check()
        assert isinstance(option, (Option, NoneType)), check()
        # ----------
        self._full_path = full_path
        self._option = option

    def save(self, merge_option: MergeOption = MergeOption.RAISE):
        """Save the object as to file.

        :param merge_option: Option to take where full_path already exists.
        """
        assert isinstance(merge_option, MergeOption), check()
        # ----------
        if self._full_path is None:
            raise Exception(f'Cannot save [{self.__class__.__name__}].')
        else:
            self.save_as(self, self._full_path, merge_option, self._option)

    @property
    def full_path(self) -> Optional[Path]:
        """Path to file on local system to save to."""
        return self._full_path

    @full_path.setter
    def full_path(self, value: Optional[Path]):
        assert isinstance(value, (Path, NoneType)), check()
        # ----------
        self._full_path = value

    @property
    def option(self) -> Optional[Option]:
        """Optional elements for formatting and saving."""
        return self._option

    def __str__(self) -> str:
        # Example: 'Store'
        # Example: 'Store [C:\test.txt]'
        if self._full_path:
            return f'{self.__class__.__name__} [{self._full_path.name}]'
        else:
            return self.__class__.__name__

    def __eq__(self, other: Any) -> bool:
        # Check equality against another Store.
        if type(self) is type(other):
            if self._file == other._file:
                if self._option == other.option:
                    return True
        return False

    @classmethod
    def _save(cls, value: Any, full_path: Path, option: Optional[Option]):
        # Implement in inherited class to support this interface.
        raise NotImplementedError('Abstract Interface.')

    @classmethod
    def _append(cls, value: Any, full_path: Path):
        # Implement in inherited class to support this interface.
        text = f'Append is not supported for [{cls.__name__}].'
        raise NotImplementedError(text)

    @classmethod
    def _merge(cls, value: Any, full_path: Path):
        # Implement in inherited class to support this interface.
        text = f'Merge is not supported for [{cls.__name__}].'
        raise NotImplementedError(text)

    @classmethod
    def _load(cls, full_path: Path, option: Optional[Option]) -> Any:
        # Override in inherited class to modify support for this interface.
        with open(full_path, mode='rb') as file_:
            return cls.parse(file_.read(), option)
