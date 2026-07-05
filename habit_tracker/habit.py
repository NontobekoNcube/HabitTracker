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
        #add today's date to completion_dates list if it is not already in the list
        if date.today() not in self.completion_dates:
            #check if it is not in list
            self.completion_dates.append(date.today())
        else:
            print("Already completed today!")
    

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
        if not self.completion_dates:
            return 0
        step = self.periodicity_checker() #checks for the periodicity of habit task, daily = 1, weekly = 7 that is there should be a log once in 7 days , monthly = 30, log once in 30 days 
        #sort list completion_dates
        sorted_dates = sorted(self.completion_dates)
        current_streak =  1 #default value of starting count of current streak
        longest_streak = 1 #dfault value of starting count of longest streak
        for i in range(1,len(sorted_dates)): #loops through the sorted dates list
            diff = (sorted_dates[i] - sorted_dates[i-1]).days  #diff is a variable that stores the difference between the index date and previous date to find gaps
            if diff == step: #if the difference is the same as step, that is periodicity then execute the following
                current_streak += 1 # adds 1 to the current streak count
            else:
                current_streak = 1  # if diff is not the same value as step, then reassign current_streak to 1
            if current_streak > longest_streak: # if current_streak value is greater than longest_streak then execute the following block
                longest_streak =  current_streak # longest streak is the current streak
        return longest_streak # keep value of longest streak now. 

    def broken_cycles(self):
        #checks how many times the user didn't complete their streak
        total_cycles = (date.today() - self.creation_date).days // self.target_period #total_cycles is the difference from the time the habit is created and the date today divided by the target period
        completed_cycles = self.get_longest_streak() // self.target_period # completed cycles is the longest streak divided by the target period. We call longest/-streak() because there is no need for the empty list check since get_longest_streak() already returns 0 for empty lists, apply the DRY principle.
        return max(0, total_cycles - completed_cycles)
    
    
    def is_broken(self):
        streak = self.get_current_streak()
        return streak == 0
    

