# greeter/client.py
import grpc
from . import helloworld_pb2_grpc, helloworld_pb2


async def send_greeting(server_address="localhost:50051", name="world"):
    async with grpc.aio.insecure_channel(server_address) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(helloworld_pb2.HelloRequest(name=name))
        return response.message
