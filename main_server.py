# Example for using the greeter client library
from greeter.server import serve
import asyncio


async def main():
    await serve()


if __name__ == "__main__":
    asyncio.run(main())
