import yaml
import os


class YamlHelper(object):
    @staticmethod
    def local_path(relative_path):
        return os.path.join(os.path.dirname(__file__), relative_path)

    @staticmethod
    def load_file(config_path):
        return yaml.safe_load(open(YamlHelper.local_path(config_path),mode='r', encoding='utf-8'))