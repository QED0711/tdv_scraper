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
        const chartDataRaw = data.match(/\[\d{10}\.\d,(\d+\.\d+,?){5}\]/g);
        const symbolName = data.match(/"name":"\w+"/i)?.[0]
        if (chartDataRaw.length > 200) {
            symbol = symbolName.split(":")[1]?.slice(1,-1)
            const parsed = chartDataRaw.map(dataPoint => JSON.parse(dataPoint))

            window._activeChart = {symbol, chart: parsed};
        }
    } catch (err) {}
});
