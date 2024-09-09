import sys

import requests
import asyncio

from rich.console import Console
from rich.markdown import Markdown

console = Console()

async def main():
    loop = asyncio.get_event_loop()
    args = sys.argv[-1]
    resp = await loop.run_in_executor(None, requests.get, args)    
    console.print(Markdown(str(resp.content)))
    print("async request going on")


if __name__ == "__main__":
    asyncio.run(main())
