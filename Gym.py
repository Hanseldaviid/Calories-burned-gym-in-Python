
# Count of calories burned during a workout session
isTrue = True
total_calories = 0

while True:
    try:
        #Get the input from the user
        amount_exercises = int(input("Enter the amount of workouts exercises you did today: "))
        if amount_exercises > 0:
            print("Good job!)")
            break
        else:
            print("Insert a valid amount please")
    except ValueError:
        print("Enter a number ")
        
#First block of the code already build

print("Now, let's calculate the calories burned during your workout session.")

#Require for more info using a loop for
for i in range(amount_exercises):
    while isTrue:
        try:
            print("\n = = M E N U = = \n")
            print("1. Running")
            print("2. Cycling")
            print("3. Lifting Weights")
            print("4. Exit (I did no workout)")
            options = int(input("Select the exercise you did (1-4):"))
            # Selecting the options created in the menu
            if options < 0 or options > 4:
                print("Please, select an option between 1 and 4")
            else:
                match options:
                    case 1: # Running section 
                        time_running = int(input("Time spent in the running section (in minutes): "))
                        sections = int(input("How many sections? "))
                        if time_running > 0 and sections > 0:
                            calories_burned = time_running * sections * 10
                            total_calories += calories_burned
                            print(f"Total calories burned: {calories_burned}")
                            if calories_burned > 250:
                                print("Great job! Keep it up)")
                            else:
                                print("Keep going bro")
                                
                            break        
                        else:
                            print("Please, enter a valid time and sections")    
                    case 2: # Cycling section 
                        time_cycling = int(input("Time spent in the cycling section (in minutes): "))
                        sections = int(input("How many sections? "))
                        if time_cycling > 0 and sections > 0:
                            calories_burned = time_cycling *  sections * 5
                            total_calories += calories_burned
                            print(f"Total calories burned: {calories_burned}")
                            if calories_burned > 150:
                                print("Great job! Keep it up)")
                            else:
                                print("Keep going bro")
                                
                            break
                        else:
                            print("Please, enter a valid time and sections") 
                    case 3: # Lifting weights section
                        time_lifting = int(input("Time spent in the lifting weights section (in minutes): "))
                        sections = int(input("How many sections? "))
                        if time_lifting > 0 and sections > 0:
                            calories_burned = time_lifting * sections * 8
                            total_calories += calories_burned
                            print(f"Total calories burned: {calories_burned}")
                            if calories_burned > 100:
                                print("Great job! Keep it up)")
                            else:
                                print("Keep going bro")
                            
                            break    
                        else:
                            print("Please, enter a valid time and sections") 
                    case 4:
                        print("You did not anything today. You're lazy ")
                        break   
        except ValueError:
            print("Please, enter a valid number")   
            
# Summarize the total calories and exercises done
print()
print("Summary of your workout session:")
print(f"Total exercises done: {amount_exercises}, exercises | Total calories burned: {total_calories} calories")  



   
        
                            
                            
                            
            

