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

# dictionary of all us states in lowercase with dashes instead of spaces mapped to the state name with spaces and upper case
states = {
    'alabama': 'Alabama',
    'alaska': 'Alaska',
    'arizona': 'Arizona',
    'arkansas': 'Arkansas',
    'california': 'California',
    'colorado': 'Colorado',
    'connecticut': 'Connecticut',
    'delaware': 'Delaware',
    'florida': 'Florida',
    'georgia': 'Georgia',
    'hawaii': 'Hawaii',
    'idaho': 'Idaho',
    'illinois': 'Illinois',
    'indiana': 'Indiana',
    'iowa': 'Iowa',
    'kansas': 'Kansas',
    'kentucky': 'Kentucky',
    'louisiana': 'Louisiana',
    'maine': 'Maine',
    'maryland': 'Maryland',
    'massachusetts': 'Massachusetts',
    'michigan': 'Michigan',
    'minnesota': 'Minnesota',
    'mississippi': 'Mississippi',
    'missouri': 'Missouri',
    'montana': 'Montana',
    'nebraska': 'Nebraska',
    'nevada': 'Nevada',
    'new-hampshire': 'New Hampshire',
    'new-jersey': 'New Jersey',
    'new-mexico': 'New Mexico',
    'new-york': 'New York',
    'north-carolina': 'North Carolina',
    'north-dakota': 'North Dakota',
    'ohio': 'Ohio',
    'oklahoma': 'Oklahoma',
    'oregon': 'Oregon',
    'pennsylvania': 'Pennsylvania',
    'rhode-island': 'Rhode Island',
    'south-carolina': 'South Carolina',
    'south-dakota': 'South Dakota',
    'tennessee': 'Tennessee',
    'texas': 'Texas',
    'utah': 'Utah',
    'vermont': 'Vermont',
    'virginia': 'Virginia',
    'washington': 'Washington',
    'west-virginia': 'West Virginia',
    'wisconsin': 'Wisconsin',
    'wyoming': 'Wyoming'
}

if len(states) != 50:
    print('Error: there are not 50 states in the list')
    sys.exit(1)

# Open a CSV file to write the data
with open('MyData\\average_rent_2024.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['State', 'Studio Rent', '1 Bedroom Rent', '2 Bedroom Rent', '3 Bedroom Rent', '4 Bedroom Rent'])

    for state_key, state_name in states.items():
        # Navigate to the website and fetch the rent data
        url = f'https://rentalrealestate.com/data/rent/{state_key}/'
        driver.get(url)
        
        try:
            rents = driver.find_elements(By.CSS_SELECTOR, 'strong')
            # Extract the rent data
            studio_rent = rents[0].text
            one_bedroom_rent = rents[1].text
            two_bedroom_rent = rents[2].text
            three_bedroom_rent = rents[3].text
            four_bedroom_rent = rents[4].text

            # remove the $ sign, comma, and " from the rent data
            studio_rent = studio_rent.replace('$', '').replace(',', '').replace('"', '')
            one_bedroom_rent = one_bedroom_rent.replace('$', '').replace(',', '').replace('"', '')
            two_bedroom_rent = two_bedroom_rent.replace('$', '').replace(',', '').replace('"', '')
            three_bedroom_rent = three_bedroom_rent.replace('$', '').replace(',', '').replace('"', '')
            four_bedroom_rent = four_bedroom_rent.replace('$', '').replace(',', '').replace('"', '')
            
            # Write the data to the CSV file
            writer.writerow([state_name, studio_rent, one_bedroom_rent, two_bedroom_rent, three_bedroom_rent, four_bedroom_rent])
        
        except Exception as e:
            print(f'Error fetching data for {state_name}: {e}')
            continue

# Close the webdriver
driver.quit()
