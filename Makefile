
gen:
	python -m grpc_tools.protoc -I proto --python_out=pb --grpc_python_out=pb proto/*.proto
clean:
	rm pb/*.py
server:
	python main.py