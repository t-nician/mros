from pydantic import Field


from mros.csm.base import (
    CommandType, ReplicationOwnership, ReplicationType, BaseSocket
)


class ClientSocket(BaseSocket):
    
    async def establish(self):
        pass