"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from .image import Image


class PNGImage(Image):

    """Image wrapper for png files."""

    EXTENSIONS: tuple[str] = ('.png')
