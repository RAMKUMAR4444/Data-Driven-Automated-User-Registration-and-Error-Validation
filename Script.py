import time  # We use this module to pause the program for a few seconds when needed.
import csv  # This module helps us read data from CSV files.
from selenium import webdriver  # This helps us control the web browser to automate tasks.
from selenium.webdriver.common.by import By  # Helps us find elements on the webpage.
from selenium.webdriver.support.ui import WebDriverWait  # Allows us to wait for elements to load.
from selenium.webdriver.support import expected_conditions as EC  # Checks if elements are visible or clickable.

# These are the file paths where we will save screenshots and get user data.
screenshot_path = r"B:/python sel/error/"  # Folder where we'll save screenshots if errors happen.
csv_file_path = r"R:/Lib/Book2.csv"  # Path to the CSV file that contains the users' information.

# Start up the web browser (we are using Microsoft Edge here).
Driver = webdriver.Edge()
wait = WebDriverWait(Driver, 5)  # We'll wait for 5 seconds before timing out while searching for elements.

Driver.get("https://demowebshop.tricentis.com/")  # Open the website where we want to register users.
time.sleep(5)  # Wait for the website to load properly.

# Function to register a user with their details
def register_user(gender, firstname, lastname, email, password, confirmpassword):
    try:
        # Go to the Register page
        Register = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Register']")))
        Register.click()  # Click on the 'Register' link.

        time.sleep(2)  # Wait for the registration page to load.

        # Select gender
        if gender.lower() == "male":
            gender_button = wait.until(EC.presence_of_element_located((By.ID, "gender-male")))
        elif gender.lower() == "female":
            gender_button = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        else:
            print(f"Invalid gender for user {firstname} {lastname}. Skipping...")  # If gender is invalid, skip this user.
            return

        gender_button.click()  # Click on the gender button.

        # Fill in the user's details (first name, last name, email, password, etc.)
        firstname_field = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        firstname_field.clear()  # Clear any old text from the field.
        firstname_field.send_keys(firstname)  # Type in the first name.

        lastname_field = wait.until(EC.presence_of_element_located((By.ID, "LastName")))
        lastname_field.clear()
        lastname_field.send_keys(lastname)

        email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password_field.clear()
        password_field.send_keys(password)

        confirmpassword_field = wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))
        confirmpassword_field.clear()
        confirmpassword_field.send_keys(confirmpassword)

        # Click the "Register" button to submit the form
        submit = wait.until(EC.presence_of_element_located((By.ID, "register-button")))
        submit.click()

        # Check if there are any errors during registration
        errors_found = False  # This flag will track if there were any errors.
        all_errors = []  # List to store error messages.

        # Look for a general error message (if any)
        try:
            fielderror = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="validation-summary-errors"]/ul/li'))
            )
            if fielderror:
                error_text = fielderror.text
                print(f"Error {firstname} {lastname}: {error_text}")
                errors_found = True  # Set the flag to True if we found an error.
                # Save a screenshot of the error
                error_screenshot_path = f"{screenshot_path}{firstname}_{lastname}_errors.png"
                Driver.save_screenshot(error_screenshot_path)
                print(f"Screenshot saved for the error: {error_screenshot_path}")
        except:
            print("No summary error, proceeding...")

        # Check if there are specific errors for individual fields
        if not errors_found:
            for i in range(1, 6):  # Check the first 5 possible field error messages.
                try:
                    error_message = wait.until(
                        EC.presence_of_element_located((By.XPATH, f"(//span[@class='field-validation-error']/span)[{i}]"))
                    )
                    error_text = error_message.text
                    all_errors.append(error_text)
                    errors_found = True  # Set flag if errors are found.
                except:
                    continue  # Skip if no error message for this field.

            if errors_found:
                print(f"Field-Error: {firstname} {lastname}: {all_errors}")
                field_error_screenshot_path = f"{screenshot_path}{firstname}_{lastname}_field_errors.png"
                Driver.save_screenshot(field_error_screenshot_path)
                print(f"Screenshot saved for field errors: {field_error_screenshot_path}")

        if not errors_found:
            print(f"Registration successful for user: {firstname} {lastname}")

        # Click 'Continue' to finish the registration process
        submit1 = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Continue"]')))
        submit1.click()

        # Save a screenshot of the successful registration
        success = f"{screenshot_path}{firstname}_{lastname}_success.png"
        Driver.save_screenshot(success)

        time.sleep(3)  # Wait for a moment before proceeding.

        # Log out after registering and return to the homepage for the next user
        home = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Log out"]')))
        home.click()

    except Exception as e:
        print(f"Error during registration for {firstname} {lastname}: {e}")
    finally:
        # Navigate back to the homepage for the next user.
        Driver.get("https://demowebshop.tricentis.com/")
        time.sleep(2)

# Main function to process all users from the CSV file
def run_data_driven_test():
    try:
        # Open the CSV file and read user data
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)  # Read the data from the CSV.
            for row in csvreader:
                # Extract user details from each row in the CSV.
                gender = row['Gender']
                firstname = row['FirstName']
                lastname = row['LastName']
                email = row['Email']
                password = row['Password']
                confirmpassword = row['ConfirmPassword']

                print(f"Attempting to register user: {firstname} {lastname}")
                register_user(gender, firstname, lastname, email, password, confirmpassword)

    except Exception as e:
        print(f"Error reading CSV file or during registration: {e}")
    finally:
        # Close the browser once all users have been processed.
        Driver.quit()

# Start the registration process for all users in the CSV
run_data_driven_test()
