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

## Use Case Title

<strong>Participating actors:</strong>  
<strong>Entry Conditions:</strong>  
<strong>Exit Conditions:</strong>  
<strong>Special Requirements:</strong>  

## Use Case Title

<strong>Participating actors:</strong>  
<strong>Entry Conditions:</strong>  
<strong>Exit Conditions:</strong>  
<strong>Special Requirements:</strong>  

## Use Case Title

<strong>Participating actors:</strong>  
<strong>Entry Conditions:</strong>  
<strong>Exit Conditions:</strong>  
<strong>Special Requirements:</strong>  

## Use Case Title

<strong>Participating actors:</strong>  
<strong>Entry Conditions:</strong>  
<strong>Exit Conditions:</strong>  
<strong>Special Requirements:</strong>  

## Use Case Title

<strong>Participating actors:</strong>  
<strong>Entry Conditions:</strong>  
<strong>Exit Conditions:</strong>  
<strong>Special Requirements:</strong>  