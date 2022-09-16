from returns.pipeline import flow
from returns.result import Result, Success
from returns.pointfree import bind, alt, map_

from app.okta.infrastructure.okta_client import client
from app.common.domain.identifier import create_id_dict
from app.common.domain.error import create_error_dict


def suspend_user(user_id) -> Result[dict[str, any], dict[str, str]]:
    return flow(
        user_id,
        client.suspend_user,
        map_(create_id_dict),
        alt(create_error_dict),
    )


def unsuspend_user(user_id) -> Result[dict[str, any], dict[str, str]]:
    return flow(
        user_id,
        client.unsuspend_user,
        map_(create_id_dict),
        alt(create_error_dict),
    )
