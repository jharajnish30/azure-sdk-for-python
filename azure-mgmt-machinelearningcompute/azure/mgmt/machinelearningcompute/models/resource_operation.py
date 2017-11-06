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


class ResourceOperation(Model):
    """Resource operation.

    :param name: Name of this operation.
    :type name: str
    :param display: Display of the operation.
    :type display:
     ~azure.mgmt.machinelearningcompute.models.ResourceOperationDisplay
    :param origin: The operation origin.
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceOperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, name=None, display=None, origin=None):
        self.name = name
        self.display = display
        self.origin = origin