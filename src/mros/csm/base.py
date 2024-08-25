from enum import Enum

from typing import Callable, Awaitable, Any

from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

from pydantic import BaseModel, ConfigDict, Field


class CommandType(Enum):
    CREATE_MODEL = "create_model"
    UPDATE_MODEL = "update_model"
    DELETE_MODEL = "delete_model"
    
    
class ReplicationType(Enum):
    CLIENT = "client_replication"
    SERVER = "server_replication"


class ReplicationOwnership(Enum):
    UNKNOWN = "unknown_environment"
    
    SERVER = "server_environment"
    CLIENT = "client_environment"
    
    SHARED = "shared_environment"
    
    
class ReplicationContainer(BaseModel):
    transformer: Callable[[Any], Awaitable[Any]] | None = Field(default=None)
    data: Any = Field(default=None) 


class ReplicationWorkspace(BaseModel):
    replication_data: dict[str, ReplicationContainer] = Field(
        default_factory=dict
    )


class BaseSocket(BaseModel):
    replication_ownership: ReplicationOwnership = Field(
        default=ReplicationOwnership.UNKNOWN
    )
    
    replication_address: tuple[str, int] = Field(
        default_factory=lambda: ("127.0.0.1", 5000)
    )

    replication_workspace: ReplicationWorkspace = Field(
        default_factory=ReplicationWorkspace
    )
    
    socket: Socket = Field(default_factory=lambda: Socket(AF_INET, SOCK_STREAM))
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)