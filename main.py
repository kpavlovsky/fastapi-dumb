from fastapi import FastAPI
import socket
from datetime import datetime

app = FastAPI()

@app.get("/")
async def get_server_hostname():
    hostname = socket.gethostname()
    return {"hostname": hostname, "current_time": datetime.now().isoformat()}
