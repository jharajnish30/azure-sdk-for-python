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


class RedirectIncompatibleRowSettings(Model):
    """Redirect incompatible row settings.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param linked_service_name: Name of the Azure Storage, Storage SAS, or
     Azure Data Lake Store linked service used for redirecting incompatible
     row. Must be specified if redirectIncompatibleRowSettings is specified.
     Type: string (or Expression with resultType string).
    :type linked_service_name: object
    :param path: The path for storing the redirect incompatible row data.
     Type: string (or Expression with resultType string).
    :type path: object
    """

    _validation = {
        'linked_service_name': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'object'},
        'path': {'key': 'path', 'type': 'object'},
    }

    def __init__(self, linked_service_name, additional_properties=None, path=None):
        super(RedirectIncompatibleRowSettings, self).__init__()
        self.additional_properties = additional_properties
        self.linked_service_name = linked_service_name
        self.path = path
