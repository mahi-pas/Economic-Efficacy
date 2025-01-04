

'''
Open csv file MyData/merged_data.csv

Create new output csv file MyData/final_dataset.csv
csv headers will be:
State Code, State, Median Family Income, Yearly 4 Bedroom Rent, Yearly Childcare for 2 children, Yearly Grocery for 3.5 people, Yearly Water for 4 people, Yearly Electricity for 4 people, Yearly Internet, Yearly Mobile Plans for 4, Yearly Cost for 2 Cars, Yearly Healthcare for 4 people, Total Cost for Family of 4, Income Minus Cost for 4, Median Single Income, Yearly Studio Rent, Yearly Groceries for 1 person, Yearly Water for 1 person, Yearly Electricity for 1 person, Yearly Internet, Yearly Mobile Plans for 1, Yearly Cost for 1 Car, Yearly Healthcare for 1 person, Total Cost for Single Person, Income Minus Cost for 1

'''

import csv

# Open the merged data file
with open('MyData/merged_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Prepare the output CSV file
    with open('MyData/final_dataset.csv', mode='w', newline='') as outfile:
        #fieldnames = ['State Code', 'State', 'Median Family Income', 'Yearly 4 Bedroom Rent', 'Yearly Childcare for 2 children', 'Yearly Grocery for 3.5 people', 'Yearly Water for 4 people', 'Yearly Electricity for 4 people', 'Yearly Internet', 'Yearly Mobile Plans for 4', 'Yearly Cost for 2 Cars', 'Yearly Healthcare for 4 people', 'Total Cost for Family of 4', 'Income Minus Cost for 4', 'Median Single Income', 'Yearly Studio Rent', 'Yearly Groceries for 1 person', 'Yearly Water for 1 person', 'Yearly Electricity for 1 person', 'Yearly Internet', 'Yearly Mobile Plans for 1', 'Yearly Cost for 1 Car', 'Yearly Healthcare for 1 person', 'Total Cost for Single Person', 'Income Minus Cost for 1']
        fieldnames = ['State', 'State Code', 'Median Family Income', '']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Iterate over each row in the input CSV
        for row in reader:
            state = row['STATE']
            state_code = row['Code']
            median_family_income = float(row['Net Income 4 People'])
            median_single_income = float(row['Net Income 1 Person'])
            yearly_4_bedroom_rent = float(row['4 Bedroom Rent']) * 12
            yearly_studio_rent = float(row['Studio Rent']) * 12
            yearly_childcare = float(row['ChildCareCostsAnnualCostPerChild'])
            yearly_grocery = float(row['GroceryPrices2023AverageMonthlyCostOfGroceriesPerPerson']) * 12
            yearly_water = float(row['WaterPricesMonthlyWaterBill'] * 12)
            yearly_electricity = float(row['Residential October 2024']) * 12
            yearly_mobile_plans = ((1 + (float(row['TOTAL TRANSACTION TAX'])/100)) * 144) * 12
            yearly_car = float(row['Total Costs for One Year of Car Ownership'])
            yearly_healthcare = float(row['HealthCareCostsSpendingPerCapita2020KFF'])