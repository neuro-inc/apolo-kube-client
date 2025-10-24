from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1QueuingConfiguration",)


class V1QueuingConfiguration(BaseModel):
    """QueuingConfiguration holds the configuration parameters for queuing"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.QueuingConfiguration"
    )

    hand_size: Annotated[
        int | None,
        Field(
            alias="handSize",
            description="""`handSize` is a small positive number that configures the shuffle sharding of requests into queues.  When enqueuing a request at this priority level the request's flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here.  The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues).  See the user-facing documentation for more extensive guidance on setting this field.  This field has a default value of 8.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    queue_length_limit: Annotated[
        int | None,
        Field(
            alias="queueLengthLimit",
            description="""`queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected.  This value must be positive.  If not specified, it will be defaulted to 50.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    queues: Annotated[
        int | None,
        Field(
            description="""`queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive.  Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant.  This field has a default value of 64.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
