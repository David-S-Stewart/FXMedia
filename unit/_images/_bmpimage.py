"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10
"""

from pathlib import Path
from unittest import TestCase
from images import BMPImage


class _BMPImage(TestCase):

    """Unit tests for BMPImage class.

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
        return full_path.joinpath('test_data', f'{name}.bmp')

    def test_bmp_black_dominant(self):
        """Test a known black image returns black as the dominant color."""
        full_path = self.get_image('Black')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(BMPImage.get_hex(color), '#000000')

    def test_bmp_black_dominant_group(self):
        """Test a known black image returns black as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Black')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(BMPImage.get_hex(color), '#000000')

    def test_bmp_white_dominant(self):
        """Test a known white image returns white as the dominant color."""
        full_path = self.get_image('White')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(BMPImage.get_hex(color), '#FFFFFF')

    def test_bmp_white_dominant_group(self):
        """Test a known white image returns white as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('White')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(BMPImage.get_hex(color), '#F8F8F8')

    def test_bmp_red_dominant(self):
        """Test a known red image returns red as the dominant color."""
        full_path = self.get_image('Red')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color()
        # Note that the expected color is out by 1. This may be due to the
        # image editor (MS paint).
        self.assertEqual(BMPImage.get_hex(color), '#FE0000')

    def test_bmp_red_dominant_group(self):
        """Test a known red image returns red as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Red')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(BMPImage.get_hex(color), '#F80000')

    def test_bmp_green_dominant(self):
        """Test a known green image returns green as the dominant color."""
        full_path = self.get_image('Green')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color()
        # Note that the expected color is out by 1. This may be due to the
        # image editor (MS paint).
        self.assertEqual(BMPImage.get_hex(color), '#00FF01')

    def test_bmp_green_dominant_group(self):
        """Test a known green image returns green as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Green')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(BMPImage.get_hex(color), '#00F800')

    def test_bmp_blue_dominant(self):
        """Test a known blue image returns blue as the dominant color."""
        full_path = self.get_image('Blue')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color()
        self.assertEqual(BMPImage.get_hex(color), '#0000FE')

    def test_bmp_blue_dominant_group(self):
        """Test a known blue image returns blue as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Blue')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(BMPImage.get_hex(color), '#0000F8')

    def test_bmp_purple_dominant(self):
        """Test a known purple image returns purple as the dominant color."""
        full_path = self.get_image('Purple')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color()
        # Note that the expected color is out by 1. This may be due to the
        # image editor (MS paint).
        self.assertEqual(BMPImage.get_hex(color), '#A349A3')

    def test_bmp_purple_dominant_group(self):
        """Test a known purple image returns purple as the lower bound for the
        group of the dominant color.
        """
        full_path = self.get_image('Purple')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(BMPImage.get_hex(color), '#A048A0')

    def test_bmp_cross_dominant(self):
        """Test the cross image returns the largest color. This is the pale
        green.
        """
        full_path = self.get_image('Cross')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color()
        # Note that the expected color is out by 1. This may be due to the
        # image editor (MS paint).
        self.assertEqual(BMPImage.get_hex(color), '#B5E51D')

    def test_bmp_cross_dominant_group(self):
        """Test the cross image returns the largest color lower bound for the
        group.
        """
        full_path = self.get_image('Cross')
        image = BMPImage.load(full_path)
        color = image.get_dominant_color(8)
        self.assertEqual(BMPImage.get_hex(color), '#B0E018')
