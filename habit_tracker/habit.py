#create habit class
#version 1.0 : Weekly periods roll on 7 day blocks from creation date
#version 2.0 : Will implement calendar weeks (Mon-Sun)

from datetime import date, timedelta

class Habit:
    def __init__(self, name, periodicity, target_period):
        self.id = None  #assigned by database as primary key
        self.name = name
        self.periodicity = periodicity
        self.target_period = target_period
        self.creation_date = date.today() #automatically set to current date habit object is created on. 
        self.completion_dates = []

    def mark_complete(self):
        #add today's date to completion_dates list
        self.completion_dates.append(date.today())
    
    def periodicity_checker(self):
    #check periodicity to determine the step of the streak counter if completion_dates list is not empty
            if self.periodicity == "daily":
                step = 1
            elif self.periodicity == "weekly":
                step = 7 
            else:
                step = 30
            return step


    def get_current_streak(self):
        check_date= date.today()
        #checks if completion_dates is not empty
        if self.completion_dates == []:
            return 0
        
        #check periodicity to determine the step of the streak counter
        step = self.periodicity_checker()
        streak = 0
        while check_date in self.completion_dates:
            streak +=1
            check_date -= timedelta(days=step)
        return streak

        
    def get_longest_streak(self):
        #check if completion_dates is not empty
        if not self.completion_dates == []:
            return 0
            step = self.periodicity_checker()
            #sort list completion_dates
            sorted_dates = sorted(self.completion_dates)
            current_streak =  1
            longest_streak = 1 
            
            for i in range(1,len(sorted_dates)):
                diff = (sorted_dates[i] - sorted_dates[i-1]).days
                if diff == step:
                    current_streak += 1
                else:
                    current_streak = 1

            if current_streak > longest_streak:
                longest_streak =  current_streak
            return longest_streak




    #def broken_cycles():
    
    def is_broken(self):
        streak = self.get_current_streak()
        return streak == 0


    #def change_periodicity():

