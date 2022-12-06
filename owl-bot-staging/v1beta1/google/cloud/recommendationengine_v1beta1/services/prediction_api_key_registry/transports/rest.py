# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.recommendationengine_v1beta1.types import prediction_apikey_registry_service
from google.protobuf import empty_pb2  # type: ignore

from .base import PredictionApiKeyRegistryTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)

# TODO (numeric enums): This file was generated with the option to
#   request that the server respond with enums JSON-encoded as
#   numbers. The code below does not implement that functionality yet.


class PredictionApiKeyRegistryRestInterceptor:
    """Interceptor for PredictionApiKeyRegistry.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PredictionApiKeyRegistryRestTransport.

    .. code-block:: python
        class MyCustomPredictionApiKeyRegistryInterceptor(PredictionApiKeyRegistryRestInterceptor):
            def pre_create_prediction_api_key_registration(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_prediction_api_key_registration(response):
                logging.log(f"Received response: {response}")

            def pre_delete_prediction_api_key_registration(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_list_prediction_api_key_registrations(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_prediction_api_key_registrations(response):
                logging.log(f"Received response: {response}")

        transport = PredictionApiKeyRegistryRestTransport(interceptor=MyCustomPredictionApiKeyRegistryInterceptor())
        client = PredictionApiKeyRegistryClient(transport=transport)


    """
    def pre_create_prediction_api_key_registration(self, request: prediction_apikey_registry_service.CreatePredictionApiKeyRegistrationRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[prediction_apikey_registry_service.CreatePredictionApiKeyRegistrationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_prediction_api_key_registration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PredictionApiKeyRegistry server.
        """
        return request, metadata

    def post_create_prediction_api_key_registration(self, response: prediction_apikey_registry_service.PredictionApiKeyRegistration) -> prediction_apikey_registry_service.PredictionApiKeyRegistration:
        """Post-rpc interceptor for create_prediction_api_key_registration

        Override in a subclass to manipulate the response
        after it is returned by the PredictionApiKeyRegistry server but before
        it is returned to user code.
        """
        return response
    def pre_delete_prediction_api_key_registration(self, request: prediction_apikey_registry_service.DeletePredictionApiKeyRegistrationRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[prediction_apikey_registry_service.DeletePredictionApiKeyRegistrationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_prediction_api_key_registration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PredictionApiKeyRegistry server.
        """
        return request, metadata

    def pre_list_prediction_api_key_registrations(self, request: prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_prediction_api_key_registrations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PredictionApiKeyRegistry server.
        """
        return request, metadata

    def post_list_prediction_api_key_registrations(self, response: prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse) -> prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse:
        """Post-rpc interceptor for list_prediction_api_key_registrations

        Override in a subclass to manipulate the response
        after it is returned by the PredictionApiKeyRegistry server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class PredictionApiKeyRegistryRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PredictionApiKeyRegistryRestInterceptor


class PredictionApiKeyRegistryRestTransport(PredictionApiKeyRegistryTransport):
    """REST backend transport for PredictionApiKeyRegistry.

    Service for registering API keys for use with the ``predict``
    method. If you use an API key to request predictions, you must first
    register the API key. Otherwise, your prediction request is
    rejected. If you use OAuth to authenticate your ``predict`` method
    call, you do not need to register an API key. You can register up to
    20 API keys per project.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(self, *,
            host: str = 'recommendationengine.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[PredictionApiKeyRegistryRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or PredictionApiKeyRegistryRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreatePredictionApiKeyRegistration(PredictionApiKeyRegistryRestStub):
        def __hash__(self):
            return hash("CreatePredictionApiKeyRegistration")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: prediction_apikey_registry_service.CreatePredictionApiKeyRegistrationRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> prediction_apikey_registry_service.PredictionApiKeyRegistration:
            r"""Call the create prediction api key
        registration method over HTTP.

            Args:
                request (~.prediction_apikey_registry_service.CreatePredictionApiKeyRegistrationRequest):
                    The request object. Request message for the
                ``CreatePredictionApiKeyRegistration`` method.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.prediction_apikey_registry_service.PredictionApiKeyRegistration:
                    Registered Api Key.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/predictionApiKeyRegistrations',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_create_prediction_api_key_registration(request, metadata)
            pb_request = prediction_apikey_registry_service.CreatePredictionApiKeyRegistrationRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = prediction_apikey_registry_service.PredictionApiKeyRegistration()
            pb_resp = prediction_apikey_registry_service.PredictionApiKeyRegistration.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_prediction_api_key_registration(resp)
            return resp

    class _DeletePredictionApiKeyRegistration(PredictionApiKeyRegistryRestStub):
        def __hash__(self):
            return hash("DeletePredictionApiKeyRegistration")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: prediction_apikey_registry_service.DeletePredictionApiKeyRegistrationRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete prediction api key
        registration method over HTTP.

            Args:
                request (~.prediction_apikey_registry_service.DeletePredictionApiKeyRegistrationRequest):
                    The request object. Request message for
                ``DeletePredictionApiKeyRegistration`` method.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1beta1/{name=projects/*/locations/*/catalogs/*/eventStores/*/predictionApiKeyRegistrations/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_prediction_api_key_registration(request, metadata)
            pb_request = prediction_apikey_registry_service.DeletePredictionApiKeyRegistrationRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _ListPredictionApiKeyRegistrations(PredictionApiKeyRegistryRestStub):
        def __hash__(self):
            return hash("ListPredictionApiKeyRegistrations")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse:
            r"""Call the list prediction api key
        registrations method over HTTP.

            Args:
                request (~.prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest):
                    The request object. Request message for the
                ``ListPredictionApiKeyRegistrations``.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse:
                    Response message for the
                ``ListPredictionApiKeyRegistrations``.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/predictionApiKeyRegistrations',
            },
            ]
            request, metadata = self._interceptor.pre_list_prediction_api_key_registrations(request, metadata)
            pb_request = prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse()
            pb_resp = prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_prediction_api_key_registrations(resp)
            return resp

    @property
    def create_prediction_api_key_registration(self) -> Callable[
            [prediction_apikey_registry_service.CreatePredictionApiKeyRegistrationRequest],
            prediction_apikey_registry_service.PredictionApiKeyRegistration]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePredictionApiKeyRegistration(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_prediction_api_key_registration(self) -> Callable[
            [prediction_apikey_registry_service.DeletePredictionApiKeyRegistrationRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePredictionApiKeyRegistration(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_prediction_api_key_registrations(self) -> Callable[
            [prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest],
            prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPredictionApiKeyRegistrations(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'PredictionApiKeyRegistryRestTransport',
)
