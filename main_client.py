# Example for using the greeter client library
from greeter.client import send_greeting
import asyncio


async def main():
    greeting = await send_greeting(name="Alice")
    print(greeting)


if __name__ == "__main__":
    asyncio.run(main())
