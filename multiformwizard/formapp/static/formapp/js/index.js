let form = document.querySelector("#customerForm")

let AllBiddingSettings = ["HIGH", "MEDIUM", "LOW"]
form.addEventListener("submit", (e) => {

    let d_o_b = form.elements['d_o_b'].value
    let biddingSettings = form.elements['bd-settings'].value

    if (new Date().getFullYear() - d_o_b.split("-")[0] < 18) {
        let error = document.querySelector("#age-error")
        error.innerHTML = "Must be above 18"
        e.preventDefault()
    }
    if (!AllBiddingSettings.includes(biddingSettings.toUpperCase())) {
        let error = document.querySelector("#bd-error")
        error.innerHTML = "Invalid bidding settings"
        e.preventDefault()
    }


})