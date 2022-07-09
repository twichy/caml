from kubernetes import client
from kubernetes.client.exceptions import ApiException


class Workspace:
    # TODO: decide on dynamic attributes and lazy loading
    attributes = {
        "name": str,
    }

    def __init__(self, project, name, attributes=None):
        if attributes:
            self.attributes = {**attributes}

        self.name = name
        self.project = project

        self.core_api = client.CoreV1Api()
        self.apps_api = client.AppsV1Api()

    def delete(self):
        """
        Deletes the current project
        @return: None
        """
        try:
            self.project_client.create_namespaced_deployment(**self.resource_args)
        except ApiException as e:
            if e.status == 404:
                print("not found!")
