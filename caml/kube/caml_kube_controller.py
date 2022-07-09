from kubernetes import client, config

from


class CamlKubeController:
    def __init__(self, kube_config=None):
        # Init the kube config
        if kube_config:
            config.load_kube_config(config_file=kube_config)
        else:
            # To use the CLI/SDK inside of the cluster
            config.load_incluster_config()

        self._init_tasks()

    def _init_tasks(self):
