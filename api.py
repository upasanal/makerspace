from fastapi import FastAPI
import time




app = FastAPI()


#simulate the endpoint for the robot so I don't have to go to the office lol
@app.post("/mock_tour")
def send_message():
    yield "Robot"

    for x in range(10): 
        print(f"{x*5} seconds went by")
        time.sleep(5)    




