# sparcs_descriptive_2022

## Project Overview
The goal of this project is to perform descriptive analytics of the **2022 SPARCS (Statewide Planning and Research Cooperative System)** de-identified dataset, focusing on healthcare trends, patient demographics, and hospital performance metrics for Nassau and Suffolk counties in New York.

### Objective
In this project, I am working with a subset of the SPARCS 2022 dataset to:
- Perform descriptive statistical analysis on key metrics like Length of Stay, Total Charges, and Total Costs.
- Create visualizations to help analyze trends in patient admissions and hospital costs.
- Summarize the key findings from the analysis.

### Dataset
The dataset is publicly available and includes de-identified hospital inpatient discharge data for 2022. For this project, I focused on the following fields:
- Age Group
- Gender
- Length of Stay
- Total Charges
- Total Costs
- Type of Admission

### Analysis Steps
1. **Loading the Data:**
   - I used Pandas to load the dataset into Python and filtered it for Nassau and Suffolk counties.
   
2. **Basic Descriptive Statistics:**
   - I calculated statistics like mean, median, standard deviation, and percentiles for Length of Stay, Total Charges, and Total Costs.

3. **Exploring Categorical Variables:**
   - I looked at the distribution of Age Group, Gender, and Type of Admission, and used bar plots to visualize the counts.
   - ![Screenshot 2024-10-10 114900](https://github.com/user-attachments/assets/23b07e4b-3b2b-413d-b066-dcc2af546d0a)
   - ![Screenshot 2024-10-10 114921](https://github.com/user-attachments/assets/7ca0c9f6-cfc1-4af0-93c8-2f6356e01807)
   - ![Screenshot 2024-10-10 114939](https://github.com/user-attachments/assets/a1069c12-92fa-4e69-acbb-0323649f7520)


4. **Visualizations:**
   - I created a histogram of Length of Stay to see its distribution.
   - ![Screenshot 2024-10-10 115003](https://github.com/user-attachments/assets/1a3ef724-bc7d-499b-a545-2205090b5e51)

   - A boxplot was used to check for outliers in Total Charges.
   - ![Screenshot 2024-10-10 115018](https://github.com/user-attachments/assets/730fc2c1-1209-4bc3-89c1-3b8f8a65563c)

   - A bar plot was made to visualize trends in Type of Admission (e.g., Emergency, Elective, Trauma).
   - ![Screenshot 2024-10-10 115033](https://github.com/user-attachments/assets/78c7c04d-c8c9-4169-bc88-d3b9610da82a)


5. **Handling Missing Data:**
   - I checked for missing values in the dataset and handled them by dropping rows with missing values.

6. **Summary of Findings:**
   - I wrote up a short summary of what I found from the analysis, such as the average length of stay, how costs varied by age group, and any trends in admission types.

## How to Run the Analysis

To run the analysis, I followed these steps:

1. **Download the Dataset:**
   - I Downloaded the SPARCS 2022 dataset from [here](https://health.data.ny.gov/resource/5dtw-tffi.csv) and save it as `sparcs_2022.csv` in my project directory.

2. **Install Required Libraries:**
   - The Python libraries required for this project are `pandas` and `matplotlib`. 

3. **Run the Python Script:**
   - Once the dataset was downloaded and the libraries were installed, I opened the `sparcs_2022.py` file in **VS Code** and ran the script to perform the analysis.
  
# Key Findings

- **Average Length of Stay**: Most patients stay for 3 days or less, with an average stay of **5.26 days**.
- **Total Costs by Age**: Younger patients (0-17 years) had the highest average total costs at **\$869.02**, while older patients (70+) had the lowest, at **\$316.03**.
- **Emergency Admissions**: Emergency admissions were the most common and had higher costs compared to other admission types.


## Conclusion

This project allowed me to analyze real-world healthcare data using Python. I explored how factors like age and admission type impact hospital stays and costs.


