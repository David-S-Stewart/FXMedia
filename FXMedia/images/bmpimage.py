"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from .image import Image


class BMPImage(Image):

    """Image wrapper for bitmap files."""

    EXTENSIONS: tuple[str] = ('.bmp', '.dib')
