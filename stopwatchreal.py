import time
from colorama import *
init()
print(Back.LIGHTWHITE_EX,"!!!!Welcome!!!",Back.RESET)
print(Back.GREEN,"###","###","###","###"+"#",Back.RESET)
print(Back.GREEN,"###","STOPWATCH","##",Back.RESET)
print(Back.GREEN,"###","###","###","###"+"#",Back.RESET)                    

start_sw=input(Fore.CYAN+"pres start to record: "+Fore.RESET)
now_time=time.time()
stopwatch=input(Fore.LIGHTGREEN_EX+"pres stop: "+Fore.RESET)

another_time=time.time()
check_thetimepassed=another_time-now_time

if stopwatch=="stop":
    print(Fore.RED+"the time elapsed is",round(check_thetimepassed,2),"scs")
    

         