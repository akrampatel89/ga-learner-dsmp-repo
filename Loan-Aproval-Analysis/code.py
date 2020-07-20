# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank=pd.read_csv(path)

categorical_var=bank.select_dtypes(include= 'object')

print(categorical_var)

numerical_var=bank.select_dtypes(include='number')

print(numerical_var)

# code ends here


# --------------
# code starts here
banks=bank.drop(['Loan_ID'],axis=1)

print(banks.isnull().sum())

bank_mode=banks.mode().iloc[0]

print(bank_mode)

banks.fillna(bank_mode, inplace=True)

print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
import pandas as pd



avg_loan_amount=pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc='mean')

print(avg_loan_amount)

# code ends here



# --------------
# code starts here
yes=(banks['Loan_Status']=='Y') & (banks['Self_Employed']=='Yes')

loan_approved_se=banks[yes].count()[0]

no=(banks['Loan_Status']=='Y') & (banks['Self_Employed']=='No')

loan_approved_nse=banks[no].count()[0]

Loan_Status_count=banks['Loan_Status'].count()

percentage_se=100*loan_approved_se/Loan_Status_count

percentage_nse=100*loan_approved_nse/Loan_Status_count

print(percentage_nse,percentage_se)

# code ends here


# --------------
# code starts here



#banks['loan_term']=banks.Loan_Amount_Term.apply(lambda x:int(x)/12)

#big_loan_term=banks[banks['loan_term']>=25].count()[0]

#loan_term=lambda x:int(x)/12
#big_loan_term=len(banks[banks.Loan_Amount_Term.apply(loan_term)>=25].index)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )

big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby=banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']

mean_values=loan_groupby.mean()

print(mean_values)

# code ends here


