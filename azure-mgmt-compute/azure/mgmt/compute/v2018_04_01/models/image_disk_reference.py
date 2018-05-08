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


class ImageDiskReference(Model):
    """The source image used for creating the disk.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A relative uri containing either a Platform Imgage
     Repository or user image reference.
    :type id: str
    :param lun: If the disk is created from an image's data disk, this is an
     index that indicates which of the data disks in the image to use. For OS
     disks, this field is null.
    :type lun: int
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'lun': {'key': 'lun', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ImageDiskReference, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.lun = kwargs.get('lun', None)