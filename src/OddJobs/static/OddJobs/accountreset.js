let usernameRequestUrl = `${window.location.origin}/oddjobs/request_username`;
let resetRequestUrl = `${window.location.origin}/oddjobs/reset_code`;
let validEmailRegEx = /^\w+@\w+\.\w+$/;


requestUsername = function() {
    let email = getEmail();
    if(email !== null){
        fetch(`${usernameRequestUrl}/${email}`)
        .then(response => response.text().trim())
        .then(message => {
            let statusDiv = document.querySelector("#username-status-div");
            if(message == 'success'){
                statusDiv.setAttribute('class', 'alert alert-success');
                statusDiv.innerHTML = "<strong>Success!</strong> Please check your email to see your username.";
            }
            else {
                statusDiv.setAttribute('class', 'alert alert-warning');
                statusDiv.innerHTML = `<strong>Whoops</strong> ${message}`;
            }
        });
    }
    
}

sendResetCode = function(){
    let email = getEmail2();
    if(email !== null){
        fetch(`${resetRequestUrl}/${email}`)
        .then(response => response.text().trim())
        .then(message => {
            let statusDiv = document.querySelector("#password-status-div");
            if(message == 'success'){
                alert("Security Code Sent. Please check your email.");
            }
            else {
                statusDiv.setAttribute('class', 'alert alert-warning');
                statusDiv.innerHTML = `<strong>Whoops</strong> ${message}`;
            }
        });
    }
}

getEmail = function() {
    let emailInput = document.querySelector("email-input");
    let email = emailInput.value;
    if(validEmailRegEx.test(email)){
        return email;
    }
    alert("Invalid Email Format");
    return null;
}

getEmail2 = function() {
    let emailInput = document.querySelector("reset-email-input");
    let email = emailInput.value;
    if(validEmailRegEx.test(email)){
        return email;
    }
    alert("Invalid Email Format");
    return null;
}