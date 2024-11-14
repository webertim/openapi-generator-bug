fastapi run api/main.py &
pip uninstall openapi_client -Y
pip install ./cli_fixed
python main.py