from kubernetes import client
from kubernetes.client.exceptions import ApiException

from caml.kube.consts import CAML_COMPUTE_NAMESPACE
from caml.modules.workspaces.jupyter_notebook import JupyterNotebook
from caml.modules.workspaces.workspace import Workspace


class WORKSPACES:
    JUPYTER_NOTEBOOK = JupyterNotebook


class WorkspacesClient:
    def __init__(self, project="test"):
        # TODO: change project to required
        self.project = project
        self.core_api = client.CoreV1Api()
        self.apps_api = client.AppsV1Api()

    def create(self, ws_class, name):
        # TODO: validate workspace

        workspace = ws_class(project=self.project, name=name)

        try:
            self.apps_api.create_namespaced_deployment(namespace=CAML_COMPUTE_NAMESPACE, body=workspace.deployment)
        except ApiException as e:
            if e.status == 409:
                raise Exception("duplicato")
            if e.status == 422:
                print("invalid!")
                raise e

        try:
            hue = self.core_api.create_namespaced_service(namespace=CAML_COMPUTE_NAMESPACE, body=workspace.service)
        except ApiException as e:
            if e.status == 409:
                raise Exception("duplicato")
            if e.status == 422:
                print("invalid!")
                raise e

        return Workspace(project=self.project, name=name)

    def list(self):
        label_selector = f"project={self.project}"
        response = self.apps_api.list_namespaced_deployment(
            namespace=CAML_COMPUTE_NAMESPACE,
            label_selector=label_selector
        )

        workspaces = []
        for item in response.items:
            workspace = Workspace(project=self.project, name=item.metadata.name, attributes=item.spec)
            workspaces.append(workspace)
        return workspaces
