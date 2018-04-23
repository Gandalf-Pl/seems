import asyncio
import aiohttp

import uvloop

import time


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print (resp.status)
            print("get {} response complete".format(url))

#async def wait_download(url):
#
#    await download(url)
#
#    print("get {} data complete.".format(url))


async def main():

    start = time.time()


    await asyncio.wait([
        download("http://www.163.com"),
        download("http://www.baidu.com"),
        download("http://www.bing.com"),
    ])

    end = time.time()
    print("Complete in {} seconds".format(end - start))


if __name__ == "__main__":

    loop =  uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

