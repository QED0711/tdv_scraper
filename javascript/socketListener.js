// ============================== WEBSOCKET ==============================
const socket = new WebSocket(`wss://localhost:8000`);
socket.onopen = () => {
    setInterval(() => {
        socket.send(JSON.stringify({ heartbeat: Date.now() }));
    }, 3000);
};

socket.onclose = () => {
    console.log("SOCKET CLOSED!!!");
};

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

listenToSocket(({ data }) => {
    try {
        const isSeriesLoading = data.match(/series_loading/i);
        if (isSeriesLoading) {
            const chartDataRaw = data.match(/\[\d{10}\.\d,(\d+\.\d+,?){5}\]/g);
            const symbolName = data.match(/"name":"\w+"/i)?.[0];
            if (chartDataRaw?.length > 200) {
                const parsed = chartDataRaw.map((dataPoint) => JSON.parse(dataPoint));
                let symbol = symbolName?.split?.(":")?.[1]?.slice?.(1, -1);
                symbol ??= document.querySelector("[data-symbol-short][data-active=true]").querySelector("[class*=symbolNameText]").innerText; 
                /* TODO: when symbol is null, determine symbol by finding the current active clicked watchlist element */
                
                // window._activeChart = { symbol, chart: parsed };
                socket.send(JSON.stringify({ symbol, chart: parsed }));
            }
        }
    } catch (err) {
        console.error(err);
    }
});
