from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_match_map_selected_list import PaginatedMatchMapSelectedList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    page: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/matches/{id}/picks/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedMatchMapSelectedList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedMatchMapSelectedList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedMatchMapSelectedList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
) -> Response[PaginatedMatchMapSelectedList]:
    """
    Args:
        id (int):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMatchMapSelectedList]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
) -> Optional[PaginatedMatchMapSelectedList]:
    """
    Args:
        id (int):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMatchMapSelectedList
    """

    return sync_detailed(
        id=id,
        client=client,
        page=page,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
) -> Response[PaginatedMatchMapSelectedList]:
    """
    Args:
        id (int):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMatchMapSelectedList]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
) -> Optional[PaginatedMatchMapSelectedList]:
    """
    Args:
        id (int):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMatchMapSelectedList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page=page,
        )
    ).parsed
