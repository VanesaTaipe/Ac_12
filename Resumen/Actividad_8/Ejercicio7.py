import aiohttp
import asyncio

async def fetch_page(session, url):
    async with session.get(url) as response:
        content = await response.text()
        filename = url.replace("https://", "").replace("/", "_") + ".html"
        with open(filename, 'w') as file:
            file.write(content)
        return filename

async def parallel_download(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        return await asyncio.gather(*tasks)

urls = ["https://google.com", "https://google.org", "https://google.net"]
results = asyncio.run(parallel_download(urls))
print(results)
