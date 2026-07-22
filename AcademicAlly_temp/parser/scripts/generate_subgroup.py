import json

def generate_subgroup():
    with open('../results.json', 'r') as f:
        data = json.load(f)
    
    subgroups = {k: k for k in data.keys()}
    
    with open('../subgroup.json', 'w') as f:
        json.dump(subgroups, f, indent=4)

if __name__ == "__main__":
    generate_subgroup()
