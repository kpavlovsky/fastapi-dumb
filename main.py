from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
async def get_server_hostname():
    hostname = socket.gethostname()
    return {"hostname": hostname}


