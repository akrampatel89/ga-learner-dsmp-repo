# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Code starts here
data=pd.read_csv(path)

loan_status= data['Loan_Status'].value_counts()

plt.bar(loan_status, loan_status.index)


# --------------
#Code starts here
property_and_loan= data.groupby(['Property_Area','Loan_Status'])

property_and_loan=property_and_loan.size().unstack()

property_and_loan.plot(kind='bar')

plt.xlabel('Property Area')

plt.ylabel('Loan Status')

plt.xticks(rotation=45)

plt.show()


# --------------
#Code starts here
education_and_loan= data.groupby(['Education','Loan_Status'])

education_and_loan=education_and_loan.size().unstack()

education_and_loan.plot(kind='bar')

plt.xlabel('Education Status')

plt.ylabel('Loan Status')

plt.xticks(rotation=45)

plt.show()


# --------------
#Code starts here
graduate=data[data.Education=='Graduate']

not_graduate=data[data.Education=='Not Graduate']

graduate.LoanAmount.plot(kind='density')

not_graduate.LoanAmount.plot(kind='density')
#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1, figsize=(20,10))

ax_1.scatter(data.ApplicantIncome, data.LoanAmount)
ax_1.set_title('Applicant Income')

#plt.scatter(data.CoapplicantIncome, data.LoanAmount, ax=ax_2)
#ax_2.set_title('Coapplicant Income')

data['TotalIncome']=data.ApplicantIncome+data.CoapplicantIncome

#plt.scatter(data.TotalIncome, data.LoanAmount, ax=ax_3)
#ax_3.set_title('Total Income')

plt.show()


