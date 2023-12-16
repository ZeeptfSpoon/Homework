# practical exersises from university lab2

"""

"""


# Global Constants Values:
a=None
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
poem = ('''Yes, I'll smile, indeed,through tears and weeping 
           Sing my songs where evil holds its way,
           Hopeless, a steadfast hope forever keeping, 
           I shall live! You thoughts of grief, away''')

#global functions

seconds_per_hour = seconds_per_minute * minutes_per_hour
seconds_per_day = seconds_per_hour * hours_per_day

#counting answers
ex1 = seconds_per_day / seconds_per_hour
ex2 = seconds_per_day // seconds_per_hour

#answers

print(seconds_per_hour)
print(seconds_per_day)
print(ex1)
print(ex2)

#poem fnct


print(poem[0:15])
print(len(poem))
print(poem.startswith("Yes"))
print(poem.endswith("I shall live"))
print(poem.find(","))
print(poem.rfind(","))
print(poem.count(","))
print(poem.isalnum())





