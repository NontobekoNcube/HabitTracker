#create habit_manager class


class HabitManager:
    def __init__(self):
        self.habits= []
    
    def add_habit(self, habit):
        #adds an existing Habit object to the habits list
        self.habits.append(habit)

    def delete_habit(self, habit_id):
        #remove from memory
        self.habits = [h for h in self.habits if h.id != habit_id]
        #for each value h, if h.id is not in the list anymore, create new list without the value
        # remove from database

        #db.delete_habit(habit_id)

        #TO DO: add db.delete_habit(habit_id)

    def get_all_habits(self):
        return self.habits

       

