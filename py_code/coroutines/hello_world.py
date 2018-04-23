import asyncio

async def hello_world():
    print("hello world")


loop = asyncio.get_event_loop()


loop.run_until_complte(hello_world())

loop.close()
