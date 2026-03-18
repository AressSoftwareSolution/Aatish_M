import yaml

data = {
    'Name': 'Nikhil',
    'age': 20,
    'handles': {
        'facebook': 'nikhilkingh97',
        'github': 'nikhilkumarsingh',
        'youtube': 'IndianPythonista'
    },
    'languages': {
        'markup': [' HTML', 'XML', 'AIMLI'],
        'programming': ['C', 'C++', 'Python', 'javascript']
    }
}


with open("yaml_example.yaml","w") as file:
    yaml.dump(data,file, default_flow_style=False)