from kubernetes import client, config
from kubernetes.client.exceptions import ApiException

from caml.kube.tasks.base_task import BaseKubeTask


class KubeTaskCamlDeployer(BaseKubeTask):
    def __init__(self, config=None):
        super().__init__(config)


        self.apps_api = client.AppsV1Api()
        self.core_api = client.CoreV1Api()
        self.batch_api = client.BatchV1Api()
        self.autoscale_api = client.AutoscalingV2beta2Api()

    def run(self, prefix, library_name, library_version):
        """
        Returns a unique and valid kubernetes resource name
        @param prefix: [String] The configuration prefix
        @param library_name: [String] The library name
        @param library_version: [String] The library version (0.0.0)
        @return: [String] job name
        """
        try:
            resource = self._config_name("job", library_name, library_version)
            self.batch_api.delete_namespaced_job(name=resource, namespace="builder", propagation_policy="Background")
            self.core_api.delete_namespaced_config_map(namespace="builder", name=resource)
        except Exception as e:
            if e.status != 404:
                raise e

    def wait(self, prefix, library_name, library_version):
        print("hello")