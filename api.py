from fastapi import FastAPI





app = FastAPI()


#simulate the endpoint for the robot so I don't have to go to the office lol
@app.post("/mock_tour")
async def send_message():
    return {"Robot": "Dance"}



