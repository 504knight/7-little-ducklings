let jobHistoryUrl = `${window.location.origin}/oddjobs/job_history_listings`;
let validDateRegEx = /^\d{4}-\d{2}-\d{2}$/;

let savedRating = 0;

var reloadJobListings = function(){
    //add error handling
    let startDate = getStartDate();
    let endDate = getEndDate();
    if(startDate !== null && endDate !== null){
        fetch(`${jobHistoryUrl}?start_date=${getStartDate()}&end_date=${getEndDate()}`)
        .then(response => response.text())
        .then(html => {
            let listingsTable = document.querySelector("#history-table");
            listingsTable.innerHTML = html;
        });

        setClickEvents();
    }
}

var setClickEvents = function(mutationList, observer){
    let rows = document.querySelectorAll(".clickable-row");
    for(let i = 0; i < rows.length; i++){
        rows[i].onclick = openRatingPopup;
    }
}

var getStartDate = function(){
    let startDatePicker = document.querySelector("#start-date-input");
    //if invalid alert user
    let dateVal = startDatePicker.value;
    if(validDateRegEx.test(dateVal)){
        return dateVal;
    }
    alert("Invalid Start Date entered.");
    return null;
}

var getEndDate = function(){
    let endDatePicker = document.querySelector("#end-date-input");
    let dateVal = endDatePicker.value;
    if(validDateRegEx.test(dateVal)){
        return dateVal;
    }
    alert("Invalid End Date entered.");
    return null;
}

var openRatingPopup = function(event) {
    let row = event.currentTarget;
    let firstCell = row.cells[0];
    let ratingPopupUrl = `${window.location.origin}/oddjobs/${firstCell.innerHTML}/rating_popup`;
    window.open(ratingPopupUrl);
}

var displayTempStars = function(event) {
    let starNum = parseInt(event.currentTarget.getAttribute('id').charAt(4));
    for(let i = 0; i <= starNum; i++){
        let star = document.querySelector(`#star${i}`);
        star.classList.add("checked");
    }
    for(let i = starNum + 1; i <= 4; i++){
        let star = document.querySelector(`#star${i}`);
        star.classList.remove("checked");
    }
}

var restoreSavedRating = function() {
    for(let i = 0; i < savedRating; i++) {
        let star = document.querySelector(`#star${i}`);
        star.classList.add("checked");
    }
    for(let i = savedRating; i <= 4; i++){
        let star = document.querySelector(`#star${i}`);
        star.classList.remove("checked");
    }
}

var setRating = function(event) {
    savedRating = parseInt(event.currentTarget.getAttribute('id').charAt(4)) + 1;
    let ratingInput = document.querySelector("#rating");
    ratingInput.setAttribute('value', savedRating); //set the value of the rating input in the form
    restoreSavedRating();
}


if(document.querySelectorAll('table').length !== 0){ //only run code for the job history page
    const historyTable = document.querySelector("#history-table");
    const observerOptions = {
        childList: true,
        attributes: true,
        subtree: true
    }
    const observer = new MutationObserver(setClickEvents);
    observer.observe(historyTable, observerOptions);
}