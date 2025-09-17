import yaml
from ase.io import read

def load_config(yaml_file):
    with open(yaml_file, "r") as f:
        return yaml.safe_load(f)

def load_geometry(xyz_file):
    return read(xyz_file)
