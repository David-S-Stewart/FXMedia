Observations
============

+----------+------------+-------------------+--------------------------------+
| Revision | Date       | Author            | Change                         |
+==========+============+===================+================================+
| 1.0      | 2025-01-17 | David Stewart     | Initial Version                |
+----------+------------+-------------------+--------------------------------+

While I am confident that his solution is working as specified, the results
are surprising in some cases. There is a general lack of precision between
formats (with the exception of png) and the color counts vary radically
between what was in theory the same simple image.

For real world images, what we perceive as the dominant color may very not be.
"Red Car.jpg" is an example of this - the image is mostly grey.

I have assumed that image transformation would need some format-specifics.
This proved to be not the case. So while I generated separate classes for each
format, they are not really required. For any edit or save functionality, they
most certainly would be.
