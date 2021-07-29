import datetime
import pytz

#The goal of __repr__ is to be unambiguous
#The goal of __str__ is to be readable 

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b= str(a)

print('str(a): {}'.format(str(a))) #both are readable, but data type is ambiguous.
print('str(b): {}'.format(str(b)))

print 

print('repr(a): {}'.format(repr(a))) #date time (unambiguous)
print('repr(b): {}'.format(repr(b))) #string (readable)