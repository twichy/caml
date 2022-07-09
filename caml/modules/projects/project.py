from kubernetes import client
from kubernetes.client.exceptions import ApiException

from caml.errors import CamlNotFoundError
from caml.kube.consts import CAML_COMPUTE_NAMESPACE, CAML_EXTENSION_GROUP
from caml.modules.workspaces import WorkspacesClient


class Project:
    # TODO: decide on dynamic attributes and lazy loading
    attributes = {
        "name": str,
    }

    def __init__(self, name=None, attributes=None):
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
        try:
            return self.project_client.get_namespaced_custom_object(**self.resource_args)
        except ApiException as e:
            if e.status == 404:
                raise CamlNotFoundError("Project not found")

    def to_json(self):
        # TODO: optimize to use attributes
        data = self._get_object_data()
        return data["spec"]

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
                raise CamlNotFoundError("Project not found")

    def _init_clients(self):
        """
        Sets up the clients that are exposed to the user.
        @return: None
        """

        self.workspaces = WorkspacesClient()
