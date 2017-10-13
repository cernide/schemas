from kubernetes import client

from polyaxon_schemas.k8s.templates import constants


def get_cluster_config_map(project, experiment, cluster_def):
    name = constants.CONFIG_MAP_CLUSTER_NAME.format(project, experiment)
    metadata = client.V1ObjectMeta(name=name)
    return client.V1ConfigMap(api_version=constants.K8S_API_VERSION_V1,
                              kind=constants.K8S_CONFIG_MAP_KIND,
                              metadata=metadata,
                              data=cluster_def)
