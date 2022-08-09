'''
In this lab, the task is to read a set of temperature
data (the monthly high temperatures at Heathrow Airport for 1948 through
2016) from a file and then find some basic information:
the highest and lowest temperatures, the mean (average) temperature,
and the median temperature (the temperature in the middle if all the temperatures are sorted).
The temperature data is in the file lab_05.txt in the source code directory for
this chapter. Because I haven't yet discussed reading files, here's the code to
read the files into a list:
'''
temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

temperatures.sort()
maxtemp = max(temperatures)
mintemp = min(temperatures)
avgtemp = sum(temperatures) / len(temperatures)

if (len(temperatures) % 2 == 0):
    median = 0.5 * (temperatures[int(len(temperatures) / 2)] +
                    temperatures[int(len(temperatures) / 2) - 1])
else:
    median = temperatures[int(len(temperatures) // 2)]

'''
Determine how many unique temperatures are in the list.
'''
unitemp = list()
for temp in temperatures:
    if temperatures.count(temp) == 1:
        unitemp.append(temp)


print('''maximum temperature is {}
minimum temperature is {}
average temperature is {}
and there are {} nique temperatures in records.
'''.format(maxtemp, mintemp, "%(a).5f" % {'a': avgtemp}, len(unitemp)))
