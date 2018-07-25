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

from msrest.pipeline import ClientRawResponse

from .. import models


class ListManagementImageOperations(object):
    """ListManagementImageOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def add_image(
            self, list_id, tag=None, label=None, custom_headers=None, raw=False, **operation_config):
        """Add an image to the list with list Id equal to list Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param tag: Tag for the image.
        :type tag: int
        :param label: The image label.
        :type label: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Image or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.Image
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.add_image.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if tag is not None:
            query_parameters['tag'] = self._serialize.query("tag", tag, 'int')
        if label is not None:
            query_parameters['label'] = self._serialize.query("label", label, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Image', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_image.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}/images'}

    def delete_all_images(
            self, list_id, custom_headers=None, raw=False, **operation_config):
        """Deletes all images from the list with list Id equal to list Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: str or ClientRawResponse if raw=true
        :rtype: str or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.delete_all_images.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_all_images.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}/images'}

    def get_all_image_ids(
            self, list_id, custom_headers=None, raw=False, **operation_config):
        """Gets all image Ids from the list with list Id equal to list Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImageIds or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.ImageIds or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.get_all_image_ids.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImageIds', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_all_image_ids.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}/images'}

    def delete_image(
            self, list_id, image_id, custom_headers=None, raw=False, **operation_config):
        """Deletes an image from the list with list Id and image Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param image_id: Id of the image.
        :type image_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: str or ClientRawResponse if raw=true
        :rtype: str or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.delete_image.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str'),
            'ImageId': self._serialize.url("image_id", image_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_image.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}/images/{ImageId}'}

    def add_image_url_input(
            self, list_id, content_type, tag=None, label=None, data_representation="URL", value=None, custom_headers=None, raw=False, **operation_config):
        """Add an image to the list with list Id equal to list Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param content_type: The content type.
        :type content_type: str
        :param tag: Tag for the image.
        :type tag: int
        :param label: The image label.
        :type label: str
        :param data_representation:
        :type data_representation: str
        :param value:
        :type value: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Image or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.Image
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        image_url = models.BodyModel(data_representation=data_representation, value=value)

        # Construct URL
        url = self.add_image_url_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if tag is not None:
            query_parameters['tag'] = self._serialize.query("tag", tag, 'int')
        if label is not None:
            query_parameters['label'] = self._serialize.query("label", label, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'BodyModel')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Image', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_image_url_input.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}/images'}

    def add_image_file_input(
            self, list_id, image_stream, tag=None, label=None, custom_headers=None, raw=False, callback=None, **operation_config):
        """Add an image to the list with list Id equal to list Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param image_stream: The image file.
        :type image_stream: Generator
        :param tag: Tag for the image.
        :type tag: int
        :param label: The image label.
        :type label: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Image or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.Image
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.add_image_file_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if tag is not None:
            query_parameters['tag'] = self._serialize.query("tag", tag, 'int')
        if label is not None:
            query_parameters['label'] = self._serialize.query("label", label, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'image/gif'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(image_stream, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Image', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_image_file_input.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}/images'}
