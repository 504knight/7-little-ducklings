
# 7 Little Ducklings - Odd Jobs

The purpose of this app is to make casual odd jobs simpler by connecting customer to worker.

## Workspace Layout

The main folder for this app is this repository.

All examples and reference documents will be stored under the folder "docs"
The plan will also be stored in "docs".

The Django server and all associated files will be stored under "OddJobs."
(Name subject to change)

## Version-Control Procedures

All team members have access to modify the main branch of this repository. Each change will be made in a branch, then reviewed by the team, and then
merged to the main branch.

## Tool Stack Description and Setup Procedure

- Django: We will be using Django because it is a simple framework that already includes most of the features
we might need and uses a programming language we are all fairly familiar with. We can easily create database models using the built-in SQLite database.

- Bootstrap: We will use the Bootstrap CSS framework because it is easy to make mobile first apps and Logan Ballard is very familiar with it.

## Build Instructions

Clone the project using any Unix-based command line using the command `git clone https://github.
com/504knight/7-little-ducklings.git`

If Django is not installed, run `python -m pip install Django`

To start the server, go into the "OddJobs" folder and run `python manage.py runserver`

To see the server work, open a browser and go to localhost:8000.

## Unit Testing Instructions

Functions that need testing: Login, Account Creation, Money Transfer, Job Posting, Job Accepting, Make Review,
Delete Account, Delete Review.

Unit tests can be found in the `unittests.py` file. Running the program will automatically run every unit test.
(Likely to change in the future)

## System Testing Instructions

To test the system, go into the app repository and start the server by running `python manage.py runserver`. Log in
with the test accounts. (Username: CustomerTest, password: ctest), (Username: WorkerTest, password: wtest),
(Username: OwnerTest, password: otest). This will allow you to test the functions of each account type.

