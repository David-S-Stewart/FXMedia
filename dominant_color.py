"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10

Image Dominant Color Finder
===========================

usage: python dominant_color.py <<full_path>> [<<group>>]

Where full_path is the path to an image file and group is the size
for grouping colors.
"""

from pathlib import Path
from sys import argv
from images import Image

if __name__ == '__main__':
    # Get the group. Default to 1.
    try:
        group = int(argv[2])
    except Exception:
        group = 1
    # Get and print the dominant color.
    try:
        full_path = Path(argv[1])
        image = Image.load(full_path)
        print(Image.get_hex(image.get_dominant_color(group)))
    except Exception as e:
        print('The operation failed.')
        print(e)
