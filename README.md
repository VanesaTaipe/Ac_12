# Ac_12
python3 -m venv GBM-venv<BR>
source GBM-ven/bin/activate<BR>
pip install lightgbm<BR>
pip install scikit-learn<BR>

python3 -m pip install grpcio grpcio-tools

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. data_analysis.proto

python3 server.py

python3 client.py
