
# 7 Little Ducklings - Odd Jobs

The purpose of this app is to make casual odd jobs simpler by connecting customer to worker.

## Workspace Layout

The main folder for this app is this repository.

All examples and reference documents will be stored under the folder `/docs`
The plan will also be stored in `docs`.

The Django server and all associated files will be stored under `/src`.
(Name subject to change)

## Version-Control Procedures

All team members have access to modify the main branch of this repository. Each change will be made in a branch, then reviewed by the team, and then
merged to the main branch.

## Tool Stack Description and Setup Procedure

- Django: We will be using Django because it is a simple framework that already includes most of the features
we might need and uses a programming language we are all fairly familiar with. We can easily create database models using the built-in SQLite database.

- Bootstrap: We will use the Bootstrap CSS framework because it is easy to make mobile first apps and Logan Ballard is very familiar with it.

## Build Instructions

Clone the project using any Unix-based command line using the command `git clone https://github.com/504knight/7-little-ducklings.git`

If Django is not installed, run `python -m pip install Django`

To start the server, go into the `/src` folder and run `python manage.py runserver`

To see the server work, open a browser and go to `localhost:8000/oddjobs`.

## Unit Testing Instructions

Functions that need testing: Login, Account Creation, Money Transfer, Job Posting, Job Accepting, Make Review.

### Visual tests:

Login + Account Creation test: Create a new user (on the oddjobs/new_user page) and then attempt to log in with the new information. User should be redirected after logging in back to the home page or whichever page the user attempted to log in from.

Job Posting test: Create a new job via the oddjobs/new_job page (only accessible when a user is logged in). The resulting job will appear in the oddjobs/active_jobs page.

Job Accepting test: Navigate to the oddjobs/available_jobs page (only accessible by a worker user) where all available jobs should be listed. Selecting a job will allow the worker to see the job details as well as an "accept job" button. The worker can select a date, then select "accept job". This job will be taken from the job board and added to the worker's accepted jobs board where the job can then be marked as complete.

Make Review test: After a job is marked as complete by a worker, a customer can go to their oddjobs/active_jobs page and view all jobs assigned or marked as complete. The customer will then be able to leave a review on the job after which the job will be removed from the oddjobs/active_jobs page and will contain a review when it is searched in the oddjobs/job_history page.

### Automated Tests:

Login tests:
- user authentication and creation: Tests that a new user can be created and authenticated
- test logged in: Tests that by default a user is not logged in, then logs in user and checks the the login worked

Still needed: Money Transfer test.

Automated unit tests can be found in the `tests.py` file. Running `python manage.py test` will run all tests.
(Likely to change in the future)

## System Testing Instructions

To test the system visually, go into the app repository and start the server by running `python manage.py runserver`. Log in
with the test accounts. Customer account -> username: alhardy, password: password. Worker account -> username: mascribner, password: password. Admin/Owner account -> username: loballard, password: password. This will allow you to test the functions of each account type.

To run automated test, run `python manage.py test` from the src folder to run the testing suite.

