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


class ConnectToTargetSqlSqlDbSyncTaskInput(Model):
    """Input for the task that validates connection to SQL DB and target server
    requirements.

    All required parameters must be populated in order to send to Azure.

    :param source_connection_info: Required. Connection information for Source
     SQL Server
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param target_connection_info: Required. Connection information for target
     SQL DB
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    """

    _validation = {
        'source_connection_info': {'required': True},
        'target_connection_info': {'required': True},
    }

    _attribute_map = {
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'SqlConnectionInfo'},
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'SqlConnectionInfo'},
    }

    def __init__(self, *, source_connection_info, target_connection_info, **kwargs) -> None:
        super(ConnectToTargetSqlSqlDbSyncTaskInput, self).__init__(**kwargs)
        self.source_connection_info = source_connection_info
        self.target_connection_info = target_connection_info
