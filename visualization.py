import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('loan_data.csv')

df.groupby('loan_intent')['loan_status'].mean().plot(kind = 'bar')

plt.title('Default Rate by Loan Intent')
plt.xlabel('Loan Intent')
plt.ylabel('Default Rate')
plt.xticks(rotation = 0)

# plt.show()

# df['income_group'] = pd.qcut(df['person_income'], q = 5)
# df.groupby('income_group')['loan_status'].mean().plot(kind = 'bar')

# plt.title('Default Rate by Income Group')
# plt.xlabel('Income Group')
# plt.ylabel('Default Rate')
# plt.xticks(rotation = 45)

# plt.show()

# df.groupby('person_home_ownership')['loan_status'].mean().plot(kind = 'bar')

# plt.title('Default Rate by Home Ownership')
# plt.xlabel('Home Ownership')
# plt.ylabel('Default Rate')
# plt.xticks(rotation = 45)

# plt.show()

# df.groupby('loan_status')['loan_percent_income'].mean().plot(kind = 'bar')

# plt.title('Loan % Income by Default Status')
# plt.xlabel('Loan Status(0 = No Default, 1 = Default)')
# plt.ylabel('Loan Percent Income')
# plt.xticks(rotation = 0)

# plt.show()

# df['person_income'].plot(kind = 'hist', bins = 30)

# plt.title('Income Distribution')
# plt.xlabel('Income')
# plt.ylabel('Frequency')

# plt.show()

# print(df['person_income'].max())  # Find the maximum income in the dataset
# print(df['person_income'].sort_values(ascending = False).head())  # Show the top 5 highest incomes in the dataset
# print(df[df['person_income'] > 1000000].shape)  # Count how many people have an income greater than 1 million

# plt.hist(df['person_income'], bins=30)


# plt.title('Income Distribution(Log Scale)')
# plt.xlabel('Income')
# plt.ylabel('Number of People')

# plt.show()

# df.boxplot(column = 'person_income', by = 'loan_status')

# plt.title('Income vs Default')
# plt.suptitle('')  # Removes extra title

# plt.xlabel('Loan Status (0 = No Default, 1 = Default)')
# plt.ylabel('Income')

# plt.show()

# plt.hist(df[df['loan_status'] == 0]['credit_score'], alpha = 0.5, label = 'No Default')
# plt.hist(df[df['loan_status'] == 1]['credit_score'], alpha= 0.5, label = 'Default')

# plt.legend()

# plt.title('Credit Score Distribution')
# plt.xlabel('Credit Score')
# plt.ylabel('Count')

# plt.show()