from habit_tracker.habit import Habit
from datetime import date, timedelta

#test functions for get_current_streak() method, 
# when the streak is consecutive and when it is broken

def test_get_current_streak_consecutive():
    #when streak is consecutive: no gaps and today is in the list
    habit =  Habit("coding", "daily", 14)
    habit.completion_dates = [date.today()- timedelta(days=2), date.today() - timedelta(days=1), date.today()]
    assert habit.get_current_streak() == 3

def test_get_current_streak_with_break():
    #when streak is broken: What number does get_current_streak() return when there is a gap, yesterday + today =  current streak
    habit = Habit("coding", "daily", 14)
    habit.completion_dates = [date.today() - timedelta(days=3), date.today() - timedelta(days=1), date.today()]
    assert habit.get_current_streak() == 2

def test_is_broken_with_no_break():
    #when streak is not broken: today is in the list
    habit =  Habit("coding", "daily", 14)
    habit.completion_dates = [date.today()]
    assert habit.is_broken() == False

def test_is_broken_with_broken_streak():
    #when streak is broken2: does is_broken() return True/ False when today is missing? Answer: True(no completion today)
    habit = Habit("coding", "daily", 14)
    habit.completion_dates = [date.today() - timedelta(days=2), date.today()- timedelta(days=1)]
    assert habit.is_broken() == True


# test functions for longest_streak:empty completion_dates list, one date, consecutive dates with no break, dates with a break:
def test_longest_streak_empty():
    #when completion_dates is empty: should return 0
    habit = Habit("coding", "daily", 14)
    assert habit.get_longest_streak() == 0

def test_longest_streak_one_date():
    #completion_dates has one date
    habit = Habit("coding", "daily", 14)
    habit.completion_dates = [date.today()]
    assert habit.get_longest_streak() == 1

def test_longest_streak_consecutive_dates_with_no_break():
    #completion_dates has consecutive dates with no break
    habit =  Habit("coding", "daily", 14)
    habit.completion_dates = [date.today()- timedelta(days=2), date.today() - timedelta(days=1), date.today()]
    assert habit.get_longest_streak() == 3

def test_longest_streak_dates_with_a_break():
    # two streaks with a gap - longest streak should be 3
    habit =  Habit("coding", "daily", 14)
    habit.completion_dates = [date.today()- timedelta(days=4), date.today() - timedelta(days=3), date.today()- timedelta(days=2),date.today()]
    assert habit.get_longest_streak() == 3

    
