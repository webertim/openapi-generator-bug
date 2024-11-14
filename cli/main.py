from pydantic import SecretStr
from openapi_client.models import SecretData
from openapi_client import DefaultApi, ApiClient, Configuration

if __name__ == "__main__":
   client = DefaultApi(ApiClient(Configuration(host="http://localhost:8000")))
   client.root_get(secret_data=SecretData(
       secret=SecretStr("test")
   )) 