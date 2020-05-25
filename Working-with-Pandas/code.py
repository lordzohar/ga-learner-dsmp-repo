# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.DataFrame( pd.read_csv(path) )

categorical_var=bank.select_dtypes(include = 'object')

print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number')

print(numerical_var)



# code ends here


# --------------
# code starts here

# print (bank['Loan_ID'] )
banks=bank.drop('Loan_ID',axis=1)

print(banks.head(10))
print( banks.isnull().sum() )

bank_mode=banks.mode()
print(bank_mode)

banks=banks.fillna(0)
print(banks.head(100))

#code ends here


# --------------
# Code starts here




avg_loan_amount=pd.pivot_table (banks, index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount', aggfunc="mean")

print(avg_loan_amount)
# code ends here



# --------------
# code starts here





loan_approved_se=len (banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status'] == 'Y')])
loan_approved_nse =len(banks [ (banks['Self_Employed'] == 'No' ) & ( banks['Loan_Status'] == 'Y') ])
print(loan_approved_se,loan_approved_nse)
Loan_Status=614

percentage_se=(loan_approved_se/Loan_Status) *100

percentage_nse=(loan_approved_nse/Loan_Status) *100


# code ends here


# --------------
# code starts here

loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)

print(loan_term.head(10))

big_loan_term=len (loan_term [loan_term>=25 ])

print(big_loan_term)

# code ends here


# --------------
# code starts here




loan_groupby=banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']

mean_values=loan_groupby.mean()


# code ends here


