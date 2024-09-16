import requests
import time

api_key = "<your api key>"

browse_url = "https://api.twin.so/browse"
task_url = "https://api.twin.so/task/"


response = requests.post(
    url=browse_url,
    headers={"x-api-key": api_key},
    json={
        "goal": "Find electric scooter suppliers and return an analysis of the average price",
        "startUrl": "https://www.alibaba.com/",
        "outputType": "string",
    },
)

data = response.json()
print(data)
task_id = data["taskId"]
status = data["status"]
last_step = None

while status not in ["COMPLETED", "FAILED"]:
    time.sleep(1)
    response = requests.get(
        url=task_url + task_id + "?limit=1",
        headers={"x-api-key": api_key},
    )
    data = response.json()
    status = data["status"]
    steps = data["steps"]
    if len(steps) > 0 and last_step != response.json()["steps"][0]:
        last_step = response.json()["steps"][0]
        action = last_step["action"]
        if action is not None:
            print(action)
