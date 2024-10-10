import pandas as pd

# Loading the data set

df = pd.read_csv('C:/Users/shvet/Downloads/HHA507_Assignments/sparcs_2022.csv')

df_filtered = df.loc[df['Hospital County'].isin(['Nassau', 'Suffolk'])]

print(df_filtered['Hospital County'].value_counts())

subset_data = df_filtered[['Age Group', 'Gender', 'Length of Stay', 'Total Charges', 'Total Costs', 'Type of Admission', 'Discharge Year', 'Ethnicity', 'Race']]

print(subset_data)


subset_data['Length of Stay'] = pd.to_numeric(subset_data['Length of Stay'], errors='coerce')
subset_data['Total Charges'] = pd.to_numeric(subset_data['Total Charges'], errors='coerce')
subset_data['Total Costs'] = pd.to_numeric(subset_data['Total Costs'], errors='coerce')

# Descriptive statistics for Length of Stay, Total Charges, and Total Costs
stats = subset_data[['Length of Stay', 'Total Charges', 'Total Costs']].describe()

percentiles = subset_data[['Length of Stay', 'Total Charges', 'Total Costs']].quantile([0.25, 0.5, 0.75])
print(stats)
print(percentiles)

# Count distribution of categorical variables
age_group_counts = subset_data['Age Group'].value_counts()
gender_counts = subset_data['Gender'].value_counts()
admission_type_counts = subset_data['Type of Admission'].value_counts()

print(age_group_counts)
print(gender_counts)
print(admission_type_counts)


import matplotlib.pyplot as plt


# Visualization (bar plot)

# Age Group Distribution
age_group_counts.plot(kind='bar', title='Age Group Distribution')
plt.show()

# Gender Distribution
gender_counts.plot(kind='bar', title='Gender Distribution')
plt.show()

# Admission Type Distribution
admission_type_counts.plot(kind='bar', title='Admission Type Distribution')
plt.show()


# Histogram for Length of Stay
plt.hist(subset_data['Length of Stay'], bins=20)
plt.title('Histogram of Length of Stay')
plt.xlabel('Length of Stay')
plt.ylabel('Frequency')
plt.show()

# Boxplot for Total Charges
plt.boxplot(subset_data['Total Charges'].dropna())
plt.title('Boxplot of Total Charges')
plt.ylabel('Total Charges')
plt.xlabel('Charges') 
plt.show()

# Bar plot for Type of Admission
admission_type_counts.plot(kind='bar', title='Type of Admission Distribution')
plt.ylabel('Count')
plt.show()

# Check for missing data
missing_data = subset_data.isnull().sum()

#Drop rows with missing data
subset_data_cleaned = subset_data.dropna()


# Group by Age Group and calculate the mean total cost
total_cost_by_age_group = subset_data.groupby('Age Group')['Total Costs'].mean()

print("Total Cost by Age Group:")
print(total_cost_by_age_group)


### Summary Report: SPARCS Descriptive 2022 Analysis

### 1. Average Length of Stay
# The average length of stay across all hospital admissions is approximately 5.26 days. The majority of patients have a relatively short stay, 
# with 50% of admissions lasting 3 days or less, and 75% of admissions lasting 6 days or less.
# - Minimum Length of Stay: 1 day
# - Maximum Length of Stay: 119 days
# - 25th Percentile: 2 days
# - Median (50th Percentile): 3 days
# - 75th Percentile: 6 days

### 2. Total Cost Variation by Age Group
#The total costs of hospital admissions vary significantly depending on age group. 
# - Patients aged 0 to 17 have the highest average total costs at $869.02.
# - Patients aged 18 to 29 have an average total cost of $485.11.
# - Patients aged 30 to 49 have an average total cost of $408.64.
# - Patients aged 50 to 69 have an average total cost of $335.51.
# - Patients aged 70 or older have the lowest average total cost at $316.03.

### Observations:
# - Young patients (0 to 17 years) have the highest average total costs, which could be due to more complex cases or specialized care requirements.
# - The total costs decreased with age, despite older adults having the highest length of stay. Which could be influenced by factors such as Medicare or Medicaid coverage.

### 3. Noticeable Trends in Admissions and Charges:
# - Admission Types: Emergency admissions are by far the most common type of all admissions. Elective admissions also account for a significant portion, while urgent admissions are relatively rare.
# - Charges: The distribution of total charges shows most patients incurring charges below $455, while the maximum charge reached $945.42.
# - Length of Stay: Most hospital stays were brief, with 50% of patients staying less than 3 days. However, some outliers experienced extremely long stays, which likely influenced the average length of stay.
