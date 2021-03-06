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


class ExitCodeMapping(Model):
    """How the Batch service should respond if a task exits with a particular exit
    code.

    :param code: A process exit code.
    :type code: int
    :param exit_options: How the Batch service should respond if the task
     exits with this exit code.
    :type exit_options: ~azure.batch.models.ExitOptions
    """

    _validation = {
        'code': {'required': True},
        'exit_options': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'exit_options': {'key': 'exitOptions', 'type': 'ExitOptions'},
    }

    def __init__(self, code, exit_options):
        super(ExitCodeMapping, self).__init__()
        self.code = code
        self.exit_options = exit_options
