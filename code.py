import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    url = "https://dharani.telangana.gov.in/knowLandStatus"

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the form element containing the dropdowns
        form = soup.find('form', {'id': 'ajax_form'})

        # Extract the CSRF token from the form
        csrf_token = form.find('input', {'name': 'csrf_test_name'}).get('value')

        # Prepare the data payload for the POST request
        data = {
            'district': district,
            'mandal': mandal,
            'village': village,
            'csrf_test_name': csrf_token
        }

        # Send a POST request with the selected options
        response = requests.post(url, data=data)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the response
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the element containing the survey numbers
            survey_numbers = soup.find('select', {'name': 'selectSurvey'}).find_all('option')

            # Extract and print the survey numbers
            for survey_number in survey_numbers:
                print(survey_number.text)
        else:
            print("Failed to fetch data. Please try again later.")
    else:
        print("Failed to connect to the website. Please check your internet connection.")

# Example
district = "Your District"
mandal = "Your Mandal"
village = "Your Village"

get_survey_numbers(district, mandal, village)
'''Replacing "Your District", "Your Mandal", and "Your Village" with the actual names of the district, mandal, and village gives, for which we want to retrieve the survey numbers.'''
