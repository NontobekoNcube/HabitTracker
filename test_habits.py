from habit_tracker.habit import Habit
from datetime import date, timedelta

#test functions for get_current_streak() method, 
# when the streak is consecutive and when it is broken

def test_get_current_streak_consecutive():
    habit =  Habit("coding", "daily", 14)
    habit.completion_dates = [date.today()- timedelta(days=2), date.today() - timedelta(days=1), date.today()]
    assert habit.get_current_streak() == 3

def test_get_current_streak_with_break():
    habit = Habit("coding", "daily", 14)
    habit.completion_dates = [date.today() - timedelta(days=3), date.today() - timedelta(days=1), date.today()]
    assert habit.get_current_streak() == 2

def test_is_broken_with_no_break():
    #test1 when streak is not broken
    habit =  Habit("coding", "daily", 14)
    habit.completion_dates = [date.today()]
    assert habit.is_broken() == False

def test_is_broken_with_broken_streak():
    #when streak is broken, the streak is broken when there is no record of completion for current day 
    habit = Habit("coding", "daily", 14)
    habit.completion_dates = [date.today() - timedelta(days=2), date.today()- timedelta(days=1)]
    assert habit.is_broken() == True


