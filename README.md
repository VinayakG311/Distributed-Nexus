# DSCD_Assignment1


command to create proto-grpc files
```
python3 -m grpc_tools.protoc -I=./Proto --python_out=. --pyi_out=. --grpc_python_out=. ./Proto/market.proto
```