import json
data = {
    'name' : 'John',
    'age' : 30,
    'city' : 'New York'
}

json_data = json.dumps(data)
print(json_data)
new_data = json.loads(json_data)
print(new_data)

with open('data.json', 'w') as f:
    json.dump(data, f)
with open('data.json', 'r') as f:
    file_data = json.load(f)
print(file_data)