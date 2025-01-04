import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
import os



# Open Data/median-household-income-by-state-2024.csv
# For each state, use selenium to open the following URL: https://www.talent.com/tax-calculator
# Enter the median household income for that state into the input with id "salary-input"
# Enter the state name into the input with id "region-input"
# Click the "Calculate" button with id "calculate-net-salary"
# Extract the value from the element with class "timeBased" inside a div with class "c-card__deductions-value" inside a div with classes "l-card__deductions c-card__deductions-highlight c-card__deductions-highlight--big"
# Save the value to a csv with the state name as the key


# Initialize the webdriver
driver = webdriver.Chrome()

# Open the CSV file
with open('Data/average-family-income-by-state-2024.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Prepare the output CSV file
    with open('MyData/state_income_taxes.csv', mode='w', newline='') as outfile:
        fieldnames = ['State', 'Gross Income 1 Person', 'Net Income 1 Person', 'Gross Income 2 People', 'Net Income 2 People', 'Gross Income 3 People', 'Net Income 3 People','Gross Income 4 People', 'Net Income 4 People']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Iterate over each row in the input CSV
        for row in reader:
            state = row['STATE']
            income = [row['1 EARNER'], row['2 PEOPLE'], row['3 PEOPLE'], row['4 PEOPLE']]
            
            # Open the URL
            driver.get('https://www.talent.com/tax-calculator')
            

            
            # Enter the state
            region_input = Select(driver.find_element(By.ID, 'region-input'))
            region_input.select_by_value(state)

            net_incomes = [0,0,0,0]

            for i, inc in enumerate(income):
                # Enter the income
                salary_input = driver.find_element(By.ID, 'salary-input')
                salary_input.clear()
                salary_input.send_keys(inc)
                
                # Click the calculate button
                calculate_button = driver.find_element(By.ID, 'calculate-net-salary')
                calculate_button.click()
                            
                # Extract the net income value
                net_income_element = driver.find_element(By.CSS_SELECTOR, '.c-card__deductions-highlight--big .c-card__deductions-value .timeBased')
                net_income = net_income_element.text

                #remove non-numeric characters
                net_income = net_income.replace('$', '')
                net_income = net_income.replace(',', '')
                net_income = net_income.replace('*', '')
                net_income = net_income.replace(' ', '')
                net_income = float(net_income)

                net_incomes[i] = net_income
            
            # Write the result to the output CSV
            writer.writerow({'State': state, 'Gross Income 1 Person': income[0], 'Net Income 1 Person': net_incomes[0], 'Gross Income 2 People': income[1], 'Net Income 2 People': net_incomes[1], 'Gross Income 3 People': income[2], 'Net Income 3 People': net_incomes[2],'Gross Income 4 People': income[3], 'Net Income 4 People': net_incomes[3]})

# Close the webdriver
driver.quit()