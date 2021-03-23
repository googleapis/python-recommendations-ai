# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry import (
    pagers,
)
from google.cloud.recommendationengine_v1beta1.types import (
    prediction_apikey_registry_service,
)

from .transports.base import PredictionApiKeyRegistryTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import PredictionApiKeyRegistryGrpcAsyncIOTransport
from .client import PredictionApiKeyRegistryClient


class PredictionApiKeyRegistryAsyncClient:
    """Service for registering API keys for use with the ``predict``
    method. If you use an API key to request predictions, you must first
    register the API key. Otherwise, your prediction request is
    rejected. If you use OAuth to authenticate your ``predict`` method
    call, you do not need to register an API key. You can register up to
    20 API keys per project.
    """

    _client: PredictionApiKeyRegistryClient

    DEFAULT_ENDPOINT = PredictionApiKeyRegistryClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PredictionApiKeyRegistryClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        PredictionApiKeyRegistryClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        PredictionApiKeyRegistryClient.parse_common_billing_account_path
    )

    common_folder_path = staticmethod(PredictionApiKeyRegistryClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        PredictionApiKeyRegistryClient.parse_common_folder_path
    )

    common_organization_path = staticmethod(
        PredictionApiKeyRegistryClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        PredictionApiKeyRegistryClient.parse_common_organization_path
    )

    common_project_path = staticmethod(
        PredictionApiKeyRegistryClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        PredictionApiKeyRegistryClient.parse_common_project_path
    )

    common_location_path = staticmethod(
        PredictionApiKeyRegistryClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        PredictionApiKeyRegistryClient.parse_common_location_path
    )

    from_service_account_info = PredictionApiKeyRegistryClient.from_service_account_info
    from_service_account_file = PredictionApiKeyRegistryClient.from_service_account_file
    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> PredictionApiKeyRegistryTransport:
        """Return the transport used by the client instance.

        Returns:
            PredictionApiKeyRegistryTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(PredictionApiKeyRegistryClient).get_transport_class,
        type(PredictionApiKeyRegistryClient),
    )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, PredictionApiKeyRegistryTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the prediction api key registry client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PredictionApiKeyRegistryTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """

        self._client = PredictionApiKeyRegistryClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_prediction_api_key_registration(
        self,
        request: prediction_apikey_registry_service.CreatePredictionApiKeyRegistrationRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> prediction_apikey_registry_service.PredictionApiKeyRegistration:
        r"""Register an API key for use with predict method.

        Args:
            request (:class:`google.cloud.recommendationengine_v1beta1.types.CreatePredictionApiKeyRegistrationRequest`):
                The request object. Request message for the
                `CreatePredictionApiKeyRegistration` method.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommendationengine_v1beta1.types.PredictionApiKeyRegistration:
                Registered Api Key.
        """
        # Create or coerce a protobuf request object.

        request = prediction_apikey_registry_service.CreatePredictionApiKeyRegistrationRequest(
            request
        )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_prediction_api_key_registration,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_prediction_api_key_registrations(
        self,
        request: prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPredictionApiKeyRegistrationsAsyncPager:
        r"""List the registered apiKeys for use with predict
        method.

        Args:
            request (:class:`google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsRequest`):
                The request object. Request message for the
                `ListPredictionApiKeyRegistrations`.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry.pagers.ListPredictionApiKeyRegistrationsAsyncPager:
                Response message for the
                ListPredictionApiKeyRegistrations.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.

        request = prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest(
            request
        )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_prediction_api_key_registrations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListPredictionApiKeyRegistrationsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_prediction_api_key_registration(
        self,
        request: prediction_apikey_registry_service.DeletePredictionApiKeyRegistrationRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Unregister an apiKey from using for predict method.

        Args:
            request (:class:`google.cloud.recommendationengine_v1beta1.types.DeletePredictionApiKeyRegistrationRequest`):
                The request object. Request message for
                `DeletePredictionApiKeyRegistration` method.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.

        request = prediction_apikey_registry_service.DeletePredictionApiKeyRegistrationRequest(
            request
        )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_prediction_api_key_registration,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-recommendations-ai",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("PredictionApiKeyRegistryAsyncClient",)
