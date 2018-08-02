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

from .migrate_sql_server_sql_db_sync_task_output_py3 import MigrateSqlServerSqlDbSyncTaskOutput


class MigrateSqlServerSqlDbSyncTaskOutputMigrationLevel(MigrateSqlServerSqlDbSyncTaskOutput):
    """MigrateSqlServerSqlDbSyncTaskOutputMigrationLevel.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar started_on: Migration start time
    :vartype started_on: datetime
    :ivar ended_on: Migration end time
    :vartype ended_on: datetime
    :ivar state: Current state of migration. Possible values include:
     'UNDEFINED', 'VALIDATING', 'PENDING', 'COMPLETE', 'ACTION_REQUIRED',
     'FAILED'
    :vartype state: str or ~azure.mgmt.datamigration.models.SyncMigrationState
    :ivar source_server_version: Source server version
    :vartype source_server_version: str
    :ivar source_server: Source server name
    :vartype source_server: str
    :ivar target_server_version: Target server version
    :vartype target_server_version: str
    :ivar target_server: Target server name
    :vartype target_server: str
    :ivar database_count: Count of databases
    :vartype database_count: int
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'started_on': {'readonly': True},
        'ended_on': {'readonly': True},
        'state': {'readonly': True},
        'source_server_version': {'readonly': True},
        'source_server': {'readonly': True},
        'target_server_version': {'readonly': True},
        'target_server': {'readonly': True},
        'database_count': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'ended_on': {'key': 'endedOn', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'source_server_version': {'key': 'sourceServerVersion', 'type': 'str'},
        'source_server': {'key': 'sourceServer', 'type': 'str'},
        'target_server_version': {'key': 'targetServerVersion', 'type': 'str'},
        'target_server': {'key': 'targetServer', 'type': 'str'},
        'database_count': {'key': 'databaseCount', 'type': 'int'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrateSqlServerSqlDbSyncTaskOutputMigrationLevel, self).__init__(**kwargs)
        self.started_on = None
        self.ended_on = None
        self.state = None
        self.source_server_version = None
        self.source_server = None
        self.target_server_version = None
        self.target_server = None
        self.database_count = None
        self.result_type = 'MigrationLevelOutput'
