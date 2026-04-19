import pandas as pd

df = pd.read_csv('loan_data.csv')

# print(data.head())    # Display the first few rows of the dataset
# print(data.columns)   # Display the column names
# print(data.info())    # Display information about the dataset, including data types and non-null counts

df['person_age'] = df['person_age'].astype('int')  # Convert the 'person_age' column to integer data type
# print(data.dtypes)

# Convert the 'previous_loan_defaults_on_file' column to binary values (1 for 'Yes' and 0 for 'No')
df['previous_loan_defaults_on_file'] = df['previous_loan_defaults_on_file'].map({'Yes' : 1, 'No' : 0})  
# print(df['previous_loan_defaults_on_file'].head())

# print(df.duplicated().sum())  # Check for duplicate rows in the dataset and print the count of duplicates

print(df['loan_status'].value_counts())  # Print the count of each unique value in the 'loan_status' column to understand how many people have defaulted on their loans versus those who have not.

print(df['loan_status'].value_counts(normalize = True))  # Print the proportion of each unique value in the 'loan_status' column to understand the percentage of people who have defaulted on their loans versus those who have not.

print(df.groupby('loan_status')['person_income'].mean()) # Print the average income for each loan status category to understand if there is a correlation between income and loan defaulting.

print(df.groupby('loan_status')['credit_score'].mean())  # Print the average credit score for each loan status category to understand if there is a correlation between credit score and loan defaulting.

print(df.groupby('loan_status')['loan_amnt'].mean())  # Print the average loan amount for each loan status category to understand if there is a correlation between loan amount and loan defaulting.

print(df.groupby('loan_intent')['loan_status'].mean())  # Print the average loan status(percentage) for each loan intent category to understand if there is a correlation between the purpose of the loan and the likelihood of defaulting.

print(df.groupby('loan_status')[['person_income', 'loan_amnt']].mean())  # Print the average income and loan amount for each loan status category to understand if there is a correlation between these two factors and loan defaulting.

df['income_group'] = pd.qcut(df['person_income'], q = 5)  # Create a new column 'income_group' by categorizing the 'person_income' column into 5 equal-sized groups (quintiles) to analyze the relationship between income levels and loan defaulting.
print(df.groupby('income_group')['loan_status'].mean())  # Print the average loan status(percentage) for each income group category to understand if there is a correlation between income levels and the likelihood of defaulting on a loan.

print(df.groupby('previous_loan_defaults_on_file')['loan_status'].mean())  # Print the average loan status(percentage) for each category of previous loan defaults on file to understand if there is a correlation between having previous loan defaults on file and the likelihood of defaulting on a current loan.

print(df['previous_loan_defaults_on_file'].value_counts()) # Print the count of each unique value in the 'previous_loan_defaults_on_file' column to understand how many people have had previous loan defaults on file versus those who have not.

print(pd.crosstab(df['previous_loan_defaults_on_file'],df['loan_status']))  # Create a cross-tabulation of the 'previous_loan_defaults_on_file' and 'loan_status' columns to understand the relationship between having previous loan defaults on file and the likelihood of defaulting on a current loan.

print(pd.crosstab(df['previous_loan_defaults_on_file'], df['loan_status'], normalize = 'index'))  # Create a normalized cross-tabulation of the 'previous_loan_defaults_on_file' and 'loan_status' columns to understand the percentage of people with previous loan defaults on file who have defaulted on their current loan versus those who have not.

print(df.groupby('loan_status')['loan_percent_income'].mean())  # Print the average loan percent income for each loan status category to understand if there is a correlation between the percentage of income that goes towards the loan and the likelihood of defaulting.

print(df.groupby('loan_status')['person_emp_exp'].mean())  # Print the average employment experience for each loan status category to understand if there is a correlation between employment experience and loan defaulting.

print(df.groupby('person_home_ownership')['loan_status'].mean())  # Print the average loan status(percentage) for each home ownership category to understand if there is a correlation between home ownership status and the likelihood of defaulting on a loan.