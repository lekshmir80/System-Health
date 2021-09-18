#Menu driven System Health tool:
import os
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt

os.system('banner System Health')
console = Console()

def yprint(string):
	console.print(Text(string,style="bold yellow"))

def rprint(string): 
	console.print(Text(string,style="bold red"))
	
def gprint(string): 
	console.print(Text(string,style="bold green"))
	
def available_ram():
	lines = os.popen('free -m | wc -l').read()
	#Total 3 lines => first cut 1st line then cut last line
	free_mem = os.popen('free -m | tr -s " " | tail -n -2 | head -n 1').read()
	print(free_mem)
	free_mem = free_mem.split(' ')[6]
	yprint(f"\nFree/Available Memory => {free_mem}")
		
def load_avg():
	load_avg = os.popen("cat /proc/loadavg").read()
	yprint(f"\nLoad Average => {load_avg}")
	
def hostname_details():
	cmd = os.popen("hostnamectl status").read()
	yprint(cmd)

def process_count():
	all_process = os.popen("ps -e | wc -l").read()
	yprint(f"All Process Count => {all_process}\n")
	
def uptime():
	cmd = os.popen("uptime").read()
	yprint(f'Uptime => {cmd}')
	
def menu():
	gprint("1. Display available RAM")
	gprint("2. Display Load avearge")
	gprint("3. Display Hostname details")
	gprint("4. Display All process count")
	gprint("5. Display uptime")
	rprint("6.Exit")
	
if __name__ == "__main__":	
	while True:
		menu()
		ch = Prompt.ask("Enter your option:	", choices=["1", "2", "3","4","5","6"])
		if ch == "1":
			available_ram()
		elif ch == "2":
			load_avg()
		elif ch == "3":
			hostname_details()
		elif ch == "4":
			process_count()
		elif ch == "5":
			uptime()
		elif ch == "6":
			break;

		
