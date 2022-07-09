from kubernetes import client
from kubernetes.client.exceptions import ApiException

from caml.kube.consts import CAML_COMPUTE_NAMESPACE

from caml.modules.workspaces.jupyter_notebook import JupyterNotebook


class WORKSPACES:
    JUPYTER_NOTEBOOK = JupyterNotebook


class WorkspacesClient:
    def __init__(self):
        # TODO: change
        self.project = "test"
        self.apps_api = client.AppsV1Api()

    def create(self, ws_class, name):
        if not WORKSPACES.validate_workspace(ws_class):
            raise Exception("no no")

        workspace = ws_class(project=self.project, name=name)

        try:
            self.apps_api.create_namespaced_deployment(namespace=CAML_COMPUTE_NAMESPACE, body=workspace.body)
        except ApiException as e:
            if e.status == 409:
                raise Exception("duplicato")
            if e.status == 422:
                print("invalid!")
                raise e

    def list(self):
        label_selector = f"project={self.project}"
        response = self.apps_api.list_namespaced_deployment(namespace=CAML_COMPUTE_NAMESPACE, label_selector=label_selector)
        return response["items"]
