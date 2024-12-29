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
with open('Data/median-household-income-by-state-2024.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Prepare the output CSV file
    with open('state_income_taxes.csv', mode='w', newline='') as outfile:
        fieldnames = ['state', 'MedianHouseholdIncome2021']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Iterate over each row in the input CSV
        for row in reader:
            state = row['state']
            income = row['MedianHouseholdIncome2021']
            
            # Open the URL
            driver.get('https://www.talent.com/tax-calculator')
            
            # Enter the income
            salary_input = driver.find_element(By.ID, 'salary-input')
            salary_input.clear()
            salary_input.send_keys(income)
            
            # Enter the state
            region_input = Select(driver.find_element(By.ID, 'region-input'))
            region_input.select_by_value(state)
            
            # Click the calculate button
            calculate_button = driver.find_element(By.ID, 'calculate-net-salary')
            calculate_button.click()
            
            # Wait for the result to load
            time.sleep(5)
            
            # Extract the net income value
            net_income_element = driver.find_element(By.CSS_SELECTOR, 'div.l-card__deductions.c-card__deductions-highlight.c-card__deductions-highlight--big div.c-card__deductions-value.timeBased')
            net_income = net_income_element.text
            
            # Write the result to the output CSV
            writer.writerow({'State': state, 'Net Income': net_income})

# Close the webdriver
driver.quit()