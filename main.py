from dictionary import killman
from dictionary import base_params
from dictionary import *
import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text
from ms4 import InfoTik
import os

gg = 0
bb = 0

console = Console()

user = input("Enter The Target Username again : ")

info = InfoTik.TikTok_Info(user)
try:
    nm = info['name']
except:
    nm = ""

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
    headers = killman()
    params = base_params()
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
