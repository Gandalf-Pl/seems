import asyncio
import requests

import time


async def download(url):

    response = requests.get(url)
    print("get {} response complete".format(url))


async def wait_download(url):

    await download(url)

    print("get {} data complete.".format(url))


async def main():

    start = time.time()


    await asyncio.wait([
        wait_download("http://www.163.com"),
        wait_download("http://www.baidu.com"),
        wait_download("http://www.bing.com"),
    ])

    end = time.time()
    print("Complete in {} seconds".format(end - start))


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

