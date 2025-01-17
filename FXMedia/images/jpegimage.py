"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from .image import Image


class JPEGImage(Image):

    """Image wrapper for jpeg files."""

    EXTENSIONS: tuple[str] = ('.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp')
