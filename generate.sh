rm -rf ./cli
docker run --rm \
    -v $PWD/:/in -v $PWD/cli:/cli openapitools/openapi-generator-cli generate \
    -i /in/openapi.json \
    -g python-pydantic-v1 \
    -o /cli