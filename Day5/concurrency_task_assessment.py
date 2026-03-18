import asyncio
import time

async def work(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")

async def main():
    start = time.time()

    await asyncio.gather(
        work("Task 1", 2),
        work("Task 2", 2),
        work("Task 3", 2)
    )

    end = time.time()
    print("Total time:", end - start)

asyncio.run(main())
