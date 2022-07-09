import os
import pathlib

from caml.kube.utils import replace_yaml_placeholders


class JupyterNotebook:
    def __init__(self, project, name, cpu=2, cpu_limit=2, memory=2, memory_limit=2):
        self.name = name
        self.project = project

        self.cpu = cpu
        self.cpu_limit = cpu_limit

        self.memory = memory
        self.memory_limit = memory_limit

        self._create_deployment()
        self._create_service()

    def _create_deployment(self):
        resource_yaml = "deployment.yml"
        placeholders = {
            "APP_LABEL": "jupyter-notebook",
            "PROJECT_LABEL": self.project,
            "COMPONENT_LABEL": "workspace",
            "DEPLOYMENT_NAME": f"workspace-{self.project}-{self.name}",
            "DEPLOYMENT_IMAGE": "jupyter/datascience-notebook",

            "WRAPPER_PORT": "8888",

            "DEPLOYMENT_CPU_LIMIT": f"{self.cpu_limit}",
            "DEPLOYMENT_CPU_REQUEST": f"{self.cpu}",
            "DEPLOYMENT_MEMORY_LIMIT": f"{self.memory_limit}G",
            "DEPLOYMENT_MEMORY_REQUEST": f"{self.memory}G",
        }

        schema_path = os.path.join(pathlib.Path(__file__).parent, f"schemas/{resource_yaml}")
        self.body = replace_yaml_placeholders(schema_path, placeholders)

    def _create_service(self):
        resource_yaml = "service.yml"
        placeholders = {
            "APP_LABEL": "jupyter-notebook",
            "PROJECT_LABEL": self.project,
            "COMPONENT_LABEL": "workspace",
            "DEPLOYMENT_NAME": f"workspace-{self.project}-{self.name}",
            "DEPLOYMENT_IMAGE": "jupyter/datascience-notebook",

            "WRAPPER_PORT": "8888",

            "DEPLOYMENT_CPU_LIMIT": "2",
            "DEPLOYMENT_CPU_REQUEST": "2",
            "DEPLOYMENT_MEMORY_LIMIT": "2G",
            "DEPLOYMENT_MEMORY_REQUEST": "2G",
        }

        schema_path = os.path.join(pathlib.Path(__file__).parent, f"schemas/{resource_yaml}")
        self.body = replace_yaml_placeholders(schema_path, placeholders)