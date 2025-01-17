Coding Standards
================

+----------+------------+-------------------+--------------------------------+
| Revision | Date       | Author            | Change                         |
+==========+============+===================+================================+
| 1.0      | 2025-01-17 | David Stewart     | Initial Version                |
+----------+------------+-------------------+--------------------------------+

All coding to follow PEP8_ at 80 characters, checked with pycodestyle.

Additionally, unless there is a compelling reason otherwise:
- All text-based files encoded in utf-8
- All text-based files to use Linux line ends (\n)
- All text-based files should have extraneous white space stripped
- Full type hints as supported from version 3.9 should be maintained
- Naming should follow American English

All code to be compatible with python Stable_Releases_.

Coding style should employ Design_by_Contract_ style with asserts on public
method parameters. 

Imports from internal modules should be relative and wherever possible follow
the form:

from ... import ...

.. _PEP8: https://peps.python.org/pep-0008/
.. _Stable_Releases: https://devguide.python.org/versions/
.. _Design_by_Contract: https://en.wikipedia.org/wiki/Design_by_contract
