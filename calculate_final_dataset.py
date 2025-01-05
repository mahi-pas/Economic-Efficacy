

'''
Open csv file MyData/merged_data.csv

Create new output csv file MyData/final_dataset.csv
csv headers will be:
['State', 'State Code', 'Median Family Income', 'Median Single Income', 'Yearly 4 Bedroom Rent', 'Yearly Studio Rent', 'Yearly Childcare', 'Yearly Grocery', 'Yearly Water', 'Yearly Electricity', 'Yearly Internet', 'Yearly Mobile Plan', 'Yearly Cost for 1 Car', 'Yearly Healthcare', 'Total Cost for Family of 4', 'Income Minus Cost for 4',  'Total Cost for Single Person', 'Income Minus Cost for 1']

'''

import csv

# Open the merged data file
with open('MyData/merged_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Prepare the output CSV file
    with open('MyData/final_dataset.csv', mode='w', newline='') as outfile:
        #fieldnames = ['State Code', 'State', 'Median Family Income', 'Yearly 4 Bedroom Rent', 'Yearly Childcare for 2 children', 'Yearly Grocery for 3.5 people', 'Yearly Water for 4 people', 'Yearly Electricity for 4 people', 'Yearly Internet', 'Yearly Mobile Plans for 4', 'Yearly Cost for 2 Cars', 'Yearly Healthcare for 4 people', 'Total Cost for Family of 4', 'Income Minus Cost for 4', 'Median Single Income', 'Yearly Studio Rent', 'Yearly Groceries for 1 person', 'Yearly Water for 1 person', 'Yearly Electricity for 1 person', 'Yearly Internet', 'Yearly Mobile Plans for 1', 'Yearly Cost for 1 Car', 'Yearly Healthcare for 1 person', 'Total Cost for Single Person', 'Income Minus Cost for 1']
        fieldnames = ['State', 'State Code', 'Median Family Income', 'Median Single Income', 'Yearly 4 Bedroom Rent', 'Yearly Studio Rent', 'Yearly Childcare', 'Child Tax Credit', 'Yearly Grocery', 'Yearly Water', 'Yearly Electricity', 'Yearly Internet', 'Yearly Mobile Plan Tax Rate', 'Yearly Cost for 1 Car', 'Yearly Healthcare', 'Total Cost for Family of 4', 'Leftover Income for Family of Four',  'Total Cost for Single Person', 'Leftover Income for Single Person', 'Difference in Cost of Family vs Being Single', 'Leftover Income for Family vs Single Person']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        mobile_plan_single = 60
        mobile_plan_family = 120
        
        # Iterate over each row in the input CSV
        for row in reader:
            state = row['STATE']
            state_code = row['Code']
            median_family_income = float(row['Net Income 4 People'])
            median_single_income = float(row['Net Income 1 Person'])
            yearly_4_bedroom_rent = float(row['4 Bedroom Rent']) * 12
            yearly_studio_rent = float(row['Studio Rent']) * 12
            yearly_childcare = float(row['ChildCareCostsAnnualCostPerChild'])
            yearly_child_tax_credit = float(row['Child Tax Credit'])
            yearly_grocery = float(row['GroceryPrices2023AverageMonthlyCostOfGroceriesPerPerson']) * 12
            yearly_water = float(row['WaterPricesMonthlyWaterBill']) * 12
            yearly_electricity = float(row['Residential October 2024']) * 12
            yearly_internet = float(row['StartingCostMonthly']) * 12
            yearly_mobile_plan_tax = ((1 + (float(row['TOTAL TRANSACTION TAX'])/100))) * 12
            yearly_car = float(row['Total Costs for One Year of Car Ownership'])
            yearly_healthcare = float(row['HealthCareCostsSpendingPerCapita2020KFF'])
        
            total_cost_family = yearly_4_bedroom_rent + (yearly_childcare * 2) + (yearly_child_tax_credit * -1)
            + (yearly_grocery * 3.5) + (yearly_water * 4) + (yearly_electricity * 4) + yearly_internet
            + (yearly_mobile_plan_tax * mobile_plan_family) + (yearly_car * 2) + (yearly_healthcare * 4)

            total_cost_family = round(total_cost_family, 2)

            total_cost_single = yearly_studio_rent + yearly_grocery + yearly_water 
            + yearly_electricity + (yearly_mobile_plan_tax * mobile_plan_single) + yearly_internet
            + yearly_car + yearly_healthcare

            total_cost_single = round(total_cost_single, 2)

            income_minus_cost_family = median_family_income - total_cost_family
            income_minus_cost_single = median_single_income - total_cost_single

            income_minus_cost_family = round(income_minus_cost_family, 2)
            income_minus_cost_single = round(income_minus_cost_single, 2)

            # Write the result to the output CSV
            writer.writerow({
                'State': state,
                'State Code': state_code,
                'Median Family Income': median_family_income,
                'Median Single Income': median_single_income,
                'Yearly 4 Bedroom Rent': yearly_4_bedroom_rent,
                'Yearly Studio Rent': yearly_studio_rent,
                'Yearly Childcare': yearly_childcare,
                'Child Tax Credit': yearly_child_tax_credit,
                'Yearly Grocery': yearly_grocery,
                'Yearly Water': yearly_water,
                'Yearly Electricity': yearly_electricity,
                'Yearly Internet': yearly_mobile_plan_tax,
                'Yearly Mobile Plan Tax Rate': yearly_mobile_plan_tax,
                'Yearly Cost for 1 Car': yearly_car,
                'Yearly Healthcare': yearly_healthcare,
                'Total Cost for Family of 4': total_cost_family,
                'Leftover Income for Family of Four': income_minus_cost_family,
                'Total Cost for Single Person': total_cost_single,
                'Leftover Income for Single Person': income_minus_cost_single,
                'Difference in Cost of Family vs Being Single': total_cost_family - total_cost_single,
                'Leftover Income for Family vs Single Person': income_minus_cost_family - income_minus_cost_single
            })

            