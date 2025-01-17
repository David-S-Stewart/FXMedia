Filesystem
==========

+----------+------------+-------------------+--------------------------------+
| Revision | Date       | Author            | Change                         |
+==========+============+===================+================================+
| 1.0      | 2025-01-17 | David Stewart     | Initial Version                |
+----------+------------+-------------------+--------------------------------+

When setting up the base project, I pulled in a simplified version of a store
interface that has proved useful in the past. This re-use assumes that work
of this nature will be part of a larger system. Use of this interface has two
primary advantages:

1. By adhering to this interface, all sorts of file-based objects can be
   supported using a common base that will always behave the same.

2. The Image class is focused on the image-specific implementations and does
   not need to concern itself with generic file system elements.
