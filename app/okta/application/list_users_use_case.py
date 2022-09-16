from returns.pipeline import flow
from returns.result import Result, Success
from returns.pointfree import bind, alt

from app.okta.infrastructure.okta_client import client
from app.okta.domain.user import create_user
from app.common.domain.error import create_error_dict


def list_users(query_params=None) -> Result[dict[str, any], dict[str, str]]:
    return flow(
        query_params,
        client.list_users,
        bind(_create_domain_users),
        alt(create_error_dict),
    )


def _create_domain_users(okta_user_list):
    return Success(list(map(lambda okta_user: create_user(okta_user), okta_user_list)))
