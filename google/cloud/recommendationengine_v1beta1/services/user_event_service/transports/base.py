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

import abc
import typing

from google import auth
from google.api_core import exceptions  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials  # type: ignore

from google.api import httpbody_pb2 as httpbody  # type: ignore
from google.cloud.recommendationengine_v1beta1.types import import_
from google.cloud.recommendationengine_v1beta1.types import user_event as gcr_user_event
from google.cloud.recommendationengine_v1beta1.types import user_event_service
from google.longrunning import operations_pb2 as operations  # type: ignore


class UserEventServiceTransport(abc.ABC):
    """Abstract transport class for UserEventService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        *,
        host: str = "recommendationengine.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=scopes
            )
        elif credentials is None:
            credentials, _ = auth.default(scopes=scopes)

        # Save the credentials.
        self._credentials = credentials

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def write_user_event(
        self,
    ) -> typing.Callable[
        [user_event_service.WriteUserEventRequest],
        typing.Union[
            gcr_user_event.UserEvent, typing.Awaitable[gcr_user_event.UserEvent]
        ],
    ]:
        raise NotImplementedError()

    @property
    def collect_user_event(
        self,
    ) -> typing.Callable[
        [user_event_service.CollectUserEventRequest],
        typing.Union[httpbody.HttpBody, typing.Awaitable[httpbody.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def list_user_events(
        self,
    ) -> typing.Callable[
        [user_event_service.ListUserEventsRequest],
        typing.Union[
            user_event_service.ListUserEventsResponse,
            typing.Awaitable[user_event_service.ListUserEventsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def purge_user_events(
        self,
    ) -> typing.Callable[
        [user_event_service.PurgeUserEventsRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def import_user_events(
        self,
    ) -> typing.Callable[
        [import_.ImportUserEventsRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()


__all__ = ("UserEventServiceTransport",)
