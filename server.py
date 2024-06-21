from concurrent import futures
import grpc
import data_analysis_pb2
import data_analysis_pb2_grpc
import math
import zlib

class DataAnalysisService(data_analysis_pb2_grpc.DataAnalysisServiceServicer):
    def Aggregate(self, request, context):
        data = request.data
        operation = request.operation
        
        if operation == "sum":
            result = sum(data)
        elif operation == "avg":
            result = sum(data) / len(data) if data else 0
        elif operation == "max":
            result = max(data) if data else 0
        elif operation == "min":
            result = min(data) if data else 0
        else:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, f"Unknown operation: {operation}")
        
        return data_analysis_pb2.AggregateResponse(result=result)

    def Filter(self, request, context):
        data = request.data
        condition = request.condition
        value = request.value
        
        if condition == "greater_than":
            filtered_data = [x for x in data if x > value]
        elif condition == "less_than":
            filtered_data = [x for x in data if x < value]
        elif condition == "equal_to":
            filtered_data = [x for x in data if x == value]
        else:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, f"Unknown condition: {condition}")
        
        return data_analysis_pb2.FilterResponse(filtered_data=filtered_data)

    def Transform(self, request, context):
        data = request.data
        operation = request.operation
        
        if operation == "square":
            transformed_data = [x**2 for x in data]
        elif operation == "sqrt":
            transformed_data = [math.sqrt(x) for x in data if x >= 0]
        elif operation == "log":
            transformed_data = [math.log(x) for x in data if x > 0]
        else:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, f"Unknown operation: {operation}")
        
        return data_analysis_pb2.TransformResponse(transformed_data=transformed_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_analysis_pb2_grpc.add_DataAnalysisServiceServicer_to_server(DataAnalysisService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
