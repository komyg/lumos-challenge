from returns.pipeline import flow
from returns.result import Result, Success
from returns.pointfree import alt, map_

from app.okta.infrastructure.okta_client import client
from app.common.domain.identifier import create_id_dict
from app.common.domain.error import create_error_dict


def delete_user(user_id) -> Result[dict[str, any], dict[str, str]]:
    return flow(
        user_id,
        client.delete_user,
        map_(create_id_dict),
        alt(create_error_dict),
    )
