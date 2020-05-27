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
import re
from typing import Callable, Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api import httpbody_pb2 as httpbody  # type: ignore
from google.api_core import operation
from google.cloud.recommendationengine_v1beta1.services.user_event_service import pagers
from google.cloud.recommendationengine_v1beta1.types import import_
from google.cloud.recommendationengine_v1beta1.types import user_event
from google.cloud.recommendationengine_v1beta1.types import user_event as gcr_user_event
from google.cloud.recommendationengine_v1beta1.types import user_event_service
from google.protobuf import any_pb2 as any  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore

from .transports.base import UserEventServiceTransport
from .transports.grpc import UserEventServiceGrpcTransport


class UserEventServiceClientMeta(type):
    """Metaclass for the UserEventService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[UserEventServiceTransport]]
    _transport_registry["grpc"] = UserEventServiceGrpcTransport

    def get_transport_class(cls, label: str = None) -> Type[UserEventServiceTransport]:
        """Return an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class UserEventServiceClient(metaclass=UserEventServiceClientMeta):
    """Service for ingesting end user actions on the customer
    website.
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Convert api endpoint to mTLS endpoint.
        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "recommendationengine.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            {@api.name}: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, UserEventServiceTransport] = None,
        client_options: ClientOptions = None,
    ) -> None:
        """Instantiate the user event service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.UserEventServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client.
                (2) If ``transport`` argument is None, ``client_options`` can be
                used to create a mutual TLS transport. If ``client_cert_source``
                is provided, mutual TLS transport will be created with the given
                ``api_endpoint`` or the default mTLS endpoint, and the client
                SSL credentials obtained from ``client_cert_source``.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = ClientOptions.from_dict(client_options)

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, UserEventServiceTransport):
            # transport is a UserEventServiceTransport instance.
            if credentials:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            self._transport = transport
        elif client_options is None or (
            client_options.api_endpoint is None
            and client_options.client_cert_source is None
        ):
            # Don't trigger mTLS if we get an empty ClientOptions.
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials, host=self.DEFAULT_ENDPOINT
            )
        else:
            # We have a non-empty ClientOptions. If client_cert_source is
            # provided, trigger mTLS with user provided endpoint or the default
            # mTLS endpoint.
            if client_options.client_cert_source:
                api_mtls_endpoint = (
                    client_options.api_endpoint
                    if client_options.api_endpoint
                    else self.DEFAULT_MTLS_ENDPOINT
                )
            else:
                api_mtls_endpoint = None

            api_endpoint = (
                client_options.api_endpoint
                if client_options.api_endpoint
                else self.DEFAULT_ENDPOINT
            )

            self._transport = UserEventServiceGrpcTransport(
                credentials=credentials,
                host=api_endpoint,
                api_mtls_endpoint=api_mtls_endpoint,
                client_cert_source=client_options.client_cert_source,
            )

    def write_user_event(
        self,
        request: user_event_service.WriteUserEventRequest = None,
        *,
        parent: str = None,
        user_event: gcr_user_event.UserEvent = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcr_user_event.UserEvent:
        r"""Writes a single user event.

        Args:
            request (:class:`~.user_event_service.WriteUserEventRequest`):
                The request object. Request message for WriteUserEvent
                method.
            parent (:class:`str`):
                Required. The parent eventStore resource name, such as
                "projects/1234/locations/global/catalogs/default_catalog/eventStores/default_event_store".
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_event (:class:`~.gcr_user_event.UserEvent`):
                Required. User event to write.
                This corresponds to the ``user_event`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.gcr_user_event.UserEvent:
                UserEvent captures all metadata
                information recommendation engine needs
                to know about how end users interact
                with customers' website.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, user_event]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = user_event_service.WriteUserEventRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if user_event is not None:
            request.user_event = user_event

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.write_user_event,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Done; return the response.
        return response

    def collect_user_event(
        self,
        request: user_event_service.CollectUserEventRequest = None,
        *,
        parent: str = None,
        user_event: str = None,
        uri: str = None,
        ets: int = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> httpbody.HttpBody:
        r"""Writes a single user event from the browser. This
        uses a GET request to due to browser restriction of
        POST-ing to a 3rd party domain.
        This method is used only by the Recommendations AI
        JavaScript pixel. Users should not call this method
        directly.

        Args:
            request (:class:`~.user_event_service.CollectUserEventRequest`):
                The request object. Request message for CollectUserEvent
                method.
            parent (:class:`str`):
                Required. The parent eventStore name, such as
                "projects/1234/locations/global/catalogs/default_catalog/eventStores/default_event_store".
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_event (:class:`str`):
                Required. URL encoded UserEvent
                proto.
                This corresponds to the ``user_event`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            uri (:class:`str`):
                Optional. The url including cgi-
                arameters but excluding the hash
                fragment. The URL must be truncated to
                1.5K bytes to conservatively be under
                the 2K bytes. This is often more useful
                than the referer url, because many
                browsers only send the domain for 3rd
                party requests.
                This corresponds to the ``uri`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ets (:class:`int`):
                Optional. The event timestamp in
                milliseconds. This prevents browser
                caching of otherwise identical get
                requests. The name is abbreviated to
                reduce the payload bytes.
                This corresponds to the ``ets`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.httpbody.HttpBody:
                Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;
                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest) returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody) returns (google.protobuf.Empty);
                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, user_event, uri, ets]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = user_event_service.CollectUserEventRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if user_event is not None:
            request.user_event = user_event
        if uri is not None:
            request.uri = uri
        if ets is not None:
            request.ets = ets

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.collect_user_event,
            default_timeout=None,
            client_info=_client_info,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Done; return the response.
        return response

    def list_user_events(
        self,
        request: user_event_service.ListUserEventsRequest = None,
        *,
        parent: str = None,
        filter: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListUserEventsPager:
        r"""Gets a list of user events within a time range, with
        potential filtering.

        Args:
            request (:class:`~.user_event_service.ListUserEventsRequest`):
                The request object. Request message for ListUserEvents
                method.
            parent (:class:`str`):
                Required. The parent eventStore resource name, such as
                ``projects/*/locations/*/catalogs/default_catalog/eventStores/default_event_store``
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. Filtering expression to specify restrictions
                over returned events. This is a sequence of terms, where
                each term applies some kind of a restriction to the
                returned user events. Use this expression to restrict
                results to a specific time range, or filter events by
                eventType. eg: eventTime > "2012-04-23T18:25:43.511Z"
                eventsMissingCatalogItems
                eventTime<"2012-04-23T18:25:43.511Z" eventType=search

                We expect only 3 types of fields:

                ::

                   * eventTime: this can be specified a maximum of 2 times, once with a
                     less than operator and once with a greater than operator. The
                     eventTime restrict should result in one contiguous valid eventTime
                     range.

                   * eventType: only 1 eventType restriction can be specified.

                   * eventsMissingCatalogItems: specififying this will restrict results
                     to events for which catalog items were not found in the catalog. The
                     default behavior is to return only those events for which catalog
                     items were found.

                Some examples of valid filters expressions:

                -  Example 1: eventTime > "2012-04-23T18:25:43.511Z"
                   eventTime < "2012-04-23T18:30:43.511Z"
                -  Example 2: eventTime > "2012-04-23T18:25:43.511Z"
                   eventType = detail-page-view
                -  Example 3: eventsMissingCatalogItems eventType =
                   search eventTime < "2018-04-23T18:30:43.511Z"
                -  Example 4: eventTime > "2012-04-23T18:25:43.511Z"
                -  Example 5: eventType = search
                -  Example 6: eventsMissingCatalogItems
                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListUserEventsPager:
                Response message for ListUserEvents
                method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, filter]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = user_event_service.ListUserEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.list_user_events,
            default_timeout=None,
            client_info=_client_info,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListUserEventsPager(
            method=rpc, request=request, response=response
        )

        # Done; return the response.
        return response

    def purge_user_events(
        self,
        request: user_event_service.PurgeUserEventsRequest = None,
        *,
        parent: str = None,
        filter: str = None,
        force: bool = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Deletes permanently all user events specified by the
        filter provided. Depending on the number of events
        specified by the filter, this operation could take hours
        or days to complete. To test a filter, use the list
        command first.

        Args:
            request (:class:`~.user_event_service.PurgeUserEventsRequest`):
                The request object. Request message for PurgeUserEvents
                method.
            parent (:class:`str`):
                Required. The resource name of the event_store under
                which the events are created. The format is
                "projects/${projectId}/locations/global/catalogs/${catalogId}/eventStores/${eventStoreId}".
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Required. The filter string to specify the events to be
                deleted. Empty string filter is not allowed. This filter
                can also be used with ListUserEvents API to list events
                that will be deleted. The eligible fields for filtering
                are:

                -  eventType - UserEvent.eventType field of type string.
                -  eventTime - in ISO 8601 "zulu" format.
                -  visitorId - field of type string. Specifying this
                   will delete all events associated with a visitor.
                -  userId - field of type string. Specifying this will
                   delete all events associated with a user. Example 1:
                   Deleting all events in a time range.
                   ``eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z"``
                   Example 2: Deleting specific eventType in time range.
                   ``eventTime > "2012-04-23T18:25:43.511Z" eventType = "detail-page-view"``
                   Example 3: Deleting all events for a specific visitor
                   ``visitorId = visitor1024`` The filtering fields are
                   assumed to have an implicit AND.
                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            force (:class:`bool`):
                Optional. The default value is false.
                Override this flag to true to actually
                perform the purge. If the field is not
                set to true, a sampling of events to be
                deleted will be returned.
                This corresponds to the ``force`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.user_event_service.PurgeUserEventsResponse``:
                Response of the PurgeUserEventsRequest. If the long
                running operation is successfully done, then this
                message is returned by the
                google.longrunning.Operations.response field.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, filter, force]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = user_event_service.PurgeUserEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter
        if force is not None:
            request.force = force

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.purge_user_events,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            user_event_service.PurgeUserEventsResponse,
            metadata_type=user_event_service.PurgeUserEventsMetadata,
        )

        # Done; return the response.
        return response

    def import_user_events(
        self,
        request: import_.ImportUserEventsRequest = None,
        *,
        parent: str = None,
        request_id: str = None,
        input_config: import_.InputConfig = None,
        errors_config: import_.ImportErrorsConfig = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Bulk import of User events. Request processing might
        be synchronous. Events that already exist are skipped.
        Use this method for backfilling historical user events.
        Operation.response is of type ImportResponse. Note that
        it is possible for a subset of the items to be
        successfully inserted. Operation.metadata is of type
        ImportMetadata.

        Args:
            request (:class:`~.import_.ImportUserEventsRequest`):
                The request object. Request message for the
                ImportUserEvents request.
            parent (:class:`str`):
                Required.
                "projects/1234/locations/global/catalogs/default_catalog/eventStores/default_event_store".
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            request_id (:class:`str`):
                Optional. Unique identifier provided by client, within
                the ancestor dataset scope. Ensures idempotency for
                expensive long running operations. Server-generated if
                unspecified. Up to 128 characters long. This is returned
                as google.longrunning.Operation.name in the response.
                Note that this field must not be set if the desired
                input config is catalog_inline_source.
                This corresponds to the ``request_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            input_config (:class:`~.import_.InputConfig`):
                Required. The desired input location
                of the data.
                This corresponds to the ``input_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            errors_config (:class:`~.import_.ImportErrorsConfig`):
                Optional. The desired location of
                errors incurred during the Import.
                This corresponds to the ``errors_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.import_.ImportUserEventsResponse``: Response
                of the ImportUserEventsRequest. If the long running
                operation was successful, then this message is returned
                by the google.longrunning.Operations.response field if
                the operation was successful.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any(
            [parent, request_id, input_config, errors_config]
        ):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = import_.ImportUserEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if request_id is not None:
            request.request_id = request_id
        if input_config is not None:
            request.input_config = input_config
        if errors_config is not None:
            request.errors_config = errors_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.import_user_events,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            import_.ImportUserEventsResponse,
            metadata_type=import_.ImportMetadata,
        )

        # Done; return the response.
        return response


try:
    _client_info = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-recommendations-ai"
        ).version
    )
except pkg_resources.DistributionNotFound:
    _client_info = gapic_v1.client_info.ClientInfo()


__all__ = ("UserEventServiceClient",)
