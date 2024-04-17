from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schema_retrieve_lang import SchemaRetrieveLang
from ...models.schema_retrieve_response_200 import SchemaRetrieveResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: Union[Unset, SchemaRetrieveLang] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_lang: Union[Unset, str] = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang.value

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/schema/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SchemaRetrieveResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SchemaRetrieveResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SchemaRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    lang: Union[Unset, SchemaRetrieveLang] = UNSET,
) -> Response[SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        lang (Union[Unset, SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchemaRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    lang: Union[Unset, SchemaRetrieveLang] = UNSET,
) -> Optional[SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        lang (Union[Unset, SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchemaRetrieveResponse200
    """

    return sync_detailed(
        client=client,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    lang: Union[Unset, SchemaRetrieveLang] = UNSET,
) -> Response[SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        lang (Union[Unset, SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchemaRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    lang: Union[Unset, SchemaRetrieveLang] = UNSET,
) -> Optional[SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        lang (Union[Unset, SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchemaRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
        )
    ).parsed
