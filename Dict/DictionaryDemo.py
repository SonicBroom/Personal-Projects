__author__ = 'ambli'

dict = {
  'foo': 1,
  'bar': [1, 2, 3],
  'baz': 'Hello'
}

# Use key to access value
print ("dict['foo']:", dict['foo'])
print ("====================")

# Iterate values
for key in dict:
    print ("dict['%s']: %s" % (key, dict[key]))
print ("====================")

for (key, value) in dict.items():
    print ("dict['%s']: %s" % (key, value))
print ("====================")

# Update values
print ("Origin dict['foo']:", dict['foo'])
dict['foo'] = 123
print ("Updated dict['foo']:", dict['foo'])
print ("====================")

# Delete value
print ("Origin dict: ", dict)
del dict['foo']
print ("Deleted dict: ", dict)