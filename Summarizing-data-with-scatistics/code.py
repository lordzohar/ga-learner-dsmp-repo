# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)

data['Gender'].replace('Agender','-',inplace=True)
#Code starts here 

gender_count=data['Gender'].value_counts()

plt.bar(data['Gender'].unique(),gender_count)
plt.show()


# --------------
#Code starts here

alignment=data['Alignment'].value_counts()

print(alignment)
plt.pie(alignment ,labels=['good','bad','natural'],autopct='%1.1f%%')
plt.show()


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]

sc_covariance=round(sc_df.cov()['Strength'][1],2)
sc_strength=round(sc_df['Strength'].std(),2)
sc_combat=round(sc_df['Combat'].std(),2)

sc_pearson=round( sc_covariance/(sc_strength*sc_combat),2)
print(sc_covariance,sc_strength,sc_combat,sc_pearson)

#For intelligence
ic_df=data[['Intelligence','Combat']]

ic_covariance=round(ic_df.cov()['Intelligence'][1],2)
ic_intelligence=round(ic_df['Intelligence'].std(),2)
ic_combat=round(ic_df['Combat'].std(),2)

ic_pearson=round( ic_covariance/(ic_intelligence*ic_combat),2)
print(ic_covariance,ic_intelligence,ic_combat,ic_pearson)






# --------------
#Code starts here

total_high=data['Total'].quantile(q=0.99)

# print(total_high)

super_best=data[ data['Total']>total_high ]

# print(super_best)

super_best_names=list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here

fig,(ax_1,ax_2,ax_3) = plt.subplots(1,3)
ax_1.boxplot(data["Intelligence"])
ax_1.set_title("Intelligence")
ax_2.boxplot(data["Speed"])
ax_2.set_title("Speed")
ax_3.boxplot(data["Power"])
ax_3.set_title("Power")
plt.show()


