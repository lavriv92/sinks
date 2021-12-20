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

.. code-block:: python

  import pprint
  from sinks import Source
  from sinks.operators import extract_partials, group_by

  r = (
    Source.from_json_url('https://jsonplaceholder.typicode.com/albums')
      >> extract_partials('id', 'title', 'userId')
      >> group_by('userId')
      >> pprint.pprint
  )()

Stream generator:

.. code-block:: python

  from sinks import GeneratorSource

  add_six = lambda x: x + 6
  divide = lambda x: x / 2

  source = (
    GeneratorSource([1,2,3,4])
        >> add_six
        >> divide
  )

  for item in source:
      print(item)

