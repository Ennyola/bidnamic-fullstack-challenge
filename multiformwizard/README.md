A Multipart form application that collects a set of data and adds them to the Database as a single entity

GETTiNG STARTED
- Create a virtual Environment using virtualenv or pipenv
- cd into the "multiformwizard" directory of the project (The same directory that contains manage.py and requirements.txt)
- Use the command "pip install -r requirements.txt" to install all dependencies(The dependencies are pinned in the requirements.txt file)
- Run the server using "python manage.py runserver"
- Navigate to http://127.0.0.1:8000/ to view the index page where you can add a new application.
- To view and delete the applications submitted, navigate to http://127.0.0.1:8000/applications/
- Upon navigating to the index page, while not authenticated, you will be redirected to the login page to sign in before submitting an application
- If you do not have an account, go to the signup page using the link provided on the login page
- A navbar is available on the index and applications page for easy navigation and logout
- 2 applications have been created. 1 for authentication called "accounts" and the other called "form_app" which handles all form   related activites

TESTING
- Tests have been written for each application and they can be found in the "tests" folder for each application.
- To run the tests for each application, use the command "python manage.py test [appname]" 
- To run the tests for the whole project, use the command "python manage.py test"
Using Coverage
- A third party Test package called coverage is also pinned alongside other dependencies. Running the "pip install -r requirements.txt" will install it too.
-To run tests using coverage, run the command "coverage run manage.py test [appname] -v 2" or "coverage run manage.py test -v 2"

LINTING AND FORMATTER
- PYLINT is the linting tool used
- BLACK is the formatter used


Enjoy the application :)



