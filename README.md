# Sinks

## Simple stream

```python
add_six = lambda x: x + 6

(
    Source(2)
      >> add_six
      >> print
  )()

  r = (
    Source.from_json_url('https://jsonplaceholder.typicode.com/albums')
      >> extract_partials('id', 'title', 'userId')
      >> group_by('userId')
      >> pprint.pprint
    )()
```

## Generator stream
