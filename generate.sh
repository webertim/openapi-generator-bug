docker run --rm \
    -v $PWD/api:/api -v $PWD/cli:/cli openapitools/openapi-generator-cli generate \
    -i /api/openapi.json \
    -g python-pydantic-v1 \
    -o /cli