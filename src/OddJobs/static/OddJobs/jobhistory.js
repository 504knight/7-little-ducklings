let jobHistoryUrl = "..."

var reloadJobListings = function(startDate, endDate){
    fetch(jobHistoryUrl + "?" + startDate + "&" + endDate)
    .then(function(response){
        let jobListingsHTML =  response.text();
        let listingsTable = document.querySelector("#history-table");
        listingsTable.innerHTML = jobListingsHTML;
    });
}
