"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from pathlib import Path
from types import NoneType
from typing import Any, Optional
from matplotlib.pyplot import imread
from numpy import ndarray, uint8, float32
from filesystem import Option, Store
from utility import check


class Image(Store):

    """Abstract image class wrapper for bitmap images.

    :var RGB: RGB type constant.
    """

    RGB = tuple[uint8, uint8, uint8]

    @classmethod
    def get_hex(cls, color: RGB) -> str:
        """Return a standard RGB hex string for the color.

        :param color: The color.
        """
        return f'#{color[0]:02X}{color[1]:02X}{color[2]:02X}'

    def __init__(self, full_path: Optional[Path] = None,
                 option: Optional[Option] = None):
        """Create a new Image_ object.

        :param full_path: Path to file on local system to save to.
        :param option: Optional elements for formatting and saving.
        """
        super().__init__(full_path, option)
        self._data = None

    def get_count(self, group: int = 1) -> int:
        """Get a count of the colors in the image.

        :param group: Color group size.
        """
        counts = self.get_color_counts(group)
        return len(counts)

    def get_dominant_color(self, group: int = 1) -> RGB:
        """Get the dominant color of the image.

        :param group: Color group size.
        """
        counts = self.get_color_counts(group)
        return max(counts.keys(), key=counts.get)

    def get_dominant_colors(self, count: int = 1,
                            group: int = 1) -> list[RGB]:
        """Get a list of the most used colors in the image. If there are
        fewer colors than the count, all colors will be returned.

        :param count: Number of colors to return.
        :param group: Color group size.
        """
        counts = self.get_colur_counts(group)
        return sorted(counts, key=counts.get, reverse=True)[:count]

    def get_color_counts(self, group: int = 1) -> dict[RGB, int]:
        """Generate a dictionary of the counts of each color in RGB for the
        image. If group is greater than one, group each channel (RGB) in
        blocks of that count (0-n, n+1-2n...) for the entire range.

        Note that if the group is not a power of 2, the top group (the white)
        end will be smaller than the rest. A group size of 8 is recommended.
        """

        def get_map() -> 'function':
            # Select the map based on the data.
            data = self._data[0, 0]
            if len(data) == 3:
                if type(data[0]) is uint8:
                    return map_rgb
            elif len(data) == 4:
                if type(data[0]) is uint8:
                    return map_rgba
                elif type(data[0]) is float32:
                    return map_deca
            raise Exception()

        def map_rgb(rgb) -> Image.RGB:
            # Integer 8bit RGB
            return tuple(rgb)

        def map_rgba(rgb) -> Image.RGB:
            # Integer RGB with alpha channel.
            return tuple(rgb[:3])

        def map_deca(rgb) -> Image.RGB:
            # Decimal RGB with alpha channel.
            return (uint8(rgb[0] * 255),
                    uint8(rgb[1] * 255),
                    uint8(rgb[2] * 255))

        map_ = get_map()
        counts = {}
        for row in self._data:
            for rgb in row:
                color = map_(rgb)
                if group > 1:
                    color = tuple(c // group * group for c in color)
                counts[color] = counts.setdefault(color, 0) + 1
        return counts

    @property
    def data(self) -> Optional[ndarray]:
        """Image data in NumPy format."""
        return self._data

    @data.setter
    def data(self, value: Optional[ndarray]):
        assert isinstance(value, (ndarray, NoneType)), check()
        # ----------
        self._data = value

    @property
    def width(self) -> int:
        """The width of the image in pixels."""
        return self._data.shape[1]

    @property
    def height(self) -> int:
        """The height of the image in pixels."""
        return self._data.shape[0]

    @classmethod
    def _load(cls, full_path: Path, option: Optional[Option]) -> Any:
        # Load an image from the file.
        image = cls(full_path)
        image.data = imread(full_path)
        return image
