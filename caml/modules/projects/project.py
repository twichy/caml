from kubernetes import client
from kubernetes.client.exceptions import ApiException

from caml.kube.consts import CAML_EXTENSION_GROUP, CAML_COMPUTE_NAMESPACE
from caml.modules.workspaces import WorkspacesClient


class Project:

    # TODO: decide on dynamic attributes and lazy loading
    attributes = {
        "name": str,
    }

    def __init__(self, name=None):
        self.resource_args = {
            "name": name,
            "group": CAML_EXTENSION_GROUP,
            "plural": "projects",
            "version": "v1",
            "namespace": CAML_COMPUTE_NAMESPACE
        }

        self.project_client = client.CustomObjectsApi()
        self._init_clients()

    def _get_object_data(self):
        return self.project_client.get_namespaced_custom_object(**self.resource_args)

    def save(self):
        pass

    def delete(self):
        """
        Deletes the current project
        @return: None
        """
        try:
            self.project_client.delete_namespaced_custom_object(**self.resource_args)
        except ApiException as e:
            if e.status == 404:
                print("not found!")

    def _init_clients(self):
        """
        Sets up the clients that are exposed to the user.
        @return: None
        """

        self.workspaces = WorkspacesClient()
