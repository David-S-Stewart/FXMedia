"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from .image import Image


class TIFFImage(Image):

    """Image wrapper for tiff files."""

    EXTENSIONS: tuple[str] = ('.tif', '.tiff')
