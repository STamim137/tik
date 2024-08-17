import requests
from ms4 import InfoTik
from random import randbytes
from binascii import hexlify
from TikTokAg import UserAgent
import time
import os
from uuid import uuid4
import random
from rich.console import Console
from rich.table import Table
from rich.text import Text

gg = 0
bb = 0

console = Console()

user = input("Enter The Target Username : ")


info = InfoTik.TikTok_Info(user)

try:
    nm = info['name']
except:
    nm = ""

try:
    target_id = info['id']
except:
    target_id = ""

try:
    folo = str(info['followers'])
except:
    folo = ""

try:
    following = str(info['following'])
except:
    following = ""

try:
    country = f"{info['country']} {info['flag']}"
except:
    country = ""

try:
    bio = info['bio']
except:
    bio = ""

try:
    user_id = str(info['id'])
except:
    user_id = ""

try:
    private = str(info['private'])
except:
    private = ""

try:
    date = str(info['Date'])
except:
    date = ""

try:
    likes = str(info['like'])
except:
    likes = ""


def Report():
    global gg, bb
    url = "https://api16-normal-c-alisg.ttapis.com/aweme/v2/aweme/feedback/"
    Mahos = UserAgent()
    agent = Mahos['User-Agent']
    brand = Mahos['brand']
    type = Mahos['type']
    tim = '{:.0f}'.format(time.time() * 1000)

    params = {
        'owner_id': target_id,
        'object_id': target_id,
        'report_type': "user",
        'enter_from': "others_homepage",
        'isFirst': "1",
        'no_hw': "1",
        'report_desc': "",
        'uri': "",
        'reason': "90084",
        'category': "porn",
        'request_tag_from': "h5",
        'iid': '73' + ''.join(random.choices('0123456789', k=16)),
        'device_id': '73' + ''.join(random.choices('0123456789', k=16)),
        'ac': "MOBILE_4G",
        'channel': "googleplay",
        'aid': "1233",
        'app_name': "musical_ly",
        'version_code': "310503",
        'version_name': "31.5.3",
        'device_platform': "android",
        'os': "android",
        'ab_version': "31.5.3",
        'ssmix': "a",
        'device_type': type,
        'device_brand': brand,
        'language': "ar",
        'os_api': "29",
        'os_version': "10",
        'openudid': hexlify(randbytes(8)).decode(),
        'manifest_version_code': "2023105030",
        'resolution': "720*1491",
        'dpi': "320",
        'update_version_code': "2023105030",
        '_rticket': tim,
        'is_pad': "0",
        'current_region': "YE",
        'app_type': "normal",
        'mcc_mnc': "42102",
        'timezone_name': "Asia/Aden",
        'carrier_region_v2': "421",
        'residence': "YE",
        'app_language': "ar",
        'carrier_region': "YE",
        'ac2': "lte",
        'uoo': "1",
        'op_region': "YE",
        'timezone_offset': "10800",
        'build_number': "31.5.3",
        'host_abi': "arm64-v8a",
        'locale': "ar",
        'ts': str(int(time.time())),
        'cdid': str(uuid4()),
    }

    headers = {
        'User-Agent': agent,
        'sdk-version': "2",
        'passport-sdk-version': "19",
        'x-tt-dm-status': "login=0;ct=0;rt=7",
        'x-vc-bdturing-sdk-version': "2.3.3.i18n",
        'x-tt-store-region': "ye",
        'x-tt-store-region-src': "did",
        'x-ss-dp': "1233",
        'x-khronos': str(int(time.time())),
    }

    res = requests.get(url, params=params, headers=headers)

    if '"status_code":0,"status_message":""' in res.text:
        os.system('clear')
        gg += 1
    else:
        os.system('clear')
        bb += 1


def display_report():
    total = gg + bb
    
    table = Table(title="TIKTOK REPORT")
    
    table.add_column("Type", justify="center", style="cyan", no_wrap=True)
    table.add_column("Count", justify="center", style="magenta")
    
    table.add_row("Good Report", Text(str(gg), style="green"))
    table.add_row("Bad Report", Text(str(bb), style="red"))
    table.add_row("Total", Text(str(total), style="yellow"))
    table.add_row("Dev", "AHMED ~~ @maho_s9")
    table.add_row("User", Text(user, style="cyan"))
    table.add_row("Name", Text(nm, style="cyan"))
    table.add_row("Followers", Text(folo, style="green"))
    table.add_row("Following", Text(following, style="yellow"))
    table.add_row("Country", Text(country, style="blue"))
    table.add_row("Bio", Text(bio, style="magenta"))
    table.add_row("ID", Text(user_id, style="cyan"))
    table.add_row("Private", Text(private, style="red" if private == "True" else "green"))
    table.add_row("Date", Text(date, style="magenta"))
    table.add_row("Likes", Text(likes, style="green"))
    
    console.print(table)


while True:
    try:
        Report()
        display_report()
    except Exception as e:
        console.print(f"Error reporting: {e}", style="bold red")
        pass
