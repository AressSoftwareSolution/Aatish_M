import asyncio

async def task():
    print("Task started")
    await asyncio.sleep(2)
    print("Task finished")

asyncio.run(task())   #is used to start and run an async function.
