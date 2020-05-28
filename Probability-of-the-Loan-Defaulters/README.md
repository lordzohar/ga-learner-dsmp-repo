### Project Overview

# Predicting Loan Repayment

In the lending industry, investors provide loans to borrowers in exchange for the promise of repayment with interest. If the borrower repays the loan, then the lender profits from the interest. However, if the borrower is unable to repay the loan, then the lender loses money. Therefore, lenders face the problem of predicting the risk of a borrower being unable to repay a loan.


To predict this dependent variable, we will use the following independent variables available to the investor when deciding whether to fund a loan:
 we will be exploring the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back.

Problem Statement
What is the probability that the borrower paid back their loan in full?

#### About the Dataset
- here is the link of data set https://www.kaggle.com/indra90/predicting-loan-repayment

## Feature	Description

1. customer.id	ID of the customer
2. credit.policy	If the customer meets the credit underwriting criteria of LendingClub.com or not
3. purpose	The purpose of the loan(takes values :"creditcard", "debtconsolidation", "educational", "majorpurchase", "smallbusiness", and "all_other").
4. int.rate	The interest rate of the loan
5. installment	The monthly installments owed by the borrower if the loan is funded
6. log.annual.inc	The natural log of the self-reported annual income of the borrower
7. dti	The debt-to-income ratio of the borrower (amount of debt divided by annual income)
8. fico	The FICO credit score of the borrower
9. days.with.cr.line	The number of days the borrower has had a credit line.
10. revol.bal	The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle)
11. revol.util	The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available)
12. pub.rec	The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments)
13. inq.last.6mths	The borrower's number of inquiries by creditors in the last 6 months
14. delinq.2yrs	The number of times the borrower had been 30+ days past due on a payment in the past 2 years
15. paid.back.loan	Whether the user has paid back loan

### Why solve this project?
After completing this project, we will have a better understanding of probability. In this project, you will apply the following concepts.

- Independency check
- Bayes theorem
- Visualizing discrete variable
- Visualizing continuous variable


### Learnings from the project

 1. Conditional filterting
2. Finding probability on various columns
3. Finding Independence among columns
4. Finding conditonal probablity
5. Various visualization techniques


### Approach taken to solve the problem

 Probablistic approach to find the most probably value


### Challenges faced

 Calculating conditional probablities for multiple couloumns and given conditional probablity formula

> P(A∣B)= P(B∣A).P(A)/P(B)

### Additional pointers

 Thank you for looking into this feel free to fork this code and try various pedictions on the dataset


