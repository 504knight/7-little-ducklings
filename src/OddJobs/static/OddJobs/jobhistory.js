let jobHistoryUrl = `${window.location.origin}/oddjobs/job_history_listings`;

var reloadJobListings = function(){
    //add error handling
    fetch(`${jobHistoryUrl}?start_date=${getStartDate()}&end_date=${getEndDate()}`)
    .then(function(response){
        let jobListingsHTML =  response.text();
        let listingsTable = document.querySelector("#history-table");
        listingsTable.innerHTML = jobListingsHTML;
    });
}

var getStartDate = function(){
    let startDatePicker = document.querySelector("#start-date-input");
    //should probably filter input and also check to make sure that the format returned by .value works as parameter for obtaining job listings
    //if invalid alert user
    return startDatePicker.value;
}

var getEndDate = function(){
    let endDatePicker = document.querySelector("#end-date-input");
    //filter in the same way as getStartDate
    return endDatePicker.value;
}
