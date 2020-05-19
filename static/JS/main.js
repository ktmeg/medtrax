let today = new Date()
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0');
var yyyy = today.getFullYear();
let time = document.querySelectorAll('#time')


if (mm == 01) {
    mm = "January"
} else if (mm == 02) {
    mm = "February"
} else if (mm == 03) {
    mm = "March"
} else if (mm == 04) {
    mm = "April"
} else if (mm == 05) {
    mm = "May"
} else if (mm == 06) {
    mm = "June"
} else if (mm == 07) {
    mm = "July"
} else if (mm == 08) {
    mm = "August"
} else if (mm == 09) {
    mm = "September"
} else if (mm == 10) {
    mm = "October"
} else if (mm == 11) {
    mm = "November"
} else if (mm == 12) {
    mm = "December"
}

today = mm + ' ' + dd + ', ' + yyyy;


let date = document.querySelectorAll('#date')
let alldates = []

// dates.push(document.querySelectorAll('#date'))

alldates.push(date.innerHTML)
console.log(alldates)

function reminder() {

    for (let i = 0; i < alldates.length; i++) {
        console.log(date)
        if (alldates[i]== ("Start date: " + today)) {
            console.log("Hello")
        } else {
            console.log("woops")
        }
    }
}

reminder()

// let i = 0; i < dates.length; i++