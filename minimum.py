from mattermostdriver import Driver
import websockets.client
import json
from asyncio import run

from secret import TOKEN
from config import URL, PORT

URI = f"wss://{URL}:{PORT}/api/v4/websocket"

AUTH_SEND = json.dumps({"seq": 1, "action": "authentication_challenge", "data": {"token": TOKEN}})


async def main():
    driver = Driver(
        {
            'url': URL,
            'basepath': '/api/v4',
            'verify': True,
            'scheme': 'https',
            'port': PORT,
            'auth': None,
            'token': TOKEN,
            'keepalive': True,
            'keepalive_delay': 5,
        }
    )

    driver.login()


    driver.client.post(
        '/posts',
        data=json.dumps({
            "channel_id": "717mezsoofdhbpc7pijgih9t4r",
            "message": "Hello",
        })

    )

    async with websockets.client.connect(URI) as ws:
        await ws.send(AUTH_SEND)

        for i in range(10):
            res = json.loads(await ws.recv())
            print(res)


run(main())
