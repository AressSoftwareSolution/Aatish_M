import asyncio  #runs asynchronous programs
import aiohttp   #async library to make HTTP requests

# function to fetch a single web page
async def fetch_page(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"Fetched {url} (length: {len(content)})")

# main function to run multiple fetches together
async def main():
    urls = [
        "https://github.com",
        "https://python.org",
        "https://www.hackerrank.com"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []

        for url in urls:
            tasks.append(fetch_page(session, url))

        await asyncio.gather(*tasks)

# start async program
asyncio.run(main())
