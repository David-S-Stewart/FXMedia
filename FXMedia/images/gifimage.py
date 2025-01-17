"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from .image import Image


class GIFImage(Image):

    """Image wrapper for gif files."""

    EXTENSIONS: tuple[str] = ('.gif')
