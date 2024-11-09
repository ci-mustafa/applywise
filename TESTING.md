# ApplyWise | Testing

Return to [README](README.md)
- - -
Comprehensive testing has been performed to ensure the website's seamless and optimal functionality.

## Table of Contents
### [Responsiveness Testing](#responsiveness-testing-1)
### [Browser Compatibility Testing](#browser-compatibility-testing-1)
### [Device Testing](#device-testing-1)
### [Code Validation](#code-validation-1)
* [HTML Validation](#html-validation)
* [CSS Validation](#css-validation)
* [JavaScript Validation](#javascript-validation)
* [Python](#python)
### [Automated Testing](#automated-testing-1)
* [Applyhub App Testing Forms](#applyhub-app-testing-forms)
* [Applyhub App Testing Views](#applyhub-app-testing-views)
* [About App Testing Views](#about-app-testing-views)
* [Contact App Testing Forms](#contact-app-testing-forms)
* [Contact App Testing views](#contact-app-testing-views)
---

## Responsiveness Testing
To ensure responsiveness and adaptability, the deployed website was thoroughly tested across a range of devices and screen sizes. Developer Tools were used to simulate various screen dimensions, allowing for an in-depth review of the website’s performance on different devices. Bootstrap classes and media queries were applied strategically to preserve both the design and functionality, guaranteeing a consistent and user-friendly experience on all platforms. This approach ensures that the website remains visually appealing and fully operational, regardless of the device used.
![Am I Responsive](static/images/testing_images/responsive-layout.png)

<details>
<summary> PC
</summary>

![PC](static/images/testing_images/testing-pc.png)
</details>

<details>
<summary> Tablet
</summary>

![Tablet](static/images/testing_images/testing-tablet.png)
</details>

<details>
<summary> Mobile
</summary>

![Mobile](static/images/testing_images/testing-phone.png)
</details>

## Browser Compatibility Testing

The project was tested on Chrome and Microsoft Edge web browsers to check for compatibility issues and ensure it functions as expected across all of them. This testing process guarantees a smooth and consistent user experience, regardless of the browser used.

## Device Testing
Device testing was conducted on a variety of phone models, including Samsung Galaxy A13, iPhone 14 pro max, iPhone 15 pro. The assistance of family members and friends was sought to perform the testing. This comprehensive approach ensured that the website was thoroughly evaluated on different devices and platforms, contributing to a more robust and user-friendly final product.

## Code Validation
### HTML Validation

<details>
<summary> Home Page
</summary>

![Home Page](static/images/testing_images/testing-homepage.png)
</details>

<details>
<summary> About Page
</summary>

![About Page](static/images/testing_images/testing-aboutpage.png)
</details>

<details>
<summary> Application Detials Page
</summary>

![Application Detials Page](static/images/testing_images/testing-appdetailspage.png)
</details>

<details>
<summary> Contact Page
</summary>

![Contact Page](static/images/testing_images/testing-contactpage.png)
</details>

<details>
<summary> Create Application Page
</summary>

![Create Application Page](static/images/testing_images/testing-createapp.png)
</details>

<details>
<summary> Filter Page
</summary>

![Filter Page](static/images/testing_images/testing-filterpage.png)
</details>

<details>
<summary> Search Page
</summary>

![Search Page](static/images/testing_images/testing-searchpage.png)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](static/images/testing_images/testing-loginpage.png)
</details>

<details>
<summary> Logout Page
</summary>

![Logout Page](static/images/testing_images/testing-logoutpage.png)
</details>

<details>
<summary> Profile Page
</summary>

![Profile Page](static/images/testing_images/testing-profilepage.png)
</details>

<details>
<summary> Reset Password Page
</summary>

![Reset Password Page](static/images/testing_images/testing-resetpasswordpage.png)
</details>

### CSS Validation

<details>
<summary> Custom CSS (style.css)
</summary>

![Custom CSS (style.css)](static/images/testing_images/css-validation.png)
</details>

### JavaScript Validation

<details>
<summary> Custom JS (delete-confirmation.js)
</summary>

![Custom JS (delete-confirmation.js)](static/images/testing_images/testing-js-delete-confirmation-script.png)
</details>

<details>
<summary> Logo Hover Inline Script
</summary>

![Logo Hover Inline Script](static/images/testing_images/testing-js-logocode.png)
</details>

<details>
<summary> Profile Picture Selection Inline Script
</summary>

![Profile Picture Selection Inline Script](static/images/testing_images/testing-js-profileupdate.png)
</details>

### Python

#### applyhub App
<details>
<summary> admin.py
</summary>

![admin.py](static/images/testing_images/testing-applyhub-admin.png)
</details>

<details>
<summary> views.py
</summary>

![views.py](static/images/testing_images/testing-applyhub-view.png)
</details>

<details>
<summary> models.py
</summary>

![models.py](static/images/testing_images/testing-applyhub-model.png)
</details>

<details>
<summary> urls.py
</summary>

![urls.py](static/images/testing_images/testing-applyhub-urls.png)
</details>

<details>
<summary> forms.py
</summary>

![forms.py](static/images/testing_images/testing-applyhub-form.png)
</details>

<details>
<summary> test_forms.py
</summary>

![test_forms.py](static/images/testing_images/testing-applyhub-form-test.png)
</details>

<details>
<summary> test_views.py
</summary>

![test_views.py](static/images/testing_images/testing-applyhub-view-test.png)
</details>

##### Note:
The code for the Contact, About, and MyProfile apps has been thoroughly reviewed and refactored to comply with the PEP8 standards, ensuring consistent and readable code throughout these modules.

## Automated Testing
The project includes a comprehensive suite of 13 Python automated tests covering core functionality across the ApplyHub, Contact, and About apps. These tests are designed to ensure robust application performance by validating form inputs, submission handling, and request responses (GET and POST).
### Applyhub app testing forms
The application form tests are designed to ensure that the CreateAppForm in the application works as expected, handling both required and optional fields correctly. These tests validate the form under two main conditions:
* Valid Data with Optional Fields Left Blank:
Tests that the form is valid even when optional fields (description, job_link, and recruiter_contact) are left blank, as long as the required fields have valid data. This test confirms that users can submit the form without filling optional information while still meeting the required input criteria.
* Valid Data with All Fields Filled:
Checks form validity when all fields, both required and optional, contain appropriate data. This ensures that the form accepts fully completed entries, providing flexibility for users to supply additional details if available.

### Applyhub app testing views
This test suite is designed to verify the functionality of views within the ApplyHub application, specifically focusing on the application list view and the application creation process. Below is a breakdown of the tests included:
* Application List View Tests:
Ensures that authenticated users can view their list of applications, with all relevant application data appearing correctly on the page.
Tests that unauthenticated users attempting to access the application list are redirected to the login page, maintaining the security of user-specific data.
* Create Application View Tests:
Verifies that users can successfully create new applications via a POST request, confirming that valid form data creates an Application instance in the database.
Checks that all submitted fields (required and optional) are correctly saved and linked to the logged-in user.
Ensures that after a successful creation, the user is redirected to the home page, improving the user flow.

### About app testing views
This test suite validates the functionality of the About View in the about app, ensuring that the correct template and context data are provided when accessing the about page.
* Setup of Test Data:
Creates a test About object containing developer image, title, and content, to simulate real data in the application.
* Testing the About View:
Verifies that a GET request to the About page returns a successful (HTTP 200) response.
Confirms that the correct template (about.html) is rendered, ensuring the user views the intended layout and information.
Checks that the context contains the About instance, ensuring that the relevant data is available to display on the About page.

### Contact app testing forms
This test suite validates the ContactForm in the Contact app, covering form validation, email format verification, and field constraints.
* Valid Data:
Confirms that the form validates successfully when provided with all required data (name, email, and message).
Ensures that the form functions as expected when users submit complete and valid information.
* Empty Data (Invalid Submission):
Checks that the form is invalid when required fields (name, email, message) are left empty.
This test ensures proper error handling and validation, flagging the correct fields with errors for incomplete submissions.
* Invalid Email Format:
Verifies that the form does not validate if the email is formatted incorrectly, raising an error on the email field.
This test confirms that only properly formatted email addresses are accepted, ensuring data accuracy.
* Exceeding Name Length:
Ensures the form is invalid if the name field exceeds the maximum allowed length.
This test checks that the form restricts names to a specified length, providing appropriate error messages when limits are exceeded.
* Valid Email Format with Other Fields Filled:
Confirms that the form validates correctly when a properly formatted email is provided alongside a valid name and message.
This test verifies the form’s acceptance of well-formed entries, reinforcing reliable data processing for complete submissions.

### Contact app testing views
The Contact View Tests ensure that the contact page and form submission processes work correctly, validating both form rendering and successful data handling.
* GET Request for Contact View:
Confirms that the contact page loads successfully, displaying a blank form when accessed via a GET request.
Ensures that the correct template (contact.html) is rendered and that a ContactForm instance is passed in the context.
* POST Request with Valid Data:
Verifies that a valid form submission saves the data in the database.
Ensures that a new Contact instance is created with the correct name, email, and message details from the form.
* Email Sending:
Checks that an email is sent upon valid form submission.
Validates the email subject, content, and sender address, ensuring accurate and expected email communication.
* Success Message and Redirection:
Confirms that a success message is displayed after a successful form submission.
Ensures that the user is redirected back to the contact page, providing a smooth user experience.
