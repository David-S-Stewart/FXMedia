"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from pathlib import Path
from unittest import TestCase
from images import GIFImage


class _GIFImage(TestCase):

    """Unit tests for GIFImage class.

    Tests include:
    - swatches for black and white.
    - swatches for primary colors.
    - a mixed color.

    This set of tests should be extended to test the capabilities of the
    format.
    """

    def get_image(self, name: str) -> Path:
        """Get the name of the required image file.

        :param name: The name without path or extension.
        """
        full_path = Path(__file__).parent.parent
        return full_path.joinpath('test_data', f'{name}.gif')

    def test_gif_black_dominant(self):
        """Test a known black image returns black as the dominant color."""
        full_path = self.get_image('Black')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(GIFImage.get_hex(color), '#000000')

    def test_gif_black_dominant_group(self):
        """Test a known black image returns black as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Black')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(GIFImage.get_hex(color), '#000000')

    def test_gif_white_dominant(self):
        """Test a known white image returns white as the dominant color."""
        full_path = self.get_image('White')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(GIFImage.get_hex(color), '#FFFFFF')

    def test_gif_white_dominant_group(self):
        """Test a known white image returns white as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('White')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(GIFImage.get_hex(color), '#F8F8F8')

    def test_gif_red_dominant(self):
        """Test a known red image returns red as the dominant color."""
        full_path = self.get_image('Red')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(GIFImage.get_hex(color), '#FF0000')

    def test_gif_red_dominant_group(self):
        """Test a known red image returns red as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Red')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(GIFImage.get_hex(color), '#F80000')

    def test_gif_green_dominant(self):
        """Test a known green image returns green as the dominant color."""
        full_path = self.get_image('Green')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(GIFImage.get_hex(color), '#00FF00')

    def test_gif_green_dominant_group(self):
        """Test a known green image returns green as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Green')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(GIFImage.get_hex(color), '#00F800')

    def test_gif_blue_dominant(self):
        """Test a known blue image returns blue as the dominant color."""
        full_path = self.get_image('Blue')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(GIFImage.get_hex(color), '#0000FF')

    def test_gif_blue_dominant_group(self):
        """Test a known blue image returns blue as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Blue')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(GIFImage.get_hex(color), '#0000F8')

    def test_gif_purple_dominant(self):
        """Test a known purple image returns purple as the dominant color.
        Note that for GIFs this color is dithered and the actual color
        returned is a long way from expected.
        """
        full_path = self.get_image('Purple')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(GIFImage.get_hex(color), '#995599')

    def test_gif_purple_dominant_group(self):
        """Test a known purple image returns purple as the lower bound for the
        group of the dominant color.
        Note that for GIFs this color is dithered and the actual color
        returned is a long way from expected.
        """
        full_path = self.get_image('Purple')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(GIFImage.get_hex(color), '#985098')

    def test_gif_cross_dominant(self):
        """Test the cross image returns the largest color. This is the pale
        green.
        Note that for GIFs this color is dithered and the actual color
        returned is a long way from expected.
        """
        full_path = self.get_image('Cross')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(GIFImage.get_hex(color), '#6680CC')

    def test_gif_cross_dominant_group(self):
        """Test the cross image returns the largest color lower bound for the
        group.
        Note that for GIFs this color is dithered and the actual color
        returned is a long way from expected.
        """
        full_path = self.get_image('Cross')
        image = GIFImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(GIFImage.get_hex(color), '#6080C8')
