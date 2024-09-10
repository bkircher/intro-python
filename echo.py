import sys

import requests
import asyncio

from rich.console import Console
from rich.markdown import Markdown

console = Console()


async def fetch_content_async(url):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, url)
    return response


def fetch_content_sync(url):
    response = requests.get(url)
    return response


async def main():
    if len(sys.argv) < 2:
        console.print("Error: URL is missing!")
        return

    url = sys.argv[-1]

    # sync request
    response_sync = fetch_content_sync(url)
    console.print(Markdown(response_sync.text))

    # async
    response_async = await fetch_content_async(url)
    console.print(Markdown(response_async.text))


if __name__ == "__main__":
    asyncio.run(main())