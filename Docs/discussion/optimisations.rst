Optimisations
=============

+----------+------------+-------------------+--------------------------------+
| Revision | Date       | Author            | Change                         |
+==========+============+===================+================================+
| 1.0      | 2025-01-17 | David Stewart     | Initial Version                |
+----------+------------+-------------------+--------------------------------+

There are a number of inefficiencies in this design.

Memory Usage
------------

This solution reads the entire image into memory, this can be significant as
seen in some of the examples. An alternative to this would be to read the file
sequentially collating the required data and discarding the rest. This would
give a minimal memory footprint and may very well be faster. A compiled
language would be a better choice.

The effort for this would be significant as each different format would need
an individual solution. This would also remove external dependencies.

Expensive Calls
---------------

Several methods are based on the same expensive call to gather the base data
set. This repetition could be mitigated by storing result internally.

Iterative Processing
--------------------

This solution relies on a pixel by pixel iteration. There maybe matrix
transformations that are significantly more efficient.
