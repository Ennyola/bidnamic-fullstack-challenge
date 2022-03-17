const AllBiddingSettings = ["HIGH", "MEDIUM", "LOW"]
let form = document.querySelector("#customerForm"),
    ageError = document.querySelector("#age-error"),
    biddingError = document.querySelector("#bd-error"),
    googleIDError = document.querySelector("#google_id_error")


// Function gotten from https://www.coditty.com/code/javascript-18-years-validation#:~:text=How%20to%20validate%20that%20user,%2Fdd%20var%20optimizedBirthday%20%3D%20birthday.
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
    let dateOfBirth = form.elements['d_o_b'].value,
        biddingSettings = form.elements['bidding_settings'].value,
        googleID = form.elements['google_id'].value

    // This ensures any previous error message is cleared
    ageError.innerHTML = ""
    biddingError.innerHTML = ""
    googleIDError.innerHTML = ""

    //Returns a validation error if age isn't up to 18
    if (!underAgeValidate(dateOfBirth)) {
        ageError.innerHTML = "Must be 18 or above"
        e.preventDefault()
    }
    //Returns a validation error if bidding settings isn't in the "AllBiddingSettings" array above
    if (!AllBiddingSettings.includes(biddingSettings)) {
        biddingError.innerHTML = "Invalid bidding settings. Please Make sure they are all in uppercase"
        e.preventDefault()
    }
    //Returns a validation error google id isn't a set of 8 integers
    if (googleID.length !== 8) {
        googleIDError.innerHTML = "Google Account ID is a set of 8 Numbers"
        e.preventDefault()
    }
})