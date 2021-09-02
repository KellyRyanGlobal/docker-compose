import time
import redis
from flask import Flask

app = Flask(__name__)
msg_txt = " hello from python"
r = redis.Redis(host='redis', port=6379)
r.set("msg:hello", msg_txt)

def get_str():
    retries = 3
    while True:
        try:
            r.append("message:hello"," how are you")
            return r.get("msg:hello")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(1)

@app_route('/')
def hello():
    some_str = get.str()
    return "hello! I see {}".format(some_str)

