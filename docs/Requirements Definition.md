# Requirements Definition

### Functional Requirements

* 1. User Account Creation and Access
	* 1.1. User will be required to log in with an account to access system services.
		* 1.1.1. User will be able to create an account of a specific type with the following information:
			* 1.1.1.1. The account type
			* 1.1.1.2. A username
			* 1.1.1.3. A password
			* 1.1.1.4. A name to be associated with the account (First name is recommended.)
		* 1.1.2. User will be able to login to a previously created account with a username and password.
	* 1.2. Each user will have some element of control over their account.
		* 1.2.1. User will be able to check their account balance.
		* 1.2.2. User will be able to "deposit" money into their account by inputting a desired amount just as a number.
		* 1.2.3. User will be able to "withdraw" money from their account by the same method as depositing.
		* 1.2.4. User should be able to delete their account.
		* 1.2.5. User should have the ability to change their username or password.
		* 1.2.6. User could have the ability to see their job history (accepted or offered).

* 2. User Account Types
	* 2.1. There will be a customer account type with full access to customer-specific features.
		* 2.1.1. User with customer account (hereafter referred to as "Customer") will be able create a job.
			* 2.1.1.1. Customer will have to select a job type from a list of job types.
				* 2.1.1.1.1. Customer will be able to fill in a custom job type upon choosing the "other" option.
			* 2.1.1.2. Customer will have to input the location at which the job will take place.
			* 2.1.1.3. Customer will have to input their preferred time of day and day of the week for the work to take place.
			* 2.1.1.4. Customer will have to input how much they will pay for the completion of the job.
		* 2.1.2. After a Worker accepts an offered job, Customer will have to confirm and approve job acceptance.
			* 2.1.2.1. Customer should recieve a reminder to tip their worker after completion of the job if they are satisfied. 
		* 2.1.3. Customer will be able see jobs they have listed.
			* 2.1.3.1. Customer should have the ability to delete an unconfirmed job.
			* 2.1.3.2. Customer could be able to edit an unaccepted job.
		* 2.1.4. Customer should have the ability to review a Worker after the completion of a job.
		* 2.1.5. Customer should be able to blacklist a worker so that Worker cannot see their jobs anymore.
	* 2.2. There will be a worker account type with full access to worker-specific features.
		* 2.2.1. User with worker account ("Worker") will be able to view a list of available jobs.
			* 2.2.1.1. Worker shoud be able to filter jobs by distance based on an inputted zip code.
			* 2.2.1.2. Worker should have the ability to filter jobs by job type.
		* 2.2.2. Worker will be able to accept a listed job.
			* 2.2.2.1. Worker will be able to see the exact job location only after job acceptance is confirmed by Customer to ensure privacy.
		* 2.2.3. Worker should be able to see their rating.
		* 2.2.4. Worker should have the ability to blacklist a Customer so they cannot see that Customer's jobs.
	* 2.3. There will be an owner account type with full access to owner-specific features.
		* 2.3.1. Owner will be able to see a list of all requested, accepted, and confirmed jobs.
			* 2.3.1.1. Owner could be able to see all completed jobs.
		* 2.3.2. Owner will be able to see a list of all users.
		* 2.3.3. A portion of every transaction will be deposited into the Owner's account balance.
			* 2.3.3.1. The owner could be able to change the size of the portion.

---

### Non-functional Requirements

* 1. Database will be used to store information.
	* 1.1. The database will store account info including:
		* 1.1.1. Account type
		* 1.1.2. Username
		* 1.1.3. Password
		* 1.1.4. Balance
		* 1.1.5. First Name
	* 1.2. The database will store job info including:
		* 1.2.1. Job location
		* 1.2.2. Job type
		* 1.2.3. Job payment offer
		* 1.2.4. Job time window

* 2. System will be deployable.

* 3. System Mechanics
	* 3.1. System should implement a priority system based on Worker reviews.
		* 3.1.1. Higher rated workers should be shown jobs first before gradually opening up jobs to a larger and larger Worker pool.
	* 3.2. System should be able to check the distance between zip codes.

---

### Possible Future Features

Features that will not be implemented in the current version of the project but have a possibility of implementation in future iterations of the application.

* 1. Owner could have the ability to view general statistics concerning application usage.
* 2. System could notify users of certain events.
	* 2.1. Workers could be notified upon job avalability or job confirmation.
	* 2.2. Customers could be notified upon job acceptance.

---

### Glossary

Important terms used in this requirements definition document are defined here.

**System**- The application program as a whole

**Customer**- A user with a customer account type. Someone who posts jobs seeking for work to be done.

**Worker**- A user with a worker account type. Someone who accepts jobs looking to make money.

**Owner**- A user with an owner account type. The person who owns and runs the system.
