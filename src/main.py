import asyncio
import threading

from mros.csm import *


async def client():
    client_socket = ClientSocket()
    
        
    
    client_socket.establish()


async def server():
    server_socket = ServerSocket()
    
    await server_socket.establish()    


if __name__ == "__main__":
    threading.Thread(target=asyncio.run, args=(server(),)).start()
    asyncio.run(client())