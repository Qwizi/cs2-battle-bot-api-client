from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_guild_member import CreateGuildMember
from ...models.guild import Guild
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union[
        CreateGuildMember,
        CreateGuildMember,
        CreateGuildMember,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/guilds/{id}/add_member/",
    }

    if isinstance(body, CreateGuildMember):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateGuildMember):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CreateGuildMember):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Guild]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Guild.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Guild]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGuildMember,
        CreateGuildMember,
        CreateGuildMember,
    ],
) -> Response[Guild]:
    """
    Args:
        id (str):
        body (CreateGuildMember):
        body (CreateGuildMember):
        body (CreateGuildMember):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Guild]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGuildMember,
        CreateGuildMember,
        CreateGuildMember,
    ],
) -> Optional[Guild]:
    """
    Args:
        id (str):
        body (CreateGuildMember):
        body (CreateGuildMember):
        body (CreateGuildMember):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Guild
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGuildMember,
        CreateGuildMember,
        CreateGuildMember,
    ],
) -> Response[Guild]:
    """
    Args:
        id (str):
        body (CreateGuildMember):
        body (CreateGuildMember):
        body (CreateGuildMember):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Guild]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGuildMember,
        CreateGuildMember,
        CreateGuildMember,
    ],
) -> Optional[Guild]:
    """
    Args:
        id (str):
        body (CreateGuildMember):
        body (CreateGuildMember):
        body (CreateGuildMember):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Guild
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
