# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_post**](DefaultApi.md#root_post) | **POST** / | Root


# **root_post**
> object root_post(secret_data)

Root

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.secret_data import SecretData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    secret_data = openapi_client.SecretData() # SecretData | 

    try:
        # Root
        api_response = api_instance.root_post(secret_data)
        print("The response of DefaultApi->root_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_data** | [**SecretData**](SecretData.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

