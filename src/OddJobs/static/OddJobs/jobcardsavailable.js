var expandCard = function(id) {
    jobCards.forEach(function(card) {
        if (card.jobData.id === id) {
            const cardHTML = document.getElementById(id);
            cardHTML.remove();

            let jobCardHTML = document.createElement("div");
            jobCard.setAttribute("id", card.jobData.id);
            jobCard.setAttribute("class", "col-lg-4 mt-3 mt-lg-0");

            let jobCardInner1 = document.createElement("div");
            jobCardInner1.setAttribute("class", "card");

            let jobCardInner2 = document.createElement("div");
            jobCardInner2.setAttribute("class", "card-body");

            let jobTitle = document.createElement("h3");
            jobTitle.setAttribute("class", "h4 card-title");
            jobTitle.textContent = card.jobData.jobTitle;

            let jobDescription = document.createElement("p");
            jobDescription.setAttribute("class", "card-text");
            jobDescription.textContent = card.jobData.job_description;

            let jobLocation = document.createElement("p");
            jobLocation.setAttribute("class", "card-text");
            jobLocation.textContent = card.jobData.location;

            let jobDuration = document.createElement("p");
            jobDuration.setAttribute("class", "card-text");
            jobDuration.textContent = card.jobData.duration;

            let jobPay = document.createElement("p");
            jobPay.setAttribute("class", "card-text");
            jobPay.textContent = card.jobData.price;

            let jobWindow = document.createElement("p");
            jobWindow.setAttribute("class", "card-text");
            jobWindow.textContent = "Preferred Window: " + card.jobData.start_time + " to " + card.jobData.end_time;


            jobCardHTML.append(jobCardInner1);
            jobCardInner1.append(jobCardInner2);
            jobCardInner2.append(jobTitle);
            jobCardInner2.append(jobLocation);
            jobCardInner2.append(jobDuration);
            jobCardInner2.append(jobPay);

            card.html = jobCardHTML;
            document.querySelector(".cardHolder").append(jobCardHTML);
        }
    })
}

var generateCard = function(job) {
    let jobCardHTML = document.createElement("div");
    jobCard.setAttribute("id", job.id);
    jobCard.setAttribute("class", "col-lg-4 mt-3 mt-lg-0");

    let jobCardInner1 = document.createElement("div");
    jobCardInner1.setAttribute("class", "card");
    jobCardInner1.addEventListener("click", expandCard(job.id))

    let jobCardInner2 = document.createElement("div");
    jobCardInner2.setAttribute("class", "card-body");

    let jobTitle = document.createElement("h3");
    jobTitle.setAttribute("class", "h4 card-title");
    jobTitle.textContent = job.jobTitle;

    let jobLocation = document.createElement("p");
    jobLocation.setAttribute("class", "card-text");
    jobLocation.textContent = job.location;

    let jobDuration = document.createElement("p");
    jobDuration.setAttribute("class", "card-text");
    jobDuration.textContent = job.duration;

    let jobPay = document.createElement("p");
    jobPay.setAttribute("class", "card-text");
    jobPay.textContent = job.price;


    jobCardHTML.append(jobCardInner1);
    jobCardInner1.append(jobCardInner2);
    jobCardInner2.append(jobTitle);
    jobCardInner2.append(jobLocation);
    jobCardInner2.append(jobDuration);
    jobCardInner2.append(jobPay);

    let jobCard = {
        html: jobCardHTML,
        jobData: job
    }

    return jobCard;
}

let jobCards = [];
jobs.forEach(function(job) {
    jobCard = generateCard(job);
    document.querySelector("#cardHolder").append(jobCard.html);
    jobCards.push(jobCard);
})