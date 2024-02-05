# README

## Running

```bash
# Build Proto
python -m grpc_tools.protoc -I./protos --python_out=./greeter --grpc_python_out=./greeter ./protos/helloworld.proto

# Update `greeter/helloworld_pb2_grpc.py` to update `import helloworld_pb2 as helloworld__pb2` to `import greeter.helloworld_pb2 as helloworld__pb2`
sed -i 's/import helloworld_pb2 as helloworld__pb2/import greeter.helloworld_pb2 as helloworld__pb2/g' greeter/helloworld_pb2_grpc.py

# Cythonize
python setup.py build_ext --inplace

# Run the Server
python main_server.py

# Run the Client
python main_client.py
```

## Stacktrace

The above will return:

```python
Traceback (most recent call last):
  File "main_client.py", line 12, in <module>
    asyncio.run(main())
  File "/home/xanrin/.pyenv/versions/3.8.18/lib/python3.8/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/home/xanrin/.pyenv/versions/3.8.18/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "main_client.py", line 7, in main
    greeting = await send_greeting(name="Alice")
  File "greeter/client.py", line 7, in send_greeting
    async with grpc.aio.insecure_channel(server_address) as channel:
  File "greeter/client.py", line 9, in greeter.client.send_greeting
    response = await stub.SayHello(helloworld_pb2.HelloRequest(name=name))
  File "/home/xanrin/.pyenv/versions/3.8.18/lib/python3.8/site-packages/grpc/aio/_call.py", line 318, in __await__
    raise _create_rpc_error(
grpc.aio._call.AioRpcError: <AioRpcError of RPC that terminated with:
        status = StatusCode.UNKNOWN
        details = "Unexpected <class 'TypeError'>: descriptor 'SerializeToString' for 'google._upb._message.Message' objects doesn't apply to a '_cython_3_0_2.coroutine' object"
        debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"Unexpected <class \'TypeError\'>: descriptor \'SerializeToString\' for \'google._upb._message.Message\' objects doesn\'t apply to a \'_cython_3_0_2.coroutine\' object", grpc_status:2, created_time:"2024-02-05T14:50:26.432929772+01:00"}"
```
