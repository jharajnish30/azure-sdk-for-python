# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IntegrationRuntimeStatus(Model):
    """Integration runtime status.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SelfHostedIntegrationRuntimeStatus,
    ManagedIntegrationRuntimeStatus

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :ivar state: The state of integration runtime. Possible values include:
     'Initial', 'Stopped', 'Started', 'Starting', 'Stopping',
     'NeedRegistration', 'Online', 'Limited', 'Offline'
    :vartype state: str or
     ~azure.mgmt.datafactory.models.IntegrationRuntimeState
    :param type: Constant filled by server.
    :type type: str
    """

    _validation = {
        'state': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'state': {'key': 'state', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'SelfHosted': 'SelfHostedIntegrationRuntimeStatus', 'Managed': 'ManagedIntegrationRuntimeStatus'}
    }

    def __init__(self, additional_properties=None):
        super(IntegrationRuntimeStatus, self).__init__()
        self.additional_properties = additional_properties
        self.state = None
        self.type = None
