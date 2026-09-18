import statistics
import time
start=time.time()
data =[2000000,50000,6000000,409000,460000,897000]

mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)

print("The mean is ",mean)
print("The median is ",median)
print("The mode is ",mode)

end=time.time()
time1=end-start
print("The time is ",time1)