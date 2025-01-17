Dependencies
============

+----------+------------+-------------------+--------------------------------+
| Revision | Date       | Author            | Change                         |
+==========+============+===================+================================+
| 1.0      | 2025-01-17 | David Stewart     | Initial Version                |
+----------+------------+-------------------+--------------------------------+

There are two dependencies in this project:
- the NumPy package
- the matplotlib package

Dependencies should be kept to a minumum. While these dependencies aid and
speed development, they also add a maintenance overhead. It is important to
bear in mind that a lot of code stays around a long time, and is only
typically changed when there is a genuine need.

Note that even with these two well known packages, there has been considerable
interface churn, and that is likely to continue.

Generally, a third party dependency should only be added if there is a
compelling case for it.

The usual exception to this is throwaway code.
