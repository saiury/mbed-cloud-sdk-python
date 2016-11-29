# coding: utf-8

"""
    mbed Cloud Connect REST API

    mbed Cloud Connect REST API allows web applications to communicate with devices.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ResourcesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def v2_endpoints_endpoint_name_resource_path_delete(self, endpoint_name, _resource_path, **kwargs):
        """
        Delete a resource
        A request to delete a resource must be handled by both mbed Cloud Client and mbed Cloud Connect. The resource is not deleted from mbed Cloud Connect until the delete is handled by mbed Cloud Client.  All resource APIs are asynchronous. Note that these APIs respond only if the device is turned on and connected to mbed Cloud Connect. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_endpoint_name_resource_path_delete(endpoint_name, _resource_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str endpoint_name: A unique identifier for the endpoint. Note that the endpoint-name must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource's url.  (required)
        :param bool no_resp: **Non-confirmable requests**  All resource APIs have the parameter noResp. If you make a request with noResp=true, mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_endpoints_endpoint_name_resource_path_delete_with_http_info(endpoint_name, _resource_path, **kwargs)
        else:
            (data) = self.v2_endpoints_endpoint_name_resource_path_delete_with_http_info(endpoint_name, _resource_path, **kwargs)
            return data

    def v2_endpoints_endpoint_name_resource_path_delete_with_http_info(self, endpoint_name, _resource_path, **kwargs):
        """
        Delete a resource
        A request to delete a resource must be handled by both mbed Cloud Client and mbed Cloud Connect. The resource is not deleted from mbed Cloud Connect until the delete is handled by mbed Cloud Client.  All resource APIs are asynchronous. Note that these APIs respond only if the device is turned on and connected to mbed Cloud Connect. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_endpoint_name_resource_path_delete_with_http_info(endpoint_name, _resource_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str endpoint_name: A unique identifier for the endpoint. Note that the endpoint-name must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource's url.  (required)
        :param bool no_resp: **Non-confirmable requests**  All resource APIs have the parameter noResp. If you make a request with noResp=true, mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_name', '_resource_path', 'no_resp']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_endpoint_name_resource_path_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_name' is set
        if ('endpoint_name' not in params) or (params['endpoint_name'] is None):
            raise ValueError("Missing the required parameter `endpoint_name` when calling `v2_endpoints_endpoint_name_resource_path_delete`")
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params) or (params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `v2_endpoints_endpoint_name_resource_path_delete`")

        resource_path = '/v2/endpoints/{endpointName}/{resourcePath}'.replace('{format}', 'json')
        path_params = {}
        if 'endpoint_name' in params:
            path_params['endpointName'] = params['endpoint_name']
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']

        query_params = {}
        if 'no_resp' in params:
            query_params['noResp'] = params['no_resp']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AsyncID',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_endpoints_endpoint_name_resource_path_get(self, endpoint_name, _resource_path, **kwargs):
        """
        Read from a resource
        Requests the resource value and when the response is available, a json AsycResponse object (AsyncIDResponse object) is received in the notification channel. Note that you can also receive notifications when a resource changes. The preferred way to get resource values is to use subscribe and callback methods.  All resource APIs are asynchronous. Note that these APIs will only respond if the device is turned on and connected to mbed Cloud Connect. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_endpoint_name_resource_path_get(endpoint_name, _resource_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str endpoint_name: Unique identifier for the endpoint. Note that the endpoint name needs to be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource's url.  (required)
        :param bool cache_only: If true, the response comes only from the cache. Default: false. 
        :param bool no_resp: **Non-confirmable requests**  All resource APIs have the parameter noResp. If a request is made with noResp=true, mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_endpoints_endpoint_name_resource_path_get_with_http_info(endpoint_name, _resource_path, **kwargs)
        else:
            (data) = self.v2_endpoints_endpoint_name_resource_path_get_with_http_info(endpoint_name, _resource_path, **kwargs)
            return data

    def v2_endpoints_endpoint_name_resource_path_get_with_http_info(self, endpoint_name, _resource_path, **kwargs):
        """
        Read from a resource
        Requests the resource value and when the response is available, a json AsycResponse object (AsyncIDResponse object) is received in the notification channel. Note that you can also receive notifications when a resource changes. The preferred way to get resource values is to use subscribe and callback methods.  All resource APIs are asynchronous. Note that these APIs will only respond if the device is turned on and connected to mbed Cloud Connect. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_endpoint_name_resource_path_get_with_http_info(endpoint_name, _resource_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str endpoint_name: Unique identifier for the endpoint. Note that the endpoint name needs to be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource's url.  (required)
        :param bool cache_only: If true, the response comes only from the cache. Default: false. 
        :param bool no_resp: **Non-confirmable requests**  All resource APIs have the parameter noResp. If a request is made with noResp=true, mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_name', '_resource_path', 'cache_only', 'no_resp']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_endpoint_name_resource_path_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_name' is set
        if ('endpoint_name' not in params) or (params['endpoint_name'] is None):
            raise ValueError("Missing the required parameter `endpoint_name` when calling `v2_endpoints_endpoint_name_resource_path_get`")
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params) or (params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `v2_endpoints_endpoint_name_resource_path_get`")

        resource_path = '/v2/endpoints/{endpointName}/{resourcePath}'.replace('{format}', 'json')
        path_params = {}
        if 'endpoint_name' in params:
            path_params['endpointName'] = params['endpoint_name']
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']

        query_params = {}
        if 'cache_only' in params:
            query_params['cacheOnly'] = params['cache_only']
        if 'no_resp' in params:
            query_params['noResp'] = params['no_resp']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AsyncID',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_endpoints_endpoint_name_resource_path_post(self, endpoint_name, _resource_path, **kwargs):
        """
        Execute a function on a resource
        With this API, you can execute a function on an existing resource.  All resource APIs are asynchronous. Note that these APIs respond only if the device is turned on and connected to mbed Cloud Connect. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_endpoint_name_resource_path_post(endpoint_name, _resource_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str endpoint_name: A unique identifier for the endpoint. Note that the endpoint-name must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource's url. (required)
        :param str resource_function: This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in mbed Cloud Client. 
        :param bool no_resp: **Non-confirmable requests**  All resource APIs have the parameter noResp. If you make a request with noResp=true, mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_endpoints_endpoint_name_resource_path_post_with_http_info(endpoint_name, _resource_path, **kwargs)
        else:
            (data) = self.v2_endpoints_endpoint_name_resource_path_post_with_http_info(endpoint_name, _resource_path, **kwargs)
            return data

    def v2_endpoints_endpoint_name_resource_path_post_with_http_info(self, endpoint_name, _resource_path, **kwargs):
        """
        Execute a function on a resource
        With this API, you can execute a function on an existing resource.  All resource APIs are asynchronous. Note that these APIs respond only if the device is turned on and connected to mbed Cloud Connect. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_endpoint_name_resource_path_post_with_http_info(endpoint_name, _resource_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str endpoint_name: A unique identifier for the endpoint. Note that the endpoint-name must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource's url. (required)
        :param str resource_function: This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in mbed Cloud Client. 
        :param bool no_resp: **Non-confirmable requests**  All resource APIs have the parameter noResp. If you make a request with noResp=true, mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_name', '_resource_path', 'resource_function', 'no_resp']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_endpoint_name_resource_path_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_name' is set
        if ('endpoint_name' not in params) or (params['endpoint_name'] is None):
            raise ValueError("Missing the required parameter `endpoint_name` when calling `v2_endpoints_endpoint_name_resource_path_post`")
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params) or (params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `v2_endpoints_endpoint_name_resource_path_post`")

        resource_path = '/v2/endpoints/{endpointName}/{resourcePath}'.replace('{format}', 'json')
        path_params = {}
        if 'endpoint_name' in params:
            path_params['endpointName'] = params['endpoint_name']
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']

        query_params = {}
        if 'no_resp' in params:
            query_params['noResp'] = params['no_resp']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resource_function' in params:
            body_params = params['resource_function']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain', 'application/xml', 'application/octet-stream', 'application/exi', 'application/json', 'application/link-format', 'application/senml+json', 'application/nanoservice-tlv', 'application/vnd.oma.lwm2m+text', 'application/vnd.oma.lwm2m+opaq', 'application/vnd.oma.lwm2m+tlv', 'application/vnd.oma.lwm2m+json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AsyncID',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_endpoints_endpoint_name_resource_path_put(self, endpoint_name, _resource_path, resource_value, **kwargs):
        """
        Write to a resource
        With this API, you can write new values to existing resources, or create new resources on the device. The resource-path does not have to exist - it can be created by the call.  All resource APIs are asynchronous. Note that these APIs respond only if the device is turned on and connected to mbed Cloud Connect. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_endpoint_name_resource_path_put(endpoint_name, _resource_path, resource_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str endpoint_name: A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource's url. (required)
        :param str resource_value: Value to be set to the resource. (Check accceptable content-types)  (required)
        :param bool no_resp: **Non-confirmable requests**  All resource APIs have the parameter noResp. If you make a request with noResp=true, mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_endpoints_endpoint_name_resource_path_put_with_http_info(endpoint_name, _resource_path, resource_value, **kwargs)
        else:
            (data) = self.v2_endpoints_endpoint_name_resource_path_put_with_http_info(endpoint_name, _resource_path, resource_value, **kwargs)
            return data

    def v2_endpoints_endpoint_name_resource_path_put_with_http_info(self, endpoint_name, _resource_path, resource_value, **kwargs):
        """
        Write to a resource
        With this API, you can write new values to existing resources, or create new resources on the device. The resource-path does not have to exist - it can be created by the call.  All resource APIs are asynchronous. Note that these APIs respond only if the device is turned on and connected to mbed Cloud Connect. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_endpoints_endpoint_name_resource_path_put_with_http_info(endpoint_name, _resource_path, resource_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str endpoint_name: A unique identifier for the endpoint. Note that the endpoint name must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource's url. (required)
        :param str resource_value: Value to be set to the resource. (Check accceptable content-types)  (required)
        :param bool no_resp: **Non-confirmable requests**  All resource APIs have the parameter noResp. If you make a request with noResp=true, mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code 204 No Content. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code 409 Conflict. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_name', '_resource_path', 'resource_value', 'no_resp']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_endpoint_name_resource_path_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_name' is set
        if ('endpoint_name' not in params) or (params['endpoint_name'] is None):
            raise ValueError("Missing the required parameter `endpoint_name` when calling `v2_endpoints_endpoint_name_resource_path_put`")
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params) or (params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `v2_endpoints_endpoint_name_resource_path_put`")
        # verify the required parameter 'resource_value' is set
        if ('resource_value' not in params) or (params['resource_value'] is None):
            raise ValueError("Missing the required parameter `resource_value` when calling `v2_endpoints_endpoint_name_resource_path_put`")

        resource_path = '/v2/endpoints/{endpointName}/{resourcePath}'.replace('{format}', 'json')
        path_params = {}
        if 'endpoint_name' in params:
            path_params['endpointName'] = params['endpoint_name']
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']

        query_params = {}
        if 'no_resp' in params:
            query_params['noResp'] = params['no_resp']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resource_value' in params:
            body_params = params['resource_value']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain', 'application/xml', 'application/octet-stream', 'application/exi', 'application/json', 'application/link-format', 'application/senml+json', 'application/nanoservice-tlv', 'application/vnd.oma.lwm2m+text', 'application/vnd.oma.lwm2m+opaq', 'application/vnd.oma.lwm2m+tlv', 'application/vnd.oma.lwm2m+json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AsyncID',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
