import asyncio, websockets, ssl

async def handler(websocket, path):
    async for message in websocket:
        print(message)


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("ssl/cert.pem", "ssl/key.pem")
# TODO: do this without password protexted .pem files

start_server = websockets.serve(handler, "0.0.0.0", 8000, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()