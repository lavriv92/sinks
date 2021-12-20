Quickstart
==========

Simple stream:

.. code-block:: python

   from sinks import Source

   add_six = lambda x: x + 6

   (
     Source(2)
       >> add_six
       >> print
   )()

Stream from http:

