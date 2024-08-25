from pydantic import Field


from mros.csm.base import (
    CommandType, ReplicationOwnership, ReplicationType, BaseSocket
)


class ServerSocket(BaseSocket):
    
    async def establish(self):
        pass