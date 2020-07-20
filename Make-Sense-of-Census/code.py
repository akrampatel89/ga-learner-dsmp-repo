# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path, delimiter=",", skip_header=1)

print("\nData: \n\n", data)

census=np.concatenate((data,new_record))

print("\n census Data: \n\n", census)


# --------------
#Code starts here
import numpy as np 

age=np.array(census[:,0], dtype='int')

max_age=np.max(age)

min_age=np.min(age)

age_mean=np.mean(age)

age_diff=age-age_mean

age_diff_sum=np.sum(age_diff**2)

N=len(list(age))

age_variance=age_diff_sum/N 

age_std=age_variance**0.5

print(age_std)


# --------------
#Code starts here
import numpy as np

race=census[:,2]

race_0=census[race==0]

race_1=census[race==1]

race_2=census[race==2]

race_3=census[race==3]

race_4=census[race==4]

len_0=len(list(race_0))

len_1=len(list(race_1))

len_2=len(list(race_2))

len_3=len(list(race_3))

len_4=len(list(race_4))

len_list=[len_0,len_1,len_2,len_3,len_4]
minority_race=len_list.index(min(len_list))

print(race_0,'\n',race_1,'\n',race_2,'\n',race_3,'\n',race_4,'\n',minority_race)

print([len_0,len_1,len_2,len_3,len_4])

#print(race_0.dtype)


# --------------
#Code starts here
import numpy as np 

citizens=census[:,0]

senior=citizens>60

senior_citizens=census[senior]

print(senior_citizens)

working_hours=np.array(census[:,6])

working_hours_sum=sum(working_hours[senior])

print(working_hours_sum)

senior_citizens_len=len(list(senior_citizens))

print(senior_citizens_len)

avg_working_hours=working_hours_sum/senior_citizens_len

print(avg_working_hours)


# --------------
#Code starts here
import numpy as np 

high=census[census[:,1]>10]

low=census[census[:,1]<=10]

avg_pay_high=census[census[:,1]>10][:,7].mean()

avg_pay_low=census[census[:,1]<=10][:,7].mean()

print(avg_pay_high>avg_pay_low)


