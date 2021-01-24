import re 
import datetime 

print(re.match(re.compile(r"\d{4}$"), "2018"))

print(datetime.datetime.now().year)