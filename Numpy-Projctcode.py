# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

data=np.genfromtxt(path, delimiter=",", skip_header=1)


print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((data, new_record),axis=0)

print("\nData: \n\n", census)
#Code starts here



# --------------
#Code starts here
age=census[:,0]
max_age=np.max(age)
print("Max",max_age)
min_age=np.min(age)
print("Min",min_age)
age_mean=np.mean(age)
print("Age mean",age_mean)
age_std=np.std(age)
print("Standard Deviation",age_std)



# --------------
#Code starts here
race_0=census [census[:,2]==0]
race_1=census [census[:,2]==1]
race_2=census [census[:,2]==2]
race_3=census [census[:,2]==3]
race_4=census [census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)


minimum=min(len_0,len_1,len_2,len_3,len_4)

if(len(race_0)==minimum):
    minority_race=np.unique(race_0[0,2])[0]
if(len(race_1)==minimum):
    minority_race=np.unique(race_1[0,2])[0]
if(len(race_2)==minimum):
    minority_race=np.unique(race_2[0,2])[0]
if(len(race_3)==minimum):
    minority_race=np.unique(race_3[0,2])[0]
if(len(race_4)==minimum):
    minority_race=np.unique(race_4[0,2])[0]
    
print("Minority",minority_race)


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
print('Senior',senior_citizens[:,0])
working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

high=census[census[:,1]>10]

low=census[census[:,1]<=10]


avg_pay_high=np.mean(high[:,7])

avg_pay_low=np.mean(low[:,7])


print("Mean of High average income= ",avg_pay_high,"\nMean of Low average income= ",avg_pay_low)

