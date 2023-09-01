// ============================== WEBSOCKET ==============================
class Socket {
    constructor({ url, reconnectInterval = 3000, heartbeat = 0 }) {
        this.url = url;
        this.ws = null;
        this.reconnectInterval = reconnectInterval;
        this.heartbeat = heartbeat;
        this.connect();
    }

    connect() {
        this.ws = new WebSocket(this.url);

        this.ws.onopen = () => {
            console.log("Socket Opened");
            if (this.heartbeat > 0) {
                this.heartbeatInterval = setInterval(() => {
                    this.send({ heartbeat: Date.now() });
                }, this.heartbeat);
            }
        };

        this.ws.onclose = () => {
            console.warn("Socket connection lost. Reconnecting...");
            clearInterval(this.heartbeatInterval);
            setTimeout(this.connect.bind(this), this.reconnectInterval);
        };

        this.ws.onerror = (err) => {
            console.error("WebSocket Error:", err);
        };
    }

    send(msg) {
        if (msg === null || msg === undefined) return;

        if (typeof msg === "string") {
            this.ws.send(msg);
        } else if (typeof msg === "object") {
            this.ws.send(JSON.stringify(msg));
        }
    }
}

const SOCKET = new Socket({ url: `wss://localhost:8000`, heartbeat: 10_000, reconnectInterval: 3000 });

// ============================== LISTENER ==============================
function listenToSocket(handler) {
    handler = handler || console.log;
    let property = Object.getOwnPropertyDescriptor(MessageEvent.prototype, "data");

    const data = property.get;

    property.get = function () {
        // to replace get function
        let socket = this.currentTarget instanceof WebSocket;

        if (!socket) {
            return data.call(this);
        }

        let msg = data.call(this);

        Object.defineProperty(this, "data", { value: msg }); //anti-loop
        handler({ data: msg, socket: this.currentTarget, event: this });
        return msg;
    };

    Object.defineProperty(MessageEvent.prototype, "data", property);
}

// ============================== HANDLER ==============================

listenToSocket(({ data }) => {
    try {
        const isSeriesLoading = data.match(/series_loading/i);
        if (isSeriesLoading) {
            const chartDataRaw = data.match(/\[\d{10}\.\d,(\d+\.\d+,?){5}\]/g);
            const symbolName = data.match(/"name":"\w+"/i)?.[0];
            if (chartDataRaw?.length > 200) {
                const parsed = chartDataRaw.map((dataPoint) => JSON.parse(dataPoint));
                let symbol = symbolName?.split?.(":")?.[1]?.slice?.(1, -1);
                symbol ??= document
                    .querySelector("[data-symbol-short][data-active=true]")
                    ?.querySelector("[class*=symbolNameText]")?.innerText;

                SOCKET.send({ symbol, chart: parsed });
            }
        }
    } catch (err) {
        console.error(err);
    }
});
