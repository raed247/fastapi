async def stream_quotes(symbols: list[str]):
    ib = await ib_insync_util.connect_async()
    contracts = [Stock(s) for s in symbols]
    for contract in contracts:
        ib.reqMktData(contract, snapshot=False)
    async for tick in ib.stream():
        yield TickData.from_ib(tick)
