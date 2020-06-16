let today = new Date()
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0');
var yyyy = today.getFullYear();
// // let time = document.querySelectorAll('#time')
// moment().format('LT')

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

if (dd == 01) {
    dd = 1
} else if (dd == 02) {
    dd = 2
} else if (dd == 03) {
    dd = 3
} else if (dd == 04) {
    dd = 4
} else if (dd == 05) {
    dd = 5
} else if (dd == 06) {
    dd = 6
} else if (dd == 07) {
    dd = 7
} else if (dd == 08) {
    dd = 8
} else if (dd == 09) {
    dd = 9
}

// today = mm + ' ' + dd + ', ' + yyyy;
// console.log(today)

function compareDates() {
    let alldates = document.querySelectorAll('#date')
    for (let i = 0; i < alldates.length; i++) {
        today = mm + ' ' + dd + ', ' + yyyy;
        console.log(alldates[i].innerHTML)
        if (alldates[i].innerHTML == today) {
            alldates[i].parentElement.classList.add("red")
        } else {
            alldates[i].parentElement.classList.remove("red")
        }
    }
}

function compareTimes() {
    let today = new Date()
    let alltimes = document.querySelectorAll('#time')
    for (let i = 0; i < alltimes.length; i++) {
        console.log(alltimes[i].innerHTML)
        if (today.getHours() > 12) {
            if (today.getMinutes() > 0) {
                var time = (today.getHours() - 12) + ":" + today.getMinutes() + ' p.m.';
            } else {
                var time = (today.getHours() - 12) + " p.m."
            }
        } else {
            if (today.getMinutes() > 0) {
                var time = today.getHours() + ":" + today.getMinutes() + ' a.m.';
            } else {
                var time = today.getHours() + " a.m."
            }

        }
        if (alltimes[i].innerHTML == time) {
            console.log('hello')
        }
    }
}

function nextDose() {
    let increments = document.querySelectorAll('#increments')
    let unit = document.querySelectorAll('#unit')
    let nextDose = document.querySelectorAll('#next_dose')
    let startTime = document.querySelectorAll('#time')

    let upcoming = document.querySelectorAll('#upcoming')
    for (let i = 0; i < unit.length; i++) {
        console.log(Math.floor(parseInt(startTime[i].innerHTML)))
        let today = new Date()

        if (unit[i].innerHTML == "Hours") {
            hours = (today.getHours())
            today = mm + ' ' + dd + ', ' + yyyy
            startDate = document.querySelectorAll('#date')
            let newTime = parseInt(startTime[i].innerHTML, 10) + parseInt(increments[i].innerHTML);
            let futureDose = (newTime + parseInt(increments[i].innerHTML))
            if (startTime[i].innerHTML.includes("p.m.")) {
                newTime = startDate[i].innerHTML + ' ' + newTime + " p.m."
            } else {
                newTime = startDate[i].innerHTML + ' ' + newTime + " a.m."
            }
            txt = document.createTextNode(newTime)
            nextDose[i].appendChild(txt)

            let array = newTime.split(" ")
            let timeIndex = array.length - 2
            console.log(array[timeIndex])  //This returns the hour of the next medication dose, which we'll then use to calculate future doses. 

            // Need to take what's on line 128 and add it to the newTime or futureDose and do it a certain number of times to indicate upcoming doses.  Empty array for time, split increments, and add those two together in the 141 chunk. 

            let upcomingDoses = array[timeIndex]
            for (let j = 0; j < 7; j++) {
                upcomingDoses = parseInt(upcomingDoses, 10) + parseInt(increments[i].innerHTML, 10)
                upcomingDoses = parseInt(upcomingDoses)
                upcomingText = document.createTextNode(upcomingDoses)
                upcoming[i].appendChild(upcomingText)

            }

        } else if (unit[i].innerHTML == "Days") {
            txt = document.createTextNode("Days")
            nextDose[i].appendChild(txt)
        } else if (unit[i].innerHTML == "Month") {
            txt = document.createTextNode("Month")
            nextDose[i].appendChild(txt)
        }
    }
}


compareDates()
compareTimes()
nextDose()


// var dt = new Date();
// dt.setHours(dt.getHours() + 2);

// today.setHours(today.getHours() + increments[i])

 // today = today.setHours(today.getHours() + increments[i].innerHTML)
            // hours = Math.floor(today / 1000 / 60 / 60)
            // console.log(hours)
            // parseInt(today)

            // + parseInt(increments[i].innerHTML)

// function date(newTime) {
            //     let arr = newTime.split(" ")
            //     let time = arr.length - 2
            //     return time
            // }
            // console.log(time)

            //today.getHours - array[timeIndex] + increment


            // let arr = [20, 40, 40, 40],
            //     sum = 0,
            //     result = arr.map(v => sum += v);

            // console.log(result)