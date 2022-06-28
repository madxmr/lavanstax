from rich.live_render import LiveRender
from rich.console import Console
from rich.panel import Panel
import os, shutil
import sys


console = Console()

def hata (text):
   console.print(Panel(f'[bold red]{text}[/]',width=70),justify="center")                         
def bilgi (text):
   console.print(Panel(f'[blue]{text}[/]',width=70),justify="center")                         
def basarili (text):
   console.print(Panel(f'[bold green] {text}[/]',width=70),justify="center")                         
def onemli (text):
   console.print(Panel(f'[bold cyan]{text}[/]',width=70),justify="center")                         
def soru (soru):
   console.print(Panel(f'[bold yellow]{soru}[/]',width=70),justify="center")                         
   return console.input(f"[bold yellow]>> [/]")
def logo (dil = "None"):
   surum = str(sys.version_info[0]) + "." + str(sys.version_info[1])
   console.print(Panel(f"[bold blue]Dikkat hiçbir bilginiz kayıt altına alınmamaktadır Lavanstax geliştiricileri bilgilerinizi göremez veya hesabınıza giriş yapamaz!"))
   console.print(Panel(f"[bold blue]Attention!, none of your information is recorded. Lavanstax developers cannot see your information or log into your account."))
   console.print(Panel(f"[bold blue]Lavanstax Installer ✨[/]\n\n[bold cyan]Version: [/][i]1.0[/]\n[bold cyan]Python: [/][i]{surum}[/]\n[bold cyan]Language: [/][i]{dil}[/]",width=80),justify="center")                         
def tamamlandi (saniye):
   console.print(Panel(f"[bold green]Kurulum Tamamlandı!\n[i]Botu {round(saniye)} saniye içinde Kurdunuz.[/]\n\n[bold green]Bir süre sonra herhangi bir sohbete .alive yazarak test edebilirsiniz. İyi günler dilerim :)[/]",width=70),justify="center")                     
                   
def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)


    
