Task
====

+----------+------------+-------------------+--------------------------------+
| Revision | Date       | Author            | Change                         |
+==========+============+===================+================================+
| 1.0      | 2025-01-17 | David Stewart     | Initial Version                |
+----------+------------+-------------------+--------------------------------+

For this challenge you should:
- Use the programming language you are most comfortable with.
- Upload your code to a public GitHub.
- Include documentation in a readme file.
- Coding Challenge: "Image Dominant Color Finder"

Challenge one
-------------

Write a program to find the dominant colour of an image. The dominant colour
is the one that appears most frequently in the image.

During your technical interview you will be asked to show your code working
and talk us through your approach.

Requirements
------------

Use the language you are most familiar with.

Ensure that your code is well documented.

Input: Your program should accept an image file as input. This can be in any
common format such as JPG, PNG, etc.

Processing
----------

Load the image and read its pixels.
Compare the colours of the pixels to determine which colour appears the most
frequently.
You can simplify the problem by reducing the colour space. For example, you
can round the RGB values of each pixel to the nearest multiple of 10 to avoid
very minor colour differences impacting the results.
Output: The program should output the RGB values of the most frequent
(dominant) colour in the image.

Challenge two
-------------

Pick any one of the following features to add on to your project:

- Implement efficiency optimisations such as using a dictionary or hash map to
  count occurrences of each colour.
- Add functionality to ignore certain colours (like white or black) if desired.
- Provide an option to return the top N dominant colours instead of just one.
