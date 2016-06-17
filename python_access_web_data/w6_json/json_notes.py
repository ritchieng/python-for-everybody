# Import json
import json

# Create Data: Dictionary
# If dictionary, data parsed will be dictionary
data = '''{
    "name" : "John",
    "phone" : {
        "type" : "international",
        "mobile" : "999"
    },
    "email" : {
        "hide" :  "yes"
    }
}'''

# Deserialization from string to internal structure (where you get back a dictionary)
info = json.loads(data)

# Access native dictionary
print 'Name:', info["name"]
print 'Hide:', info["email"]["hide"]


# Create data list
# If list, data parsed will be list
input2 = '''[
    {
    "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {
    "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''

info2 = json.loads(input2)
print 'User count:', len(info2)
for item in info2:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']