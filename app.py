
import dbm
import contextlib
import time
import threading

from fastapi import FastAPI
import uvicorn

from config import *

app = FastAPI()

@app.get("/callback")
def callback(code: str) -> dict:
    # Storing the recieved code to in memory db
    with dbm.open('oauth', 'c') as db:
        db['code'] = code
    return {"code": code}


# Reference: https://github.com/encode/uvicorn/discussions/1103#discussioncomment-941736

class Server(uvicorn.Server):
    def install_signal_handlers(self):
        pass
    
    @contextlib.contextmanager
    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        try:
            while not self.started and thread.is_alive(): # Added a condition for checking if thread is alive 
                time.sleep(1e-3)
            yield
        finally:
            self.should_exit = True
            thread.join()
