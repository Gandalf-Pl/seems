import requests

import time


def download(url):

    response = requests.get(url)

    print("get {} response complete".format(url))


def main():

    start = time.time()

    download("http://www.163.com")

    download("http://www.baidu.com")

    download("http://www.bing.com")

    end = time.time()

    print("Complete in {} seconds".format(end - start))


if __name__ == "__main__":
    main()

