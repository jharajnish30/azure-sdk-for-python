# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentPropertiesExtended(Model):
    """Deployment properties with additional details.

    :param provisioning_state: Gets or sets the state of the provisioning.
    :type provisioning_state: str
    :param correlation_id: Gets or sets the correlation ID of the deployment.
    :type correlation_id: str
    :param timestamp: Gets or sets the timestamp of the template deployment.
    :type timestamp: datetime
    :param outputs: Gets or sets key/value pairs that represent
     deploymentoutput.
    :type outputs: object
    :param providers: Gets the list of resource providers needed for the
     deployment.
    :type providers: list of :class:`Provider
     <azure.mgmt.resource.resources.models.Provider>`
    :param dependencies: Gets the list of deployment dependencies.
    :type dependencies: list of :class:`Dependency
     <azure.mgmt.resource.resources.models.Dependency>`
    :param template: Gets or sets the template content. Use only one of
     Template or TemplateLink.
    :type template: object
    :param template_link: Gets or sets the URI referencing the template. Use
     only one of Template or TemplateLink.
    :type template_link: :class:`TemplateLink
     <azure.mgmt.resource.resources.models.TemplateLink>`
    :param parameters: Deployment parameters. Use only one of Parameters or
     ParametersLink.
    :type parameters: object
    :param parameters_link: Gets or sets the URI referencing the parameters.
     Use only one of Parameters or ParametersLink.
    :type parameters_link: :class:`ParametersLink
     <azure.mgmt.resource.resources.models.ParametersLink>`
    :param mode: Gets or sets the deployment mode. Possible values include:
     'Incremental', 'Complete'
    :type mode: str or :class:`DeploymentMode
     <azure.mgmt.resource.resources.models.DeploymentMode>`
    :param debug_setting: Gets or sets the debug setting of the deployment.
    :type debug_setting: :class:`DebugSetting
     <azure.mgmt.resource.resources.models.DebugSetting>`
    """ 

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'outputs': {'key': 'outputs', 'type': 'object'},
        'providers': {'key': 'providers', 'type': '[Provider]'},
        'dependencies': {'key': 'dependencies', 'type': '[Dependency]'},
        'template': {'key': 'template', 'type': 'object'},
        'template_link': {'key': 'templateLink', 'type': 'TemplateLink'},
        'parameters': {'key': 'parameters', 'type': 'object'},
        'parameters_link': {'key': 'parametersLink', 'type': 'ParametersLink'},
        'mode': {'key': 'mode', 'type': 'DeploymentMode'},
        'debug_setting': {'key': 'debugSetting', 'type': 'DebugSetting'},
    }

    def __init__(self, provisioning_state=None, correlation_id=None, timestamp=None, outputs=None, providers=None, dependencies=None, template=None, template_link=None, parameters=None, parameters_link=None, mode=None, debug_setting=None):
        self.provisioning_state = provisioning_state
        self.correlation_id = correlation_id
        self.timestamp = timestamp
        self.outputs = outputs
        self.providers = providers
        self.dependencies = dependencies
        self.template = template
        self.template_link = template_link
        self.parameters = parameters
        self.parameters_link = parameters_link
        self.mode = mode
        self.debug_setting = debug_setting