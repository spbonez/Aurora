import pkgutil
import inspect
import json


__all__ = []

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        if inspect.isfunction(value):
            globals()[name] = value
            __all__.append(name)

with open('../config/config.json', 'r') as json_file:
    data = json.load(json_file)
json_file.close()

data['Commands'] = {'User_Cmd': [], 'Admin_Cmd': []}
for cmd in __all__:
    if cmd.startswith('_'):
        data['Commands']['Admin_Cmd'].append('!'+cmd)
    else:
        data['Commands']['User_Cmd'].append('!'+cmd)

with open('../config/config.json', 'w') as json_file:
    json.dump(data, json_file, indent=2, sort_keys=True)
json_file.close()
