import os
import pathlib

from kubernetes import client, config

from caml.kube.utils import replace_yaml_placeholders
from caml.kube.consts import CAML_INFRA_NAMESPACE, CAML_COMPUTE_NAMESPACE

from caml.modules.projects import ProjectsClient


class Caml:
    def __init__(self, kube_config):
        # Init the kube config
        if kube_config:
            config.load_kube_config(config_file=kube_config)
        else:
            # To use the CLI/SDK inside of the cluster
            config.load_incluster_config()

        self._init_clients()

    @staticmethod
    def deploy_caml(kube_config: str, **kwargs):
        """
        Deploys a new CAML platform to kubernetes
        NOTE: Deploying on an existing CAML installation will override it.
        :param kube_config: [String] The path to the kube config file.

        :param caml_infra_namespace: [String] Override default caml infra namespace.
        :param caml_compute_namespace: [String] Override default caml compute namespace.
        :return: None
        """

        print("init kube config")
        # Init the kube config
        if kube_config:
            config.load_kube_config(config_file=kube_config)
        else:
            # To use the CLI/SDK inside of the cluster
            config.load_incluster_config()

        core_api = client.CoreV1Api()
        api_reg_api = client.ApiextensionsV1Api()
        schema_path = os.path.join(pathlib.Path(__file__).parent, "kube/schemas")

        print("creating infra namespace")
        infra_namespace_body = replace_yaml_placeholders(f"{schema_path}/namespace.yml", {
            "NAMESPACE_NAME": kwargs.get("caml_infra_namespace", CAML_INFRA_NAMESPACE)
        })
        infra_namespace = core_api.create_namespace(body=infra_namespace_body)

        print("creating compute namespace")
        compute_namespace_body = replace_yaml_placeholders(f"{schema_path}/namespace.yml", {
            "NAMESPACE_NAME": kwargs.get("caml_compute_namespace", CAML_COMPUTE_NAMESPACE)
        })
        compute_namespace = core_api.create_namespace(body=compute_namespace_body)

        print("creating custom resources")
        # Projects
        project_resource_body = replace_yaml_placeholders(f"{schema_path}/project.yml", {})
        api_reg_api.create_custom_resource_definition(project_resource_body)

        if infra_namespace.status.phase == "Active" and compute_namespace.status.phase == "Active":
            print("yayy")
        else:
            print("nayy")


    @staticmethod
    def destroy_caml(kube_config: str, **kwargs):
        """
        Destroys CAML namespaces and local configuration files
        :param kube_config:
        :param kwargs:
        :return:
        """
        print("init kube config")
        # Init the kube config
        if kube_config:
            config.load_kube_config(config_file=kube_config)
        else:
            # To use the CLI/SDK inside of the cluster
            config.load_incluster_config()

        # TODO: fix
        print("deleting caml")
        core_api = client.CoreV1Api()
        core_api.delete_namespace(name=CAML_INFRA_NAMESPACE)
        core_api.delete_namespace(name=CAML_COMPUTE_NAMESPACE)

        api_reg_api = client.ApiextensionsV1Api()
        api_reg_api.delete_custom_resource_definition(name="projects.extensions.caml.io")


    @staticmethod
    def connect_caml():
        pass

    def _init_clients(self):
        """
        Sets up the clients that are exposed to the user.
        @return: None
        """

        self.projects = ProjectsClient()

