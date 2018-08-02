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

from .connection_info_py3 import ConnectionInfo


class MySqlConnectionInfo(ConnectionInfo):
    """Information for connecting to MySQL source.

    All required parameters must be populated in order to send to Azure.

    :param user_name: User name
    :type user_name: str
    :param password: Password credential.
    :type password: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param server_name: Required. Name of the server
    :type server_name: str
    :param port: Required. Port for Server
    :type port: int
    """

    _validation = {
        'type': {'required': True},
        'server_name': {'required': True},
        'port': {'required': True},
    }

    _attribute_map = {
        'user_name': {'key': 'userName', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'server_name': {'key': 'serverName', 'type': 'str'},
        'port': {'key': 'port', 'type': 'int'},
    }

    def __init__(self, *, server_name: str, port: int, user_name: str=None, password: str=None, **kwargs) -> None:
        super(MySqlConnectionInfo, self).__init__(user_name=user_name, password=password, **kwargs)
        self.server_name = server_name
        self.port = port
        self.type = 'MySqlConnectionInfo'
