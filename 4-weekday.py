
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

the_day_is_number = datetime.datetime.today().weekday() #Return the day of the week as an integer, 

my_dictionary_responses = {0:"Yes, unfortunately today is a weekday.",1:"Yes, unfortunately today is a weekday.", 2:"Yes, unfortunately today is a weekday.", \
3:"Yes, unfortunately today is a weekday.",4:"Yes, unfortunately today is a weekday.!",5:"It is the weekend, yay!",6:"It is the weekend, yay!"}


print(my_dictionary_responses[the_day_is_number]) #using the_day_is_number variable to access dictionary key to return dictionary value
