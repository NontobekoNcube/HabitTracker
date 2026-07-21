def get_habits_by_periodicity(habits, periodicity):
    """
    Returns a list of habits that match the given periodicity.
    
    :param habits: List of Habit objects
    :param periodicity: String representing the periodicity to filter by (e.g., "daily", "weekly", "monthly")
    :return: List of Habit objects that match the given periodicity
    """
    return [habit for habit in habits if habit.periodicity == periodicity]

def get_habits_by_streak_length(habits, min_streak_length):
    """
    Returns a list of habits that have a current streak length greater than or equal to the specified minimum streak length.
    
    :param habits: List of Habit objects
    :param min_streak_length: Integer representing the minimum streak length to filter by
    :return: List of Habit objects that have a current streak length >= min_streak_length
    """
    return [habit for habit in habits if habit.get_current_streak() >= min_streak_length]

def get_longest_streak_habits(habits):
    """
    Returns a list of habits that have the longest streak length among the given habits.
    
    :param habits: List of Habit objects
    :return: List of Habit objects that have the longest streak length
    """
    if not habits:
        return []
    
    max_streak_length = max(habit.get_longest_streak() for habit in habits)
    return [habit for habit in habits if habit.get_longest_streak() == max_streak_length]

def get_longest_streak_habit(habit):
     """
    Returns the longest streak for a given habit.
    
    :param habit: Habit object
    :return: Integer representing the longest streak
    """
     return habit.get_longest_streak()
