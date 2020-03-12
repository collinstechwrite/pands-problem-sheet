
"""
weekday.py is a program that outputs whether or not today is a weekday.
An example of running this program on a Thursday is given below.
$ python weekday.py
Yes, unfortunately today is a weekday.
An example of running it on a Saturday is as follows.
$ python weekday.py
It is the weekend, yay!
"""


#This program uses datetime weekday to return an integer value for the day,
#each key of the dictionary represents day of week, where Monday is 0 and Sunday is 6, etc.,
#then the program uses indexing dictionary key to return dictionary value
#source: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date



import datetime

#weekday variable responses ammend to suit
Monday = "Yes, unfortunately today is a weekday."
Tuesday = "Yes, unfortunately today is a weekday."
Wednesday = "Yes, unfortunately today is a weekday."
Thursday = "Yes, unfortunately today is a weekday."
Friday = "Yes, unfortunately today is a weekday."
Saturday = "It is the weekend, yay!"
Sunday = "It is the weekend, yay!"


the_day_is_number = datetime.datetime.today().weekday() #Return the day of the week as an integer, 

my_dictionary_responses = {0:Monday,1:Tuesday, 2:Wednesday, \
3:Thursday,4:Friday,5:Saturday,6:Sunday}


print(my_dictionary_responses[the_day_is_number]) #using the_day_is_number variable to access dictionary key to return dictionary value
