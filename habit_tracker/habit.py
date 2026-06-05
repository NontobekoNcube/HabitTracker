# create habit class
#version 1.0 : Weekly periods roll on 7 day blocks from creation date
#version 2.0 : Will implement calendar weeks (Mon-Sun)

from datetime import date, timedelta

class Habit:
    def __init__(self, name, periodicity, target_period):
        self.name = name
        self.periodicity = periodicity
        self.target_period = target_period
        self.creation_date = date.today() #automatically set to current date habit object is created on. 
        self.completion_dates = []

    def mark_complete(self):
        #add today's date to completion_dates list
        self.completion_dates.append(date.today())

    def get_current_streak(self):
        check_date= date.today()
        #checks if completion_dates is not empty
        if self.completion_dates == []:
            return 0
        
        #check periodicity to determine the step of the streak counter
        else:
            if self.periodicity == "daily":
                step = 1
            elif self.periodicity == "weekly":
                step = 7 
            else:
                step = 30

        streak = 0
        while check_date in self.completion_dates:
            streak +=1
            check_date -= timedelta(days=step)
        return streak

    def  get_progress():
        
    def get_longest_streak():
    def broken_cycles():
    
    def is_broken():
    def change_periodicity():


#test 1 get_current_streak function:
coding = Habit("coding", "daily", 14)
coding.completion_dates = [date.today() - timedelta(days=2), date.today()- timedelta(days=1),date.today()]
print(coding.get_current_streak()) #Expected: 3

#test 2 get_current_streak function:


        


    

#run = Habit("Run", "daily", 7)
#print(run.completion_dates)
#run.mark_complete()
#print(run.completion_dates) 

