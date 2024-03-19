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
                file.write(f"add list=adblocker comment=AdGuardHome-ADblocker address={url}\n")


def generate_stalkerware_list() -> None:
    response = urlopen(
        'https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts').read()
    decoded_response = response.decode('utf-8')
    stalkerware_list = decoded_response.split("\n")
    with open("dist/stalkerware.rsc", "w") as file:
        file.write("# ============================================================\n")
        file.write("# Last Update     : " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
        file.write("/ip firewall address-list \n")
        for line in stalkerware_list:
            file.write(f"add list=stalkerware comment=AdGuardHome-Stalkerware address={line}\n")


async def main() -> None:
    generate_lists_folder()
    generate_ad_block_file()
    generate_stalkerware_list()


if __name__ == "__main__":
    asyncio.run(main())
