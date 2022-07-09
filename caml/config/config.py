import os

from kubernetes import config

CONFIG_FOLDER = os.path.join(os.path.expanduser("~"), ".caml")
CONFIG_FILE_NAME = os.path.join(CONFIG_FOLDER, "config.json")
CONFIG_KUBE_FILE_NAME = os.path.join(CONFIG_FOLDER, "caml-kube-config")


class CamlConfig:
    def __init__(self, kube_config=None):
        # Init the kube config globally
        CamlConfig.load_kube_config(kube_config)

    @staticmethod
    def load_kube_config(kube_config=None):
        """
        Inits the kube config from either the given config, local setup or kubernetes cloud
        :return: None
        """
        if kube_config:
            config.load_kube_config(config_file=kube_config)
        elif os.path.exists(CONFIG_KUBE_FILE_NAME):
            config.load_kube_config(config_file=CONFIG_KUBE_FILE_NAME)
        else:
            # To use the CLI/SDK inside of the cluster
            config.load_incluster_config()
