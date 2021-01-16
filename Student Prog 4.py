
#-----------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime                                                                         #time is imported from your computer's local time
now_time = datetime.now()
live_time_by_your_pc = now_time.strftime("%H:%M:%S")
print("✦ _________________________________________________________________ ✦")
print("")     
print("    Welcome to the Student Progression Program - Alternative Staff Version                ")  #welcome message
print("")                                                                                            #I learnt the code for importing time from https://docs.python.org/3/library/time.html website.
print("                    Time is : ", live_time_by_your_pc)                                        #and i used it by changing variables 
print("✦ _________________________________________________________________ ✦")
#--------------------------------------------------------------------------------------------------------------------------------------
print("")
print("                        -User Instructions-                           ")                      #User Instructions
print("01. No inputs needed.")
print("___________________________________________________________________")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

l_for_display=["Pass=120  Defer=00  Fail=00 " , "Pass=100   Defer=20  Fail=0  ","Pass=100    Defer=0    Fail=20  ","Pass =80  Defer= 20  Fail =20 " , "Pass=60  Defer=40  Fail=20  ","Pass=40  Defer=40  Fail=40","Pass=20   Defer=40    Fail=60  ","Pass=20   Defer=20  Fail=80 ", "Pass=20  Defer=00  Fail=100","Pass=00  Defer=00  Fail=120"]
tup_display=('Progress' , 'Progress – module trailer' , 'Do not Progress – module retriever' , 'Exclude') 
#                  0                   1                             2                             3    

print("\n")
print(l_for_display[0]) #1
print(tup_display[0])
print("----------------------------")
print("\n")

print(l_for_display[1]) #2
print(tup_display[1])
print("----------------------------")
print("\n")

print(l_for_display[2]) #3
print(tup_display[1])
print("----------------------------")
print("\n")

print(l_for_display[3]) #4
print(tup_display[2])
print("----------------------------")
print("\n")

print(l_for_display[4]) #5
print(tup_display[2])
print("----------------------------")
print("\n")

print(l_for_display[5]) #6
print(tup_display[2])
print("----------------------------")
print("\n")

print(l_for_display[6]) #7
print(tup_display[2])
print("----------------------------")
print("\n")

print(l_for_display[7]) #8
print(tup_display[3])
print("----------------------------")
print("\n")

print(l_for_display[8]) #9
print(tup_display[3])
print("----------------------------")
print("\n")

print(l_for_display[9]) #10
print(tup_display[3])
print("----------------------------")