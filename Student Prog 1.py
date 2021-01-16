

def range_check_of_student_version(your_input_1):                                                                          #function for check the range
    if  your_input_1 <= 120 and your_input_1 >= 0 and your_input_1 % 20 == 0 :    
        save_1 = True
  

    else:
        print("range error")
        save_1 = False
        return save_1

def progress_check_of_student_version():                                                                                     #function for progression outcome
    if ps_mark_for_student_version == 120:
        print("Progress")

    elif ps_mark_for_student_version == 100:
        print("Progress–module trailer")

    elif fl_mark_for_student_version >= 80:
        print("Exclude")

    else:
        print("Do not progress–module retriever")
#--------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime                                                                                                #time is imported from your computer's local time
now_time_pc = datetime.now()                                                                                                 #I learnt the code for importing time from https://docs.python.org/3/library/time.html website.
live_time_by_your_pc = now_time_pc.strftime("%H:%M:%S")                                                                      #and i used it by changing variable names
print("✦ _________________________________________________________________ ✦")    
print("\n")
print("    Welcome to the Student Progression Program - Student Version                ")                                    #welcome message
print("                    Time is : ", live_time_by_your_pc)
print("✦ _________________________________________________________________ ✦")
#--------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("                        -USER INSTRUCTIONS-                           ")                                              #user instructions
user_instructions_for_students_1=print("01.Please use only 0  / 20 / 40 / 60 / 80 / 100 / 120 as your marks.")
user_instructions_for_students_2=print("02.Please do not use letters / symbols / special characters as your inputs.")
#--------------------------------------------------------------------------------------------------------------------------------------

print("\n")
student_id = input("Please enter your Student ID number : ")                                                                  #student id 
print("Hello " + str(student_id))
print("\n")

save_2 = False     
while save_2 == False:

    boolean_range_student_version = False
    while boolean_range_student_version == False:
        try:
            ps_mark_for_student_version = int(input("Please enter your PASS credit :"))
            boolean_range_student_version = range_check_of_student_version(ps_mark_for_student_version)           
        
        except ValueError:
            print("Integers required")
            boolean_range_student_version = False

    boolean_range_student_version = False
    while boolean_range_student_version == False:
        try:
            df_mark_for_student_version = int(input("Please enter your DEFER credit :"))
            boolean_range_student_version = range_check_of_student_version(df_mark_for_student_version)          
        
        except ValueError:
            print("Integers required")
            boolean_range_student_version = False

    boolean_range_student_version = False
    while boolean_range_student_version == False:
        try:
            fl_mark_for_student_version = int(input("Please enter your FAIL credit:"))
            boolean_range_student_version = range_check_of_student_version(fl_mark_for_student_version)          
        
        except ValueError:
            print("Integers required")
            boolean_range_student_version = False
#---------------------------------------------------------------------------------------------------------------------------------------  
    total_marks_of_student_version = ps_mark_for_student_version + fl_mark_for_student_version + df_mark_for_student_version         #Total calculated by the sum of 3 credit types
    if total_marks_of_student_version == 120:
        save_2 = True
        print("\n")
    else:
        print("Total incorrect")
        save_2 = False
      
progress_check_of_student_version()                                                                                                                                       

print("___________________________________________________________________")                                                          #program exit message
print("Thanks for using Student progression Program. Have a nice day!")
print("\n")
#--------------------------------------------------------------------------------------------------------------------------------------
#                              end of the programme

