
import yaml

tree = {}


def read(config_file):
    global tree
    with open(config_file) as f:
        tree = yaml.safe_load(f.read())
