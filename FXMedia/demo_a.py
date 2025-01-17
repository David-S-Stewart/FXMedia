"""
:Author:        David Stewart
:Date:          2025-01-14
:Compatibility: Python 3.10

Demo a. Loop through swatches examples and print out all data.
"""

if __name__ == '__main__':

    from pathlib import Path
    from images import Image

    test_data = Path(__file__).parent.joinpath('unit', 'test_data')

    group = 16
    top = 9

    for name in ('Black', 'White', 'Red', 'Blue', 'Green', 'Purple', 'Cross'):
        print('=============================')
        for extension in ('.png', '.jpg', '.bmp', '.tif', '.gif'):
            full_path = test_data.joinpath(f'{name}{extension}')
            image = Image.load(full_path)
            count = image.get_count(group)
            dominant = Image.get_hex(image.get_dominant_color())
            grouped = Image.get_hex(image.get_dominant_color(group))
            print(image)
            print(f'- Size:     {image.width} × {image.height} pixels'
                  f'({image.width * image.height})')
            print(f'- Colors:   {image.get_count()} ({count} grouped)')
            print(f'- Dominant: {dominant} ({grouped} grouped)')
            print(f'- Top {top} colors:')
            for count in image.get_dominant_colors(top):
                print(f'    {Image.get_hex(count)}')
            print(f'- Top {top} grouped colors:')
            for count in image.get_dominant_colors(top, group):
                print(f'    {Image.get_hex(count)}')
