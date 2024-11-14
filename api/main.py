import json
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, SecretStr

app = FastAPI()

class SecretData(BaseModel):
    secret: SecretStr

@app.get("/")
async def root(
    secret_data: SecretData,
) -> None:
    print(secret_data)

if __name__ == "__main__":
    openapi = get_openapi(title="My API", version="1.0.0", summary="Minimal Bug example", routes=app.routes)
    with open("openapi.json", "w") as f:
        f.write(json.dumps(openapi, indent=2))