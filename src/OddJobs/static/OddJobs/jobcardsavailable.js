let expandCard = function(id) {
    for (var card of jobCards) {
        if (card.jobData.pk === id) {
            const cardHTML = document.getElementById(id);
            let parent = cardHTML.parentNode;
            let childIndex = Array.from(parent.children).indexOf(cardHTML);
            cardHTML.remove();

            let jobCardHTML = document.createElement("div");
            jobCardHTML.setAttribute("id", card.jobData.pk);
            jobCardHTML.setAttribute("class", "col-lg-4 mt-3 mt-lg-0");

            let jobCardInner1 = document.createElement("div");
            jobCardInner1.setAttribute("class", "card text-center my-3");

            let jobTitle = document.createElement("h5");
            jobTitle.setAttribute("class", "card-header");
            jobTitle.textContent = card.jobData.fields.job_title;
            jobTitle.onclick = function() {
                shrinkCard(id);
            };

            let jobCardInner2 = document.createElement("div");
            jobCardInner2.setAttribute("class", "card-body");

            let jobDescription = document.createElement("p");
            jobDescription.setAttribute("class", "card-text");
            jobDescription.textContent = card.jobData.fields.job_description;

            let jobCardInner3 = document.createElement("table");
            jobCardInner3.setAttribute("class", "table table-lg");

            let jobCardInner4 = document.createElement("tbody");

            let jobLocation = document.createElement("tr");
            let jobLoc1 = document.createElement("td");
            jobLoc1.textContent = "Location:";
            let jobLoc2 = document.createElement("td");
            jobLoc2.setAttribute("class", "text-center");
            jobLoc2.textContent = card.jobData.fields.location;
            jobLocation.append(jobLoc1);
            jobLocation.append(jobLoc2);

            let jobDuration = document.createElement("tr");
            let jobDur1 = document.createElement("td");
            jobDur1.textContent = "Expected Duration:";
            let jobDur2 = document.createElement("td");
            jobDur2.setAttribute("class", "text-center");
            let duration = card.jobData.fields.duration;
            if (duration > 1440) {
                jobDur2.textContent = (duration / 1440) + " days";
            }
            else if (duration > 60) {
                jobDur2.textContent = (duration / 60) + " hours";
            }
            else {
                jobDur2.textContent = duration + " minutes";
            }
            jobDuration.append(jobDur1);
            jobDuration.append(jobDur2);
            
            let jobPay = document.createElement("tr");
            let jobPay1 = document.createElement("td");
            jobPay1.textContent = "Offered Payment:";
            let jobPay2 = document.createElement("td");
            jobPay2.setAttribute("class", "text-center");
            jobPay2.textContent = "$" + card.jobData.fields.price;
            jobPay.append(jobPay1);
            jobPay.append(jobPay2);

            let jobWindow = document.createElement("tr");
            let jobWin1 = document.createElement("td");
            let jobWin2 = document.createElement("td");
            jobWin2.setAttribute("class", "text-center");
            let startDate = new Date(card.jobData.fields.start_time);
            let endDate = new Date(card.jobData.fields.end_time);
            jobWin1.textContent = "Preferred Window:";
            jobWin2.textContent = `${startDate.toLocaleString()} to ${endDate.toLocaleString()}`;
            jobWindow.append(jobWin1);
            jobWindow.append(jobWin2);

            let dateForm = document.createElement("form");
            dateForm.action = `accept_job`;
            dateForm.method = "POST";

            let datePicker = document.createElement("input");
            datePicker.type = "datetime-local";
            datePicker.id = "date";
            datePicker.class = "form-control";
            datePicker.name = "date";
            datePicker.value = startDate;

            let csrfToken = document.createElement("input");
            csrfToken.type = "hidden";
            csrfToken.name = "csrfmiddlewaretoken";
            csrfToken.value = CSRF;

            let job_id = document.createElement("input");
            job_id.type = "hidden";
            job_id.name = "job_id";
            job_id.value = id;

            let acceptButton = document.createElement("button");
            acceptButton.setAttribute("class", "btn btn-success text-body fw-bold mx-3 mt-2");
            acceptButton.textContent = "Accept Job";
            acceptButton.type = "submit";


            jobCardHTML.append(jobCardInner1);
            jobCardInner1.append(jobTitle);
            jobCardInner1.append(jobCardInner2);
            jobCardInner2.append(jobDescription);
            jobCardInner2.append(jobCardInner3);
            jobCardInner3.append(jobCardInner4);
            jobCardInner4.append(jobLocation);
            jobCardInner4.append(jobDuration);
            jobCardInner4.append(jobPay);
            jobCardInner4.append(jobWindow);
            jobCardInner2.append(dateForm);
            dateForm.append(csrfToken);
            dateForm.append(job_id);
            dateForm.append(datePicker);
            dateForm.append(acceptButton);

            card.html = jobCardHTML;
            document.querySelector("#cardHolder").append(jobCardHTML);
            parent.insertBefore(jobCardHTML, parent.children[childIndex]);
        }
    }
}

let shrinkCard = function(id) {
    for (var card of jobCards) {
        if (card.jobData.pk === id) {
            const cardHTML = document.getElementById(id);
            let parent = cardHTML.parentNode;
            let childIndex = Array.from(parent.children).indexOf(cardHTML);
            cardHTML.remove();

            let jobCardHTML = document.createElement("div");
            jobCardHTML.setAttribute("id", card.jobData.pk);
            jobCardHTML.setAttribute("class", "col-lg-4 mt-3 mt-lg-0");

            let jobTitle = document.createElement("h5");
            jobTitle.setAttribute("class", "card-header");
            jobTitle.textContent = card.jobData.fields.job_title;

            let jobCardInner1 = document.createElement("div");
            jobCardInner1.setAttribute("class", "card text-center my-3");
            jobCardInner1.onclick = function() {
                expandCard(id);
            };

            let jobCardInner2 = document.createElement("div");
            jobCardInner2.setAttribute("class", "card-body");

            let jobDuration = document.createElement("p");
            jobDuration.setAttribute("class", "card-text");
            let duration = card.jobData.fields.duration;
            if (duration > 1440) {
                jobDuration.textContent = "Expected Duration: " + (duration / 1440) + " days";
            }
            else if (duration > 60) {
                jobDuration.textContent = "Expected Duration: " + (duration / 60) + " hours";
            }
            else {
                jobDuration.textContent = "Expected Duration: " + duration + " minutes";
            }
            
            let jobPay = document.createElement("p");
            jobPay.setAttribute("class", "card-text");
            jobPay.textContent = "Offered Payment: $" + card.jobData.fields.price;


            jobCardHTML.append(jobCardInner1);
            jobCardInner1.append(jobTitle);
            jobCardInner1.append(jobCardInner2);
            jobCardInner2.append(jobDuration);
            jobCardInner2.append(jobPay);

            card.html = jobCardHTML;
            document.querySelector("#cardHolder").append(jobCardHTML);
            parent.insertBefore(jobCardHTML, parent.children[childIndex]);
        }
    }
}

let generateCard = function(job) {

    let jobCardHTML = document.createElement("div");
    jobCardHTML.setAttribute("id", job.pk);
    jobCardHTML.setAttribute("class", "col-lg-4 mt-3 mt-lg-0");

    let jobCardInner1 = document.createElement("div");
    jobCardInner1.setAttribute("class", "card text-center my-3");
    jobCardInner1.onclick = function() {
        expandCard(job.pk);
    };
    jobCardInner1.addEventListener("click", expandCard(job.pk))

    let jobTitle = document.createElement("h5");
    jobTitle.setAttribute("class", "card-header");
    jobTitle.textContent = job.fields.job_title;

    let jobCardInner2 = document.createElement("div");
    jobCardInner2.setAttribute("class", "card-body");

    let jobDuration = document.createElement("p");
    jobDuration.setAttribute("class", "card-text");
    let duration = job.fields.duration;
    if (duration > 1440) {
        jobDuration.textContent = "Expected Duration: " + (duration / 1440) + " days";
    }
    else if (duration > 60) {
        jobDuration.textContent = "Expected Duration: " + (duration / 60) + " hours";
    }
    else {
        jobDuration.textContent = "Expected Duration: " + duration + " minutes";
    }
    
    let jobPay = document.createElement("p");
    jobPay.setAttribute("class", "card-text");
    jobPay.textContent = "Offered Payment: $" + job.fields.price;


    jobCardHTML.append(jobCardInner1);
    jobCardInner1.append(jobTitle);
    jobCardInner1.append(jobCardInner2);
    jobCardInner2.append(jobDuration);
    jobCardInner2.append(jobPay);

    let jobCard = {
        html: jobCardHTML,
        jobData: job
    }

    return jobCard;
}

var updateFilter = async function(){
    let cardHolder = document.querySelector("#cardHolder");
    cardHolder.remove();
    cardHolder = document.createElement("div");
    cardHolder.setAttribute("id", "cardHolder");
    cardHolder.setAttribute("class", "row mt-3");

    let distanceFilter = 10;
    switch (distanceDrop.selectedIndex) {
        case 0:
            distanceFilter = 5;
            break;
        case 1:
            distanceFilter = 10;
            break;
        case 2:
            distanceFilter = 15;
            break;
        case 3:
            distanceFilter = 30;
            break;
        case 4:
            distanceFilter = 99999;
            break;
        default:
            break;
    }

    let priceFilter = 5;
    switch (payDrop.selectedIndex) {
        case 0:
            priceFilter = 5;
            break;
        case 1:
            priceFilter = 10;
            break;
        case 2:
            priceFilter = 15;
            break;
        case 3:
            priceFilter = 20;
            break;
        case 4:
            priceFilter = 50;
            break;
        case 5:
            priceFilter = 80;
            break;
        default:
            break;
    }

    for (var card of jobCards) {
        if (card.jobData.fields.worker == null) {
            let distance = 0;
            /*try {
                let locationInfo = undefined;
                await fetch('https://api.freegeoip.app/json/?apikey=88a17340-5497-11ec-99dd-4f3ea4deddd6').
                    then(response => response.json()).
                    then(json => locationInfo = json);
                if (typeof locationInfo.longitude === 'undefined' || typeof locationInfo.latitude === 'undefined') {
                    throw new Exception;
                }
                try {
                    let origin = new google.maps.LatLng(locationInfo.latitude, locationInfo.longitude);
                    let destination = card.jobData.fields.location;

                    let callback = function(response, status) {
                        if (status == 'OK') {
                            distance = response.rows[0].elements[0].duration.value / 60;
                        }
                        else {
                            console.log("bad")
                        }
                    }

                    service.getDistanceMatrix(
                    {
                        origins: [origin],
                        destinations: [destination],
                        travelMode: google.maps.TravelMode.DRIVING,
                        unitSystem: google.maps.UnitSystem.METRIC,
                        avoidHighways: false,
                        avoidTolls: false,
                    }, callback);
                }
                catch (e) {
                    console.log("Error fetching distance");
                }
            }
            catch (err) {
                console.log("Error fetching location");
            }*/
            if (card.jobData.fields.price >= priceFilter && distance < distanceFilter) {
                switch (typeDrop.selectedIndex) {
                    case 0:
                        cardHolder.append(card.html);
                        break;
                    case 1:
                        if (card.jobData.fields.job_title.toLowerCase().includes("mow")) {
                            cardHolder.append(card.html);
                        }
                        break;
                    case 2:
                        if (card.jobData.fields.job_title.toLowerCase().includes("shovel")) {
                            cardHolder.append(card.html);
                        }
                        break;
                    case 3:
                        if (!card.jobData.fields.job_title.toLowerCase().includes("shovel") && !card.jobData.fields.job_title.toLowerCase().includes("mow")) {
                            cardHolder.append(card.html);
                        }
                        break;
                    default:
                        cardHolder.append(card.html);
                        break;
                }
                
            }
        }
    }
    document.querySelector("#container").append(cardHolder);
}

var distanceDrop = document.getElementById("distance");
var typeDrop = document.getElementById("type");
var payDrop = document.getElementById("pay");

distanceDrop.onclick = updateFilter;
typeDrop.onclick = updateFilter;
payDrop.onclick = updateFilter;

let jobCards = [];
let jobs = JSON.parse(jobData);
for (var job of jobs) {
    if (job.fields.rating == null) {
        let jobCard = generateCard(job);
        document.querySelector("#cardHolder").append(jobCard.html);
        jobCards.push(jobCard);
    }
}

//var service = new google.maps.DistanceMatrixService();
updateFilter();
