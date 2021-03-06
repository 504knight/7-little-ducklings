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
            jobCardInner1.onclick = function() {
                shrinkCard(id);
            };

            let jobTitle = document.createElement("h5");
            jobTitle.setAttribute("class", "card-header");
            jobTitle.textContent = card.jobData.fields.job_title;

            let jobCardInner2 = document.createElement("div");
            jobCardInner2.setAttribute("class", "card-body");

            let progressText = document.createElement("p");
            progressText.setAttribute("class", "card-text text-warning fw-bold");
            progressText.textContent = "- Waiting for customer confirmation -";

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
            jobWin1.textContent = "Anticipated Start Time:";
            jobWin2.textContent = startDate.toLocaleString();
            jobWindow.append(jobWin1);
            jobWindow.append(jobWin2);

            let completeButton = document.createElement("button");
            completeButton.setAttribute("class", "btn btn-secondary mx-2 mt-2");
            completeButton.textContent = "Mark as Complete"
            completeButton.onclick = function() {
                let completeJobURL = `${window.location.origin}/oddjobs/${id}/complete_job`;
                window.location.replace(completeJobURL);
            };

            let cancelButton = document.createElement("button");
            cancelButton.setAttribute("class", "btn btn-danger mx-2 mt-2");
            cancelButton.textContent = "Cancel";
            cancelButton.onclick = function() {
                let cancelJobURL = `${window.location.origin}/oddjobs/${id}/cancel_job`;
                window.location.replace(cancelJobURL);
            };

            jobCardHTML.append(jobCardInner1);
            jobCardInner1.append(jobTitle);
            jobCardInner1.append(jobCardInner2);

            if(card.jobData.fields.completed) {
                jobCardInner2.append(progressText);
            }

            jobCardInner2.append(jobDescription);
            jobCardInner2.append(jobCardInner3);
            jobCardInner3.append(jobCardInner4);
            jobCardInner4.append(jobLocation);
            jobCardInner4.append(jobDuration);
            jobCardInner4.append(jobPay);
            jobCardInner4.append(jobWindow);

            if (!card.jobData.fields.completed) {
                jobCardInner2.append(completeButton);
                jobCardInner2.append(cancelButton);
            }


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

            let progressText = document.createElement("p");
            progressText.setAttribute("class", "card-text text-warning fw-bold");
            progressText.textContent = "- Waiting for customer confirmation -";

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

            if(card.jobData.fields.completed) {
                jobCardInner2.append(progressText);
            }

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

    let progressText = document.createElement("p");
    progressText.setAttribute("class", "card-text text-warning fw-bold");
    progressText.textContent = "- Waiting for customer confirmation -";

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

    if(job.fields.completed) {
        jobCardInner2.append(progressText);
    }

    jobCardInner2.append(jobDuration);
    jobCardInner2.append(jobPay);

    let jobCard = {
        html: jobCardHTML,
        jobData: job
    }

    return jobCard;
}

let jobCards = [];
let jobs = JSON.parse(jobData);
for (var job of jobs) {
    console.log(userID);
    if (job.fields.rating == null && job.fields.worker == userID) {
        console.log("Job should generate")
        let jobCard = generateCard(job);
        document.querySelector("#cardHolder").append(jobCard.html);
        jobCards.push(jobCard);
    }
}