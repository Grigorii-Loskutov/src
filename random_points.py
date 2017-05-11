import os
import matplotlib.pyplot as plt
import numpy
import datetime
#import random

import numpy as numpy

fig=plt.figure()

cafe_number=2
stuff_number=10
t_staff=[0 for j in range(stuff_number)]
#start_time=datetime.datetime(2017,2,12,22,00)
cday=datetime.date.today()
print(cday)
start_time=datetime.datetime(cday.year,cday.month,cday.day,22,00)
print(start_time)
x_staff_coord=5*numpy.random.random_integers(stuff_number, size=(stuff_number))
y_staff_coord=5*numpy.random.random_integers(stuff_number, size=(stuff_number))
x_cafe_coord=5*numpy.random.random_integers(stuff_number, size=(cafe_number))
y_cafe_coord=5*numpy.random.random_integers(stuff_number, size=(cafe_number))
cafe=numpy.random.random_integers(cafe_number, size=(stuff_number))
for i in range (0,stuff_number):
    t_staff[i]=start_time+datetime.timedelta(hours=numpy.random.randint(1,5),minutes=numpy.random.randint(1,60))
    print (t_staff[i].strftime("%H:%M"))
    plt.text(x_staff_coord[i]+0.1,y_staff_coord[i]+0.1, t_staff[i].strftime("%H:%M"), fontsize=8)
    plt.text(x_staff_coord[i] + 0.1, y_staff_coord[i] - 1, str(cafe[i]), fontsize=8)

#    plt.scatter(x_staff_coord[i], y_staff_coord[i], marker='+',color='k')
#    print(t_stuff[i])

print(x_staff_coord)
print(y_staff_coord)
plt.scatter(x_staff_coord, y_staff_coord, marker='+',color='k')
plt.scatter(x_cafe_coord, y_cafe_coord, marker='*',color='r')

file_name_time=datetime.datetime.today().strftime("%Y.%m.%d.%H_%M")+'time'
file_name_coordinate_staff=datetime.datetime.today().strftime("%Y.%m.%d.%H_%M")+'staff'
file_name_coordinate_cafe=datetime.datetime.today().strftime("%Y.%m.%d.%H_%M")+'cafe'
#print(file_name_time,file_name_coordinate_cafe,file_name_coordinate_staff)
os.chdir('C:/Users/GRIGORII/Documents/src/test_points')
f1=open(file_name_time+'.txt','w')
f2=open(file_name_coordinate_staff+'.txt','w')
f3=open(file_name_coordinate_cafe+'.txt','w')
for index in range(0,stuff_number):
    f1.write(t_staff[index].strftime("%H,%M")+'\n')
    f2.write(str(x_staff_coord[index])+','+str(y_staff_coord[index])+';'+str(cafe[index])+'\n')
for index in range(0, cafe_number):
    f3.write(str(x_cafe_coord[index])+','+str(y_cafe_coord[index])+'\n')
    plt.text(x_cafe_coord[index]-1, y_cafe_coord[index]-1, str(index), color='r')

f1.close
f2.close
f3.close
plt.show()
