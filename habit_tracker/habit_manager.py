#create habit_manager class

from habit_tracker import db     #call db functions

class HabitManager: #manages a collection of Habit objects
    def __init__(self):
        self.habits= []
    
    def add_habit(self, habit): 
        #adds an existing Habit object to the habits list
        self.habits.append(habit)

    def delete_habit(self, habit_id):# deletes a habit from the habits list and the database based on its id
        #remove from memory
        self.habits = [h for h in self.habits if h.id != habit_id]
        #for each value h, if h.id is not in the list anymore, create new list without the value
        # remove from database 
        db.delete_habit(habit_id)

    def get_all_habits(self): #returns the list of all Habit objects
        return self.habits
    
    def save_to_db(self,habit): #saves a habit object to the database
        #calls db.save_habit 
        db.save_habit(habit)
        

    def load_from_db(self): #loads the habits from the database and returns a list of Habit objects
        #calls db.load_from_db
        self.habits = db.load_habits() 
        for habit in self.habits:
            habit.completion_dates = db.load_completions(habit.id) #load completion dates for each habit from the database