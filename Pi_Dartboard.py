import random
import math

n=int(raw_input('How many darts?'))
count=1
circleval=0
squareval=0
while count<=n:
    y=2*random.random()
    x=2*random.random()
    if math.sqrt((x-1)**2+(y-1)**2)<=1:
        circleval+=1
        squareval+=1
    else:
        squareval+=1
    count+=1

print 'pi is approximately', 4*(1.*circleval/squareval)
