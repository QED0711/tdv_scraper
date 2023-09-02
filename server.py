#!/usr/bin/python
import os, asyncio, websockets, ssl, json, datetime
import pandas as pd

from environment import DATA_OUTPUT_DIR, BASE_PATH

os.makedirs(BASE_PATH, exist_ok=True)

async def handler(websocket, path):
    # on connection
    print("WebSocket connection opened")
    
    try:
        async for message in websocket:
            parsed = json.loads(message)
            if("symbol" in parsed and "chart" in parsed):
                sym = parsed["symbol"]
                df = pd.DataFrame(parsed["chart"], columns=("time", "open", "high", "low", "close", "volume"))
                df.time = pd.to_datetime(df.time, unit="s", utc=True).dt.tz_convert("America/New_York").dt.tz_localize(None)
                out_path = os.path.join(BASE_PATH, f"{sym}.csv")
                df.to_csv(out_path, index=False)
                print(f"{str(datetime.datetime.now().replace(microsecond=0))}: Received {sym}")
                # TODO: save a record of when each symbol was updated in the chart date
                # TODO: append data from each message so we can maintain longer periods?
            if("heartbeat" in parsed):
                pass
                # print("hb: ", parsed["heartbeat"])
    except Exception as e:
        print(e)
    finally:
        # on disconnection
        print("WebSocket connection closed")


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("/app/ssl/cert.pem", "/app/ssl/key.pem")

start_server = websockets.serve(handler, "0.0.0.0", 8000, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()