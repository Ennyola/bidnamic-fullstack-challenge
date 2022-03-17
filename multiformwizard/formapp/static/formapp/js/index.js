let form = document.querySelector("#customerForm")
let ageError = document.querySelector("#age-error")
let biddingError = document.querySelector("#bd-error")
let googleIDError = document.querySelector("#google_id_error")


let AllBiddingSettings = ["HIGH", "MEDIUM", "LOW"]

function underAgeValidate(birthday) {

    // it will accept two types of format yyyy-mm-dd and yyyy/mm/dd
    let optimizedBirthday = birthday.replace(/-/g, "/");

    //set date based on birthday at 01:00:00 hours GMT+0100 (CET)
    let myBirthday = new Date(optimizedBirthday);

    // set current day on 01:00:00 hours GMT+0100 (CET)
    let currentDate = new Date().toJSON().slice(0, 10) + ' 01:00:00';

    // calculate age comparing current date and birthday
    let myAge = ~~((Date.now(currentDate) - myBirthday) / (31557600000));

    return myAge < 18 ? false : true;
}




form.addEventListener("submit", (e) => {

    let dateOfBirth = form.elements['d_o_b'].value
    let biddingSettings = form.elements['bd-settings'].value
    let googleID = form.elements['google_id'].value


    // This ensures any previous error message is cleared
    ageError.innerHTML = ""
    biddingError.innerHTML = ""
    googleIDError.innerHTML = ""

    if (!underAgeValidate(dateOfBirth)) {
        ageError.innerHTML = "Must be 18 or above"
        e.preventDefault()
    }
    if (!AllBiddingSettings.includes(biddingSettings)) {

        biddingError.innerHTML = "Invalid bidding settings. Please Make sure they are all in uppercase"
        e.preventDefault()
    }
    if (googleID.length !== 8) {
        googleIDError.innerHTML = "Google Account ID is a set of 8 Numbers"
        e.preventDefault()
    }


})