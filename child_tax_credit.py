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

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the CSV file
with open('Data/average-family-income-by-state-2024.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Prepare the output CSV file
    with open('MyData/state_child_tax_credit_for_income.csv', mode='w', newline='') as outfile:
        fieldnames = ['State', 'Child Tax Credit']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Iterate over each row in the input CSV
        for row in reader:
            state = row['STATE']
            income = row['4 PEOPLE']
            
            # Open the URL
            driver.get('https://dig.abclocal.go.com/ccg/interactives/child-tax-credit-calculator/index.html')
            
            # select  the radio button by id married and select
            married_radio = driver.find_element(By.ID, 'married')
            married_radio.click()

            
            # select button of class q1next and click
            next_button = driver.find_element(By.CLASS_NAME, 'q1next')
            #scroll to button
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            next_button.click()
            # get input by id childrenunder6 and enter 1
            children_under_6 = driver.find_element(By.ID, 'childrenunder6')
            driver.execute_script("arguments[0].scrollIntoView();", children_under_6)
            children_under_6.send_keys('1')
            # get input by id childrenover6 and enter 1
            children_over_6 = driver.find_element(By.ID, 'childrenover6')

            children_over_6.send_keys('1')
            
            # select button of class q2next and click
            next_button = driver.find_element(By.CLASS_NAME, 'q2next')
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            next_button.click()
            
            #get input by id income and enter income
            income_input = driver.find_element(By.ID, 'income')
            driver.execute_script("arguments[0].scrollIntoView();", income_input)
            income_input.send_keys(income)

            # select button of class q3submit and click
            submit_button = driver.find_element(By.CLASS_NAME, 'q3submit')
            driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            submit_button.click()

            # select div of class payment and save text to child_tax_credit
            child_tax_credit = driver.find_element(By.CLASS_NAME, 'payment').text

            
            # Write the result to the output CSV
            writer.writerow({'State': state, 'Child Tax Credit': child_tax_credit})

# Close the webdriver
driver.quit()