from fastapi import FastAPI, HTTPException
from typing import Literal

app = FastAPI()

@app.get("/calc/")
def calculator(op: Literal["+", "-"], a: float, b: float):
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    else:
        raise HTTPException(status_code=400, detail="Unsupported operation")
    return {"operation": op, "a": a, "b": b, "result": result}
