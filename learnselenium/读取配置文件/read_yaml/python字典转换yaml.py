import yaml
dict={'name': 'Jack', 'age': 23, 'children': {'name': 'Jason', 'age': 2, 'name_1': 'Jeff', 'age_1': 4}}
print(yaml.dump(dict))