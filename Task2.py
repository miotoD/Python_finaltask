Num_of_runners = []  # the number/ID of runner is stored here
Runners_time = []     #the time is stored here
Total_runners = 0

print("Park Run Timer\n~~~~~~~~~~~~\nLets go!")

while True:
    try:
        x = input(">")
        if x == "END":
            print("Ending..")
            break
        runner , time = x.split("::") #runner stores value input before "::", time stoes after "::"
        Num_of_runners.append(runner)
        Runners_time.append(time)
        Total_runners = Total_runners + 1  #incrementing number of runners


    except ValueError:
        print("Error in data stream.Ignoring.carrying on..")
    
fastest_time = float("inf")       #fastest time 
fastest_runner = ""           #ID of fastest runner is stored



for i in range(len(Num_of_runners)):        #calculating fastest time
    if float(Runners_time[i]) < fastest_time:
        fastest_time = float(Runners_time[i])       
        fastest_runner = Num_of_runners[i]

for time in Runners_time:                   # to calculate fastest time in minutes and seconds
    minutes, seconds = divmod(fastest_time, 60)

slowest_time = 0                        #calculating the slowest time
for time in Runners_time:
    slowest_time = max(slowest_time,float(time))

min, sec = divmod(slowest_time, 60)

total_time = 0                      #calculating average by convertitng i into float and adding in total 
for i in Runners_time:              
    total_time += float(i)
    average_time = total_time / len(Runners_time)
    m, s = divmod(average_time, 60)

print("The slowest time is: {:.0f} minutes,{:.0f} seconds.".format(min,sec))
print("The fastest time: {:.0f} minutes,{:.0f} seconds".format(minutes, seconds))
print("Total runners seen:",Total_runners)
print("The fastest runner #",fastest_runner)
print("The average time: {:.0f} minutes,{:.0f} seconds".format(m, s))