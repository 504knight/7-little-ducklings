var expandCard = function(id) {

}

var generateCard = function(job) {
    let jobCard = document.createElement("div");
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
    jobDuration.textContent = job.start_time;

    let jobPay = document.createElement("p");
    jobPay.setAttribute("class", "card-text");
    jobPay.textContent = job.price;


    jobCard.append(jobCardInner1);
    jobCardInner1.append(jobCardInner2);
    jobCardInner2.append(jobTitle);
    jobCardInner2.append(jobLocation);
    jobCardInner2.append(jobDuration);
    jobCardInner2.append(jobPay);

    return jobCard;
}

let jobCards = [];
jobs.forEach(function(job) {
    jobCard = generateCard(job);
    document.querySelector(".cardHolder").append(jobCard);
    jobCards.push(jobCard);
})