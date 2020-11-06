from colorama import Fore
import inquirer, os, subprocess, time
from subprocess import check_output

same_dir_choice = input("\nIs ip addr .txt file in same dir as this script? [yes (y) | no (n)]\n")

if (same_dir_choice == "yes" or same_dir_choice == "y"):
    filename = ""
    while (filename == ""):
        filename = input("\nName of file:\n")
        print(Fore.BLUE + f"\nEntered filename: {filename}" + Fore.RESET)
        if(filename == ""):
            print(Fore.MAGENTA + "\nFilename cannot be a blank string! \nPlease enter a filename...\n" + Fore.RESET)     
        try:
            with open(filename, "r") as f:
                ipv4s = [line.rstrip() for line in f]
            print(Fore.YELLOW + f"IP Addresses to Ping: {ipv4s}\n" + Fore.RESET) 
            for ip in ipv4s:
                bash_command = "ping " + ip
                #subprocess.call(bash_command, shell = True)
                p = subprocess.Popen(["ping", ip], stdout = subprocess.PIPE)
                time.sleep(1)
                p.kill()
                output, error = p.communicate()
                response = output.decode("utf-8")
                if("64" in response):
                    print(f"Ping Response: {response}")
                    print(Fore.GREEN + f"IPv4 Address: {ip} is alive!\n" + Fore.RESET)
                else:
                    print(Fore.RED + f"IPv4 Address: {ip} is dead!\n" + Fore.RESET)
        except IOError:
            print(Fore.MAGENTA + f"{filename} is not a valid .txt file" + Fore.RESET)