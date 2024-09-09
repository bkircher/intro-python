import sys

import requests

from rich.console import Console
from rich.markdown import Markdown

console = Console()

def main():
    args = sys.argv[-1]
    resp = requests.get(args)
    console.print(Markdown(resp.text))


if __name__ == "__main__":
    main()
