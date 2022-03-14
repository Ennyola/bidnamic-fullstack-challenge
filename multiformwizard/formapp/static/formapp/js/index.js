let form = document.querySelector("#customerForm")

let AllBiddingSettings = ["HIGH", "MEDIUM", "LOW"]
form.addEventListener("submit", (e) => {

    let d_o_b = form.elements['d_o_b'].value
    let biddingSettings = form.elements['bd-settings'].value
    let ageError = document.querySelector("#age-error")
    let biddingError = document.querySelector("#bd-error")

    // This ensures any previous error message is cleared
    ageError.innerHTML = ""
    biddingError.innerHTML = ""

    if (new Date().getFullYear() - d_o_b.split("-")[0] < 18) {
        ageError.innerHTML = "Must be 18 or above"
        e.preventDefault()
    }
    if (!AllBiddingSettings.includes(biddingSettings.toUpperCase())) {

        biddingError.innerHTML = "Invalid bidding settings"
        e.preventDefault()
    }


})