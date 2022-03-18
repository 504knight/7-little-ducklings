
var displayForm = function(action) {
    let actionInput = document.querySelector("#action-input");
    let amountLbl = document.querySelector("#amount-label");
    let submitBtn = document.querySelector("#submit-btn");
    let form = document.querySelector("#update-balance-form");
    if(action == 'deposit') {
        amountLbl.innerHTML = "Amount to Deposit:";
        submitBtn.innerHTML = "Deposit Funds";
        actionInput.setAttribute('value', 0);
    }
    else if(action == 'withdraw') {
        amountLbl.innerHTML = "Amount to Withdraw:";
        submitBtn.innerHTML = "Withdraw Funds";
        actionInput.setAttribute('value', 1);
    }
    form.removeAttribute('hidden');
}
