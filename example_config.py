import yaml

def load_config():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)

    return config
