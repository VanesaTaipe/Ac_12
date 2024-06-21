import grpc
import data_analysis_pb2
import data_analysis_pb2_grpc
import zlib

def compress_data(data):
    return zlib.compress(str(data).encode())

def decompress_data(compressed_data):
    return eval(zlib.decompress(compressed_data).decode())

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = data_analysis_pb2_grpc.DataAnalysisServiceStub(channel)
    
    # Test Aggregate
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    compressed_data = compress_data(data)
    request = data_analysis_pb2.AggregateRequest(data=data, operation="avg")
    try:
        response = stub.Aggregate(request)
        print(f"Aggregate result: {response.result}")
    except grpc.RpcError as e:
        print(f"RPC failed: {e.code()} - {e.details()}")
    
    # Test Filter
    request = data_analysis_pb2.FilterRequest(data=data, condition="greater_than", value=3.0)
    try:
        response = stub.Filter(request)
        print(f"Filtered data: {response.filtered_data}")
    except grpc.RpcError as e:
        print(f"RPC failed: {e.code()} - {e.details()}")
    
    # Test Transform
    request = data_analysis_pb2.TransformRequest(data=data, operation="square")
    try:
        response = stub.Transform(request)
        print(f"Transformed data: {response.transformed_data}")
    except grpc.RpcError as e:
        print(f"RPC failed: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()
