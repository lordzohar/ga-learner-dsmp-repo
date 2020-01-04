# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
#you can save path='' and save it to your location
path='file.csv'
data=np.genfromtxt(path, delimiter=",", skip_header=1)

#Printing tye of data
print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Concatenation of new record
census=np.concatenate((data, new_record),axis=0)

print("\nData: \n\n", census)
#Code starts here



# --------------
#Finding the age of census
age=census[:,0]
# Maximum age of census
max_age=np.max(age)
print("Max",max_age)
# Minimum age of census
min_age=np.min(age)
print("Min",min_age)
age_mean=np.mean(age)
#Mean age of census
print("Age mean",age_mean)
# Standard deviaion from the mean it's can be changed by changing the sample and size of diffrent samples
age_std=np.std(age)
print("Standard Deviation",age_std)



# --------------
#Finding diffrent kinds of races within the data
race_0=census [census[:,2]==0]
race_1=census [census[:,2]==1]
race_2=census [census[:,2]==2]
race_3=census [census[:,2]==3]
race_4=census [census[:,2]==4]

#finding the length of each race
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Race having least count
minimum=min(len_0,len_1,len_2,len_3,len_4)

#Finding the index or actual race eg if race 3 in minimum print 3 so to do it we need to find unique value from data point race
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
#Finding senior citizen within the data age >60
senior_citizens=census[census[:,0]>60]
print('Senior',senior_citizens[:,0])
working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
#Averge working hours of senior members
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Categorizing data high or low based on his education >10 or less than equal to 10
high=census[census[:,1]>10]

low=census[census[:,1]<=10]

#Average salary for both high and low income
avg_pay_high=np.mean(high[:,7])

avg_pay_low=np.mean(low[:,7])


print("Mean of High average income= ",avg_pay_high,"\nMean of Low average income= ",avg_pay_low)


