# Use Case Diagrams

## User Registers for an Account

<img src="/docs/use-case-diagrams/user-creates-account.jpg">

<strong>Participating actors:</strong> User  
<strong>Entry Conditions:</strong>
<ul>
    <li>User wishes to create an account.</li>
</ul>  
<strong>Exit Conditions:</strong>
<ul>
    <li>Account is created</li>
    <li>User no longer wishes to create an account</li>
</ul>
<strong>Event Flow:</strong>
<ol>
    <li>User requests to create an account (navigates to account creation page).</li>
    <li>User enters account information into the input fields on account creation page.
    </li>
    <li>User submits information for account creation.</li>
    <li>
        System validates user input.<br>
        <ul>
            <li>If the input is valid, then an account is created and a confirmation is displayed to the user.</li>
            <li>If the input is invalid, then the system notifies the user that their input is invalid.</li>
        </ul>
    </li>
</ol>   


## Customer Creates a Work Order/Request

<img src="/docs/use-case-diagrams/customer-creates-work-request.jpg">

<strong>Participating actors:</strong> Customer  
<strong>Entry Conditions:</strong> 
<ul>
    <li>User is logged-in</li>
</ul> 
<strong>Exit Conditions:</strong> 
<ul>
    <li>The user decides not to fill out a work request</li>
</ul> 

<strong>Event Flow:</strong>  
<ol>
    <li>User requests to create a work order (navigates to the create work order page).</li>
    <li>System displays user input fields.</li>
    <li>User enters information into the inputs.</li>
    <li>User submits the work order request.</li>
    <li>
        The user's inputs are validated.<br>
        <ul>
        <li>If the user's inputs are valid, then the work order is submitted.</li>
        <li>If the user's inputs are invalid, then the system notifies the user that their inputs are invalid.</li>
        </ul>
    </li>
</ol>

## User Login

<img src="/docs/use-case-diagrams/user-login.jpg">

<strong>Participating actors:</strong> User  
<strong>Entry Conditions:</strong>  
<ul>
    <li>User wishes to login</li>
</ul>
<strong>Exit Conditions:</strong>
<ul>
    <li>User decides not to login</li>
</ul>  
<strong>Event Flow:</strong>  
<ol>
    <li>User navigates to login page.</li>
    <li>User enters username and password and submits form.</li>
    <li>System checks to see if the username and password are valid.
        <ul>
            <li>If the username and password are valid, the user session is initiated and the user is redirected to the appropriate home page corresponding to their user type (customer, worker, owner).</li>
            <li>If the username and password are invalid, the user is notified.</li>
        </ul>
    </li>
    
</ol>

## Worker Selects and Accepts a Job

<img src="/docs/use-case-diagrams/accept-job.jpg">

<strong>Participating actors:</strong> Worker  
<strong>Entry Conditions:</strong>  
<ul>
    <li>Worker wants to find a job.</li>
    <li>Worker is logged in.</li>
</ul>
<strong>Exit Conditions:</strong>  
<ul>
    <li>Worker stops searching for a job.</li>
</ul>
<strong>Event Flow:</strong>  
<ol>
    <li>Worker navigates to the job listings page.</li>
    <li>The system displays all of the available job listings to the worker.</li>
    <li>The worker chooses and accepts a job from the list.</li>
    <li>The system displays a confirmation message to the worker.</li>
</ol>

## Customer Leaves Review of Job

<img src="/docs/use-case-diagrams/user-review.jpg">

<strong>Participating actors:</strong> Customer  
<strong>Entry Conditions:</strong>  
<ul>
    <li>Customer wishes to leave review</li>
    <li>Customer is logged in</li>
</ul>
<strong>Exit Conditions:</strong>
<ul>
    <li>Customer leaves a review</li>
    <li>Customer no longer wishes to leave a review</li>
</ul>
<strong>Event Flow:</strong>
<ol>
    <li>Customer navigates to Job History page.</li>
    <li>Customer selects a past job and opts to leave a review.</li>
    <li>System displays inputs for customer to leave review.</li>
    <li>Customer submits review</li>
    <li>Review is recorded in the database</li>
    <li>Submission confirmation is displayed to customer</li>
</ol>  

## Worker Cancels Job

<img src="/docs/use-case-diagrams/worker-cancel-job.jpg">

<strong>Participating actors:</strong> Worker  
<strong>Entry Conditions:</strong>  
<ul>
    <li>Worker wishes to cancel job</li>
    <li>Worker is logged in</li>
</ul>
<strong>Exit Conditions:</strong>  
<ul>
    <li>Worker decides not to cancel job</li>
    <li>Worker cancels job</li>
</ul>
<strong>Event Flow:</strong>
<ol>
    <li>Worker navigates to Work Schedule page.</li>
    <li>Worker selects a job and requests to cancel it.</li>
    <li>
        <ul>
            <li>System displays message confirming job cancelation.</li>
            <li>System changes record in database.
            <li>System notifies customer that job has been canceled and reopened to other workers.</li>
        </ul>
    </li>
</ol>  

## Customer Cancels Job

<img src="/docs/use-case-diagrams/customer-cancel-job.jpg">

<strong>Participating actors:</strong> Customer  
<strong>Entry Conditions:</strong>  
<ul>
    <li>Customer wishes to cancel job</li>
    <li>Customer is logged in</li>
</ul>
<strong>Exit Conditions:</strong>  
<ul>
    <li>Customer cancels job</li>
    <li>Customer decides not to cancel job</li>
</ul>
<strong>Event Flow:</strong>  
<ol>
    <li>Customer navigates to Scheduled Jobs page.</li>
    <li>Customer selects a job and requests to cancel it.</li>
    <li>
        <ul>
            <li>If this Job Listing has a worker associated with it, notify the worker that the job has been canceled.</li>
            <li>Delete Job Listing from the Job Listings table in the database.</li>
            <li>Display message to customer confirming the job cancelation.</li>
        </ul>
    </li>
</ol>

## Worker Marks Job as Complete

<img src="/docs/use-case-diagrams/worker-complete-job.jpg">

<strong>Participating actors:</strong> Worker  
<strong>Entry Conditions:</strong>  
<ul>
    <li>Worker has finished job</li>
    <li>Worker is logged in</li>
</ul>
<strong>Exit Conditions:</strong>  
<ul>
    <li>Worker decides not to mark job as complete.</li>
    <li>Worker marks job as complete.</li>
</ul>
<strong>Event Flow:</strong>  
<ol>
    <li>Worker navigates to work schedule page.</li>
    <li>Worker selects a job.</li>
    <li>System displays option to edit job status.</li>
    <li>Worker changes job status to complete and submits change.</li>
    <li>
        <ul>
            <li>System updates status of Job Listing in database.</li>
            <li>System charges the customer's account for the price of the job</li>
            <li>System transfers money to the worker's account.</li>
        </ul>
    </li>
</ol>

## User Edits/Deletes Account

<img src="/docs/use-case-diagrams/edit-account.jpg">

<strong>Participating actors:</strong> User  
<strong>Entry Conditions:</strong>  
<ul>
    <li>User wishes to edit their account details</li>
    <li>User is logged in</li>
</ul>
<strong>Exit Conditions:</strong>  
<ul>
    <li>User edits their account details.</li>
    <li>User decides not to edit their account</li>
</ul>
<strong>Event Flow:</strong>  
<ol>
    <li>User navigates to Account Details/Settings page.</li>
    <li>User edits one or more aspects of their account.</li>
    <li>User submits changes.</li>
    <li>The system updates these changes in the database</li>
</ol>

## Owner Reviews Workers

<img src="/docs/use-case-diagrams/owner-review.jpg">

<strong>Participating actors:</strong> Owner  
<strong>Entry Conditions:</strong>  
<ul>
    <li>Owner wishes to review workers</li>
    <li>Owner is logged in</li>
</ul>
<strong>Exit Conditions:</strong>  
<ul>
    <li>Owner is finished reviewing workers</li>
</ul>
<strong>Event Flow:</strong>  
<ol>
    <li>Owner navigates to worker review page.</li>
    <li>System populates list of workers</li>
    <li>Owner selects employee from list of workers
        <ul>
            <li>Owner requests to view reviews of jobs performed by selected worker.
                <ul>
                    <li>Query database for reviews.</li>
                    <li>Display reviews.</li>
                </ul>
            </li>
            <li>Owner requests to remove worker.
                <ul>
                    <li>Database is Updated.</li>
                    <li>Worker is notified that they have been removed.</li>
                </ul>
            </li>
        </ul>
    </li>

</ol>