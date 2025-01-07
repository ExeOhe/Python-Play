#import date time  module
import datetime
# get the current time
current_time = datetime.datetime.now()
# print the current time
print(current_time.strftime("The time is currrently : %I: %M: %S %p"))