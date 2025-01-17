"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from pathlib import Path
from unittest import TestCase
from images import PNGImage


class _PNGImage(TestCase):

    """Unit tests for PNGImage class.

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
        return full_path.joinpath('test_data', f'{name}.png')

    def test_png_black_dominant(self):
        """Test a known black image returns black as the dominant color."""
        full_path = self.get_image('Black')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(PNGImage.get_hex(color), '#000000')

    def test_png_black_dominant_group(self):
        """Test a known black image returns black as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Black')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(PNGImage.get_hex(color), '#000000')

    def test_png_white_dominant(self):
        """Test a known white image returns white as the dominant color."""
        full_path = self.get_image('White')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(PNGImage.get_hex(color), '#FFFFFF')

    def test_png_white_dominant_group(self):
        """Test a known white image returns white as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('White')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(PNGImage.get_hex(color), '#F8F8F8')

    def test_png_red_dominant(self):
        """Test a known red image returns red as the dominant color."""
        full_path = self.get_image('Red')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(PNGImage.get_hex(color), '#FF0000')

    def test_png_red_dominant_group(self):
        """Test a known red image returns red as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Red')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(PNGImage.get_hex(color), '#F80000')

    def test_png_green_dominant(self):
        """Test a known green image returns green as the dominant color."""
        full_path = self.get_image('Green')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(PNGImage.get_hex(color), '#00FF00')

    def test_png_green_dominant_group(self):
        """Test a known green image returns green as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Green')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(PNGImage.get_hex(color), '#00F800')

    def test_png_blue_dominant(self):
        """Test a known blue image returns blue as the dominant color."""
        full_path = self.get_image('Blue')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(PNGImage.get_hex(color), '#0000FF')

    def test_png_blue_dominant_group(self):
        """Test a known blue image returns blue as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Blue')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(PNGImage.get_hex(color), '#0000F8')

    def test_png_purple_dominant(self):
        """Test a known purple image returns purple as the dominant color."""
        full_path = self.get_image('Purple')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(PNGImage.get_hex(color), '#A349A4')

    def test_png_purple_dominant_group(self):
        """Test a known purple image returns purple as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Purple')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(PNGImage.get_hex(color), '#A048A0')

    def test_png_cross_dominant(self):
        """Test the cross image returns the largest color. This is the pale
        green.
        """
        full_path = self.get_image('Cross')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(PNGImage.get_hex(color), '#B5E61D')

    def test_png_cross_dominant_group(self):
        """Test the cross image returns the largest color lower bound for the
        group.
        """
        full_path = self.get_image('Cross')
        image = PNGImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(PNGImage.get_hex(color), '#B0E018')
