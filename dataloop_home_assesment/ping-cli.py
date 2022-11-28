from asyncio import sleep
import os
from turtle import Terminator
from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
import sys
import uvicorn

class Item(BaseModel):
    name: str # pong string

app = FastAPI()

port_one, port_two = 3000, 5000
game_mode = sys.argv[1]
time_ms = sys.argv[2]

if game_mode == 'start':
    pass
elif game_mode == 'Pause':
    pass # os.system("pause")
elif game_mode == 'Resume':
    pass
elif game_mode == 'Stop':
    pass # terminate()




@app.get(f"/<pong_time_ms>/")
async def ping_pong(pong_time_ms, port = port_one):
    if pong_time_ms == 0:
        pass
    else:
        sleep(pong_time_ms)
        return ping_pong(pong_time_ms, port = port_two)

    
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port_one, reload=True)
    uvicorn.run(app, host="0.0.0.0", port=port_two, reload=True)
    

