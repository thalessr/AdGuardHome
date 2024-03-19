import asyncio
import os
from time import gmtime, strftime
from urllib.request import urlopen


def generate_lists_folder() -> None:
    if not os.path.isdir("dist"):
        os.mkdir("dist")


def generate_ad_block_file() -> None:
    response = urlopen('https://badmojr.gitlab.io/1hosts/Lite/adblock.txt').read()
    decoded_response = response.decode('utf-8')
    adblockers = decoded_response.split("\n")
    with open("dist/adblock.rsc", "w") as file:
        file.write("# ============================================================\n")
        file.write("# Last Update     : " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
        file.write("/ip firewall address-list \n")
        for line in adblockers:
            if (line.startswith('||')):
                url = line.replace('||', "")
                url = url.replace('^', "")
                file.write(f"add list=adblocker comment=AdGuardHome address={url}\n")


async def main() -> None:
    generate_lists_folder()
    generate_ad_block_file()


if __name__ == "__main__":
    asyncio.run(main())
