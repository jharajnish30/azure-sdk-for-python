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


class SlotSwapStatus(Model):
    """The status of the last successfull slot swap operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar timestamp_utc: The time the last successful slot swap completed.
    :vartype timestamp_utc: datetime
    :ivar source_slot_name: The source slot of the last swap operation.
    :vartype source_slot_name: str
    :ivar destination_slot_name: The destination slot of the last swap
     operation.
    :vartype destination_slot_name: str
    """

    _validation = {
        'timestamp_utc': {'readonly': True},
        'source_slot_name': {'readonly': True},
        'destination_slot_name': {'readonly': True},
    }

    _attribute_map = {
        'timestamp_utc': {'key': 'timestampUtc', 'type': 'iso-8601'},
        'source_slot_name': {'key': 'sourceSlotName', 'type': 'str'},
        'destination_slot_name': {'key': 'destinationSlotName', 'type': 'str'},
    }

    def __init__(self):
        super(SlotSwapStatus, self).__init__()
        self.timestamp_utc = None
        self.source_slot_name = None
        self.destination_slot_name = None
