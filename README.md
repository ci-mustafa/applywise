# ApplyWise


ApplyWise is a robust web application designed to streamline the job application process for users. It empowers individuals to take control of their job applications, providing a user-friendly platform with a range of features that enhance the application experience.

![Home Screen](/static/images/readme_images/responsive-layout.png)

[View Applywise live website here](https://applywise-f12ef2315c63.herokuapp.com/)

- - -

## Table of Contents
### [User Experience](#user-experience-ux)
* [Project Goals](#project-goals)
* [Agile Methodology](#agile-methodology)
* [User Stories](#user-stories)
* [First time user](#first-time-user)
* [Registered user](#registered-user)
* [Admin user](#admin-user)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Data Model](#data-models)
* [Database Scheme](#database-scheme)
### [Security Features](#security-features-1)
### [Features](#features-1)
* [Existing Features](#existing-features)
* [Upcoming Features](#upcoming-features)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Deployment and Local developement](#deployment-and-local-developement-1)
* [Local Developement](#local-developement)
* [PostgreSQL Database](#postgresql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)
### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgments](#acknowledgments)
- - -
## User Experience (UX)


### Project Goals
ApplyWise was designed to streamline job application management, empowering users to efficiently track and organize job applications within a single platform. The application aims to provide an intuitive, user-friendly experience that simplifies the job search process for individuals and enhances their ability to manage and monitor progress effectively.

### Agile Methodology

The Agile Methodology was employed to effectively prioritize and organize tasks, structure user stories, and manage the project workflow using GitHub Project Boards. To streamline the creation of user stories and define epics, a custom template was developed, enabling consistency and clarity across all project planning efforts.
* Epics were written containing possible user stories and based on that the website was made.
* User stories were created by looking at epics and through iterations the project was advancing.
* Project Board is set to public.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns

<details>
<summary> Project Board
</summary>

![Project Board](/static/images/readme_images/project-board.png)
</details>

<details>
<summary> Project Template
</summary>

![Project Board](/static/images/readme_images/project-template.png)
</details>

### User Stories

#### Epics
* Initial Deployment (As a developer)
    * Create a new Heroku application.

    *  Link the GitHub repository to the Heroku app for streamlined updates and deployments.
* User Interface
    *  Create a navigation bar that allows users to easily access key sections like Dashboard, Profile.
    *  Add a footer with links to support, privacy policy, and other relevant information.
    * Design a homepage that provides a brief overview of ApplyWise’s features to inform new visitors about the app’s benefits.
* User Registration and Authentication
    *  I want to register an account so that I can start tracking my job applications securely.
    * Build a registration form that collects essential details like name, email, and password.
    * Implement secure login and logout functionality to protect user data.
    * Show the user's name on the dashboard or homepage after login to confirm successful authentication.
* Job Application Management (CRUD Operations)
    * List all applications.
    * Create a form for adding new job applications with fields for company name, position, status, and application date.
    * Enable users to update application details when the status changes (e.g., interview scheduled, offer received).
    *  Provide an option to delete applications that are no longer relevant to keep the dashboard uncluttered.
* Application Tracking and Organization
    * Display all applications on a main dashboard, organized by status or application date.
    * Implement filtering options so that users can sort applications by keywords, date, or status (e.g., applied, interview, offer).
    * Add a search feature to quickly locate specific applications by entering keywords.
* Profile Customization
    * Allow users to update their profile details at any time to keep their information current.
* Design Consistency and Responsiveness
    *  Implement a consistent color scheme and layout across all pages to enhance visual cohesion.
    * Test responsiveness to ensure that all features are easily accessible on both desktop and mobile devices.
    * Use media queries and responsive design techniques to adjust layouts as needed based on device screen size.
* Contact Page
    * As an Owner of the app I want to have a Contact page So that users can easily reach out to me with questions or feedback.
    * As the owner of the app, I want to store the content of the Contact page in the database so that I can track who has contacted me.
* About Page
    * As an Owner of the app I want to have an About page so that users can learn more about me and the app.
    * As the owner of the app, I want to store the contents of the About page in the database so that I can easily update them.
* Pagination for Application List
    * As a job applicant, I want to view my job applications in a paginated format so that I can easily navigate through my applications without being overwhelmed by a long list.
* Password Reset Feature
    * As a user, I want the ability to reset my password securely, so that I can regain access to my account without complications if I forget my current password.
* Displaying Feedback Messages
    *  provide clear and actionable feedback messages to users based on their interactions with the application.

### First time user
* Easy Navigation: A well-organized layout helps new users explore features without confusion.
* About page: Engaging visuals and a quick guide introducing ApplyWise’s features and how they simplify the job search process.
* Simple Registration: A straightforward sign-up process to quickly create an account and start tracking applications.

### Registered User
* Secure Login: Fast, secure login process with personalized access to their application data.
* Job Application Management: Tools to create, edit, and delete job applications with comprehensive details.
* Progress Tracking: Visual indicators and status updates for applications, helping users manage multiple applications with ease.
* Search and Filter: Quickly locate specific applications by keywords or status, making it easy to stay organized and focused
* Dashboard: An at-a-glance view of recent activities and key metrics related to the user’s job search.

### Admin user
* Admin Portal: Secure login access to a centralized dashboard for managing user data and overseeing platform operations.
* User Account Management: Admins can modify or delete user accounts if necessary, ensuring appropriate control over data.

## Design

The ApplyWise website features a clean, professional, and intuitive design to create a seamless user experience for job seekers. With a modern color palette that includes calm, neutral tones, the design aims to evoke a sense of focus and organization, enhancing the user’s job search journey.

The navigation bar is designed to be simple and accessible, featuring a clearly marked logo and straightforward navigation options, making it easy for users to explore ApplyWise’s features. Key sections, such as the Dashboard and Application Tracker, are laid out with visual clarity, utilizing card layouts and intuitive icons to guide users through their job applications, statuses, and updates.

### Color Scheme
![Color Scheme1](static/images/readme_images/color-scheme1.png)
![Color Scheme2](static/images/readme_images/color-scheme2.png)

### Logo
* The 'Gugi' font is specified as the Logo font.

### Typography
* The 'lato' font is specified as the primary font, and the 'sans-serif' font is specified as a fallback font.

### Data Models
1. AllAuth User Model
    * Django Allauth, the User model is the default user model provided by the Django authentication system
    * The User entity has a one-to-many relationship with the Application entity. This means that a User can have multiple applications, but each application is associated with only one User.
2. Application Model
    * The Application model stores information related to job applications,
    including the position applied for, company details, application status, 
    and the method of application. Each application is linked to a specific user 
    through a foreign key relationship, allowing users to manage and track 
    their job applications effectively.
3. Contact Model
    * The Contact model is used to store contact information and messages submitted
    by users through a contact form. It includes the user's name, email address, 
    and the content of the message they wish to send.

4. About Model
    * The About model represents the information displayed in the "About" section of the ApplyWise application. This section is designed to provide users with an introduction to the developer and the purpose of the application, enhancing transparency and engagement.
5. ProfileImage
    * The ProfileImage model is designed to store the profile picture of a user in the application. This model is associated with Django's default User model through a one-to-one relationship, meaning each user can have only one profile image, and each profile image is tied to exactly one user.

### Database Scheme

Entity Relationship Diagram (ERD)
![DataScheme](static/images/readme_images/ERD-applywise.png)

## Security Features

### User Authentication

* Django Allauth is a popular authentication and authorization library for Django, which provides a set of features for managing user authentication, registration, and account management.

### Login Decorator

* application_list, create_application, edit_application, delete_application, search_applications, and filter_apps: These views involve operations related to application creation and require authentication with the login_required decorator.
* This ensures that only authenticated users can access these views.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are generated for each user session, and they are required to submit forms or perform state-changing actions. When a user logs out, the session and associated CSRF token are invalidated, making it difficult for an attacker to forge a valid request using a copied URL.

### Custom error pages

* 404 Error Page, provides user with a button the redirect to home page.
![Page Not Found](static/images/readme_images/applywise-pagenotfound.png)

## Features

* ApplyWise is a robust web application that simplifies job application management, providing users with an intuitive platform to stay organized and improve their job search outcomes.

### Existing Features
* Secure registration, login, and logout functionalities ensure that users have private and convenient access to their data.
* * Account Creation Page
![Account Creation Page](static/images/readme_images/applywise-registration.png)
* * Logout Confirmation Page
![Logout Confirmation Page](static/images/readme_images/applywise-logout.png)
* * Login Page
![Login Page](static/images/readme_images/applywise-login.png)

* Application Tracking: A centralized dashboard enables users to track the progress of all applications in one place, keeping them updated on status changes.
![Centralized Dashboard](static/images/readme_images/applywise-dashboard.png)

* Application Management: Users can create, update, and delete applications, including detailed information about positions, companies, and statuses.
* * Create Application
![Application Creation](static/images/readme_images/applywise-create-app.png)
* * Edit Application
![Edit Application](static/images/readme_images/applywise-update-app.png)
* * Delete Application
![Edit Application](static/images/readme_images/applywise-delete-app.png)

* Password Recovery: A "Forgot Password" option helps users quickly reset their passwords, allowing easy re-entry in case of forgotten credentials.
![Password Recovery](static/images/readme_images/applywise-password-recovery.png)

* Search, Filter, and Pagination: Users can efficiently locate applications with keyword search, filter by status (e.g., applied, interview, offered, rejected), and use pagination to browse applications with ease.
* * Search Apps
![Search Apps](static/images/readme_images/applywise-search.png)
* * Filter Apps
![Filter Apps](static/images/readme_images/applywise-filter1.png)
![Filter Apps](static/images/readme_images/applywise-filter2.png)
* * Pagination
![Pagination-1](static/images/readme_images/applywise-pagination1.png)
![Pagination-2](static/images/readme_images/applywise-pagination2.png)
* Profile Customization: Personalize profiles with relevant details.
![Profile](static/images/readme_images/applywise-profile.png)
* Feedback Messages: Real-time feedback messages keep users informed of completed actions, such as updates and deletions.
![Feedback Message 1](static/images/readme_images/applywise-m1.png)
![Feedback Message 2](static/images/readme_images/applywise-m2.png)
![Feedback Message 3](static/images/readme_images/applywise-m3.png)
* Contact Page: Users can reach out for support or feedback using a contact form for timely assistance from the ApplyWise team.
![Contact Page](static/images/readme_images/applywise-contact-page.png)
* About Page: Shares the mission and goals of ApplyWise, explaining how it empowers job seekers by enhancing their application management.
![About Page](static/images/readme_images/applywise-about-page.png)

### Upcoming Features
* Social Media Account Integration: Users will soon be able to create accounts and log in through social media platforms, making sign-up and login faster and easier.
* User Interface Enhancements: Improvements to the UI for a more intuitive and visually appealing experience.
* Email Reminders: Automated email notifications will remind users 15 days after applying to a job, helping them follow up on pending applications.

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used
* [PostgreSQL](https://www.postgresql.org/) - Postgres database
* [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used
* [Django](https://www.djangoproject.com/) - Python framework
* [Bootstrap 5.0.1](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - CSS framework

### Programs Used
* [Github](https://github.com/) - Storing the code online
* [Gitpod](https://www.gitpod.io/) - To write the code.
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Google Fonts](https://fonts.google.com/) - Import main font the website.
* [Am I Responsive](https://ui.dev/amiresponsive) - To show the website image on a range of devices.
* [Git](https://git-scm.com/) - Version control
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python
* [JSHint](https://jshint.com/) - Used to validate JavaScript
* [Colormind](http://colormind.io/) - Color Scheme

## Deployment and Local Developement

Live deployment can be found on this [Applywise live website here](https://applywise-f12ef2315c63.herokuapp.com/)
### Local Developement

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Applywise](https://github.com/ci-mustafa/applywise)
3. Click the fork button in the top right corner
#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Applywise](https://github.com/ci-mustafa/applywise)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt
### PostgreSQL Database
[Applywise](https://github.com/ci-mustafa/applywise) is using [PostgreSQL](https://www.postgresql.org/) Database.

For the backend of this project, ApplyWise utilizes a PostgreSQL database provided by Code Institute. This database serves as the primary storage for application data, ensuring reliable and efficient data management. To connect ApplyWise to this PostgreSQL database and enable data storage functionality, simply use the provided database URL in your environment settings.
### Cloudinary
[Applywise](https://github.com/ci-mustafa/applywise) is using [Cloudinary](https://cloudinary.com/)
1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.
### Heroku Deployment
* Log into [Heroku](https://www.heroku.com/) account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"
#### Prepare enviroment and settings.py
* In your GitPod workspace, create an env.py file in the main directory.
* Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
* Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
* Comment out the default database configuration.
* Save all files and make migrations.
* Add the Cloudinary URL to env.py
* Add the Cloudinary libraries to the list of installed apps.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

#### Add the following Config Vars in Heroku:

* SECRET_KEY - This can be any Django random secret key
* CLOUDINARY_URL - Insert your own Cloudinary API key
* PORT = 8000
* DISABLE_COLLECTSTATIC = 1 - this is temporary, and can be removed for the final deployment
* DATABASE_URL - Insert your own PostgreSQL database URL here

#### Heroku needs two additional files to deploy properly

* requirements.txt
* Procfile

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.
## Testing
Please see  [TESTING.md](TESTING.md) for all the detailed testing performed.
## References
### Docs

* [Stack Overflow](https://stackoverflow.com/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Django docs](https://docs.djangoproject.com/en/4.2/releases/3.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Cloudinary](https://cloudinary.com/documentation/diagnosing_error_codes_tutorial)
* [Google](https://www.google.com/)

### Content

* All of the content is imaginary and written by the developer, me, Mustafa Akbari.

### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would also like to extend my appreciation to the Slack community for their continuous engagement and willingness to share knowledge. The collaborative environment provided a platform for learning, troubleshooting, and gaining inspiration from fellow developers.