from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# ---- Simple placeholder until you paste your real trade code ----
class TradeRequest(BaseModel):
    cash: float

@app.post("/trade")
def trade(req: TradeRequest):
    # Hard-coded idea just to prove the pipe works
    return {
        "strategy": "Bull Call Debit Spread",
        "underlying": "AMD",
        "cost": req.cash * 0.96,
        "maxProfit": req.cash * 1.5,
        "expectedROI": 56,
        "thesis": "Demo response",
        "legs": [
            {"side": "BUY",  "symbol": "AMD 160 C", "contracts": 1, "price": 2.40},
            {"side": "SELL", "symbol": "AMD 170 C", "contracts": 1, "price": 1.44}
        ]
    }
