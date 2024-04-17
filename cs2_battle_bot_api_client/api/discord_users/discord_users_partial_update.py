from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.discord_user import DiscordUser
from ...models.patched_discord_user import PatchedDiscordUser
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union[
        PatchedDiscordUser,
        PatchedDiscordUser,
        PatchedDiscordUser,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/discord-users/{id}/",
    }

    if isinstance(body, PatchedDiscordUser):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedDiscordUser):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedDiscordUser):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DiscordUser]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DiscordUser.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DiscordUser]:
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
        PatchedDiscordUser,
        PatchedDiscordUser,
        PatchedDiscordUser,
    ],
) -> Response[DiscordUser]:
    """
    Args:
        id (str):
        body (PatchedDiscordUser):
        body (PatchedDiscordUser):
        body (PatchedDiscordUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiscordUser]
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
        PatchedDiscordUser,
        PatchedDiscordUser,
        PatchedDiscordUser,
    ],
) -> Optional[DiscordUser]:
    """
    Args:
        id (str):
        body (PatchedDiscordUser):
        body (PatchedDiscordUser):
        body (PatchedDiscordUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiscordUser
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
        PatchedDiscordUser,
        PatchedDiscordUser,
        PatchedDiscordUser,
    ],
) -> Response[DiscordUser]:
    """
    Args:
        id (str):
        body (PatchedDiscordUser):
        body (PatchedDiscordUser):
        body (PatchedDiscordUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiscordUser]
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
        PatchedDiscordUser,
        PatchedDiscordUser,
        PatchedDiscordUser,
    ],
) -> Optional[DiscordUser]:
    """
    Args:
        id (str):
        body (PatchedDiscordUser):
        body (PatchedDiscordUser):
        body (PatchedDiscordUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiscordUser
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
