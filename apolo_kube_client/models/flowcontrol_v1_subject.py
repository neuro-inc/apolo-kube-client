from pydantic import BaseModel, Field

from .v1_group_subject import V1GroupSubject
from .v1_service_account_subject import V1ServiceAccountSubject
from .v1_user_subject import V1UserSubject


class FlowcontrolV1Subject(BaseModel):
    group: V1GroupSubject | None = Field(None, alias="group")

    kind: str | None = Field(None, alias="kind")

    service_account: V1ServiceAccountSubject | None = Field(
        None, alias="serviceAccount"
    )

    user: V1UserSubject | None = Field(None, alias="user")
