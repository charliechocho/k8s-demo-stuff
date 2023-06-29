# this file can only contain Starlark code, not YAML content
# this restriction is based on the file extension

def func1(get_key):
  list = [1, 2, 3]
  return list[get_key]
end
