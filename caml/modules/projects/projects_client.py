from kubernetes import client
from kubernetes.client.exceptions import ApiException

from caml.kube.consts import CAML_EXTENSION_GROUP, CAML_COMPUTE_NAMESPACE
from caml.modules.projects.project import Project


class ProjectsClient:
    def __init__(self):
        self.resource_args = {
            "group": CAML_EXTENSION_GROUP,
            "plural": "projects",
            "version": "v1",
            "namespace": CAML_COMPUTE_NAMESPACE
        }

        self.project_client = client.CustomObjectsApi()

    def create(self, name):
        body = {
            "apiVersion": f"{CAML_EXTENSION_GROUP}/v1",
            "kind": "Project",
            "metadata": {"name": name},
            "spec": {
                "name": name
            }
        }
        try:
            response = self.project_client.create_namespaced_custom_object(**self.resource_args, body=body)
            return response.items()
        except ApiException as e:
            if e.status == 409:
                print("conflict!")

    def list(self):
        response = self.project_client.list_namespaced_custom_object(**self.resource_args)
        return response["items"]

    def get(self, name):
        return Project(name)

    def delete(self, name):
        try:
            self.project_client.delete_namespaced_custom_object(**self.resource_args, name=name)
        except ApiException as e:
            if e.status == 404:
                print("not found!")
