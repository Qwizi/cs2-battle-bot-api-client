from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_server_list import PaginatedServerList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    guild: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["guild"] = guild

    params["is_public"] = is_public

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/servers/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedServerList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedServerList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedServerList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    guild: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Response[PaginatedServerList]:
    """
    Args:
        guild (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedServerList]
    """

    kwargs = _get_kwargs(
        guild=guild,
        is_public=is_public,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    guild: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Optional[PaginatedServerList]:
    """
    Args:
        guild (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedServerList
    """

    return sync_detailed(
        client=client,
        guild=guild,
        is_public=is_public,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    guild: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Response[PaginatedServerList]:
    """
    Args:
        guild (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedServerList]
    """

    kwargs = _get_kwargs(
        guild=guild,
        is_public=is_public,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    guild: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Optional[PaginatedServerList]:
    """
    Args:
        guild (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedServerList
    """

    return (
        await asyncio_detailed(
            client=client,
            guild=guild,
            is_public=is_public,
            page=page,
        )
    ).parsed
