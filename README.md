# Data-Driven-Automated-User-Registration-and-Error-Validation

## **About This Project**
This project **automates** the process of **user registration** on a demo website. Using data from a **CSV file**, the script registers multiple users on the site, checks for errors in the form, and takes **screenshots** of the results. The project is built using **Python** and **Selenium** for browser automation.

## **What I Did**
- Created a script that **automates** the user registration process on a demo website.
- The script reads **user data** from a **CSV file** and enters it into the registration form.
- **Validates** the registration by checking for any errors (e.g., invalid email or password mismatch).
- If errors occur, the script takes **screenshots** of the form with the error messages.
- If the registration is successful, the script saves a **screenshot** of the success page.
- This project demonstrates how to do **data-driven testing** by automating multiple user registrations.

## **Challenges & Solutions**
1. **Handling Form Validation Errors:**
   - **Challenge:** The registration form has various **validation rules**, and the error messages are dynamically displayed.
   - **Solution:** Used **Selenium’s WebDriverWait** to wait for error elements and capture them. If any errors were found, a **screenshot** was taken for later review.

2. **Managing Multiple User Registrations:**
   - **Challenge:** The script had to handle a large number of users, each with different details.
   - **Solution:** Used a **CSV file** to store user data, making it easy to manage multiple users without changing the code. The script reads the CSV and loops through the rows to register each user.

3. **Ensuring Browser Compatibility:**
   - **Challenge:** The project needed to run in different **browsers**, and I was using **Microsoft Edge**.
   - **Solution:** Ensured that the correct version of the **Edge WebDriver** was installed, which ensures compatibility with the browser.

## **Conclusion**
This project **automates** the registration of multiple users on a demo website and checks for errors in the form, saving **screenshots** for further inspection. It is a great example of how to automate repetitive tasks using **Python** and **Selenium**, and also how to conduct **data-driven testing** efficiently.
