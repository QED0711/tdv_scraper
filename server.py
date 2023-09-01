#!/usr/bin/python
import asyncio, websockets, ssl, json

async def handler(websocket, path):
    # on connection
    print("WebSocket connection opened")
    
    try:
        async for message in websocket:
            parsed = json.loads(message)
            if("symbol" in parsed and "chart" in parsed):
                print(parsed["symbol"], parsed["chart"][-1])
            # your code here
    
    finally:
        # on disconnection
        print("WebSocket connection closed")


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("/app/ssl/cert.pem", "/app/ssl/key.pem")

start_server = websockets.serve(handler, "0.0.0.0", 8000, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()