# Sinks

## Simple stream

```python
add_six = lambda x: x + 6

(
    Source(2)
      >> add_six
      >> print
  )()
```

# Http stream

```python
r = (
  Source.from_json_url('https://jsonplaceholder.typicode.com/albums')
    >> extract_partials('id', 'title', 'userId')
    >> group_by('userId')
    >> pprint.pprint
)()
```

## Generator stream

```python
add_six = lambda x: x + 6
divide = lambda x: x / 2

source = (
    GeneratorSource([1,2,3,4])
        >> add_six
        >> divide
)

for item in source:
    print(item)
```
