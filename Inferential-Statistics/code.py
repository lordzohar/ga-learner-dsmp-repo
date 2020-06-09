# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]
data=pd.read_csv(path)
#Sampling over the data
data_sample=data.sample(n=sample_size,random_state=0)

#Finding the sample mean andstandard deviation of installment coloumn
sample_mean=round(data_sample['installment'].mean(),2)
sample_std=data_sample['installment'].std()

#Finding margin of error
margin_of_error=round(z_critical*(sample_std/np.sqrt(sample_size)),2)
print('margin of error %0.3f'%margin_of_error )
#Finding confidence interval
confidence_interval=[sample_mean-margin_of_error,sample_mean+margin_of_error]
print(confidence_interval)

#Finding true mean
true_mean=data['installment'].mean()

#check for 
if(true_mean>=confidence_interval[0] and true_mean<=confidence_interval[1]):print(true_mean)
else:print('Not in range')
#Code starts here



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

fig ,axes=plt.subplots(nrows = 3 , ncols = 1)

for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        m.append(data['installment'].sample(n=sample_size[i]).mean())
    mean_series=pd.Series(m)
    axes[i].hist(mean_series)
plt.show()


#Code starts here



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
'''
Null Hypothesis H_0 :μ= 12 %

Meaning: There is no difference in interest rate being given to people with purpose as 'small_business'

Alternate Hypothesis H_1: μ>12 %
Meaning: Interest rate being given to people with purpose as 'small_business' is higher than the average interest rate
'''
#Calculationg interest and stripping the % and dividing by 100
data['int.rate']=data['int.rate'].str.strip('%').astype(float)/100

#finding z_statistic,p_value for small business interests rates
z_statistic,p_value=ztest(x1=data[data['purpose']=='small_business']['int.rate'] ,value = data['int.rate'].mean(),alternative='larger')

#checking for hypothesis testing
if(p_value<=0.05):print('We reject the null hypothesis therefore H_1: μ>12 % i.e small_business is higher than the average interest rate')
else:print('We accept the null hypothesis that is H_0 :μ= 12% There is no difference in interest rate being given to people with purpose as small_business')







# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

'''
Null Hypothesis H_0: μ¨D(yes)==¨Dμ(no)

Meaning: There is no difference in installments being paid by loan defaulters and loan non defaulters

Alternate Hypothesis H_1: μ¨D(yes)¨D̸=μ(no)

Meaning: There is difference in installments being paid by loan defaulters and loan non defaulters
'''


#Code starts here
z_statistic,p_value=ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2 = data[data['paid.back.loan']=='Yes']['installment'])

if(p_value<=0.05):print('we reject null hypothesis as there is no difference in installments being paid by loan defaulters and loan non defaulters')

else:print('we accept null hypothesis as there is difference in installments being paid by loan defaulters and loan non defaulters')


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1
'''
Null Hypothesis : Distribution of purpose across all customers is same.

Alternative Hypothesis : Distribution of purpose for loan defaulters and non defaulters is different.
'''
#Code starts here

yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()

no=data[data['paid.back.loan']=='No']['purpose'].value_counts()
print(yes,no)
observed=pd.concat([yes.transpose(),no.transpose()],axis=1,keys= ['Yes','No'])
print(observed)
chi2, p, dof , ex=chi2_contingency(observed)
print(chi2, p, dof , ex)

#if(chi2>=critical_value):
#print(chi2 'chi is greater than or equal to critical value',critical_value,'therefore reject the null hypothesis that the two distributions are the same')
#else:print(chi2 'chi is less than critical value',critical_value,'we acept null hypothesis and it cannot be rejected')







