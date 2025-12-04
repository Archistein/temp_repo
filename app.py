from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post('/api/v1/calc')
async def calc(a: float, op: str, b: float):
    try:
        match op:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return a / b
            case _:
                raise HTTPException(
                    status_code=419,
                    detail=f'Error: unknown operator `{op}`'
                )
    except ZeroDivisionError:
        raise HTTPException(
            status_code=420,
            detail=f'Error: division by zero`'
        )