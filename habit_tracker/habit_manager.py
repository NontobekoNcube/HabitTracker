#create habit_manager class


class HabitManager:
    def __init__(self):
        self.habits= []
    
    def add_habit(self, habit):
        #adds an existing Habit object to the habits list
        self.habits.append(habit)

    def delete_habit(self, habit_id):
        #remove from memory
        self.habits = [h for h in self.habits if h.id ! = habit_id]
        # remove from database
        db.delete_habit(habit_id)

        #TO DO: add db.delete_habit(habit_id)
        
       

