let today = new Date()
// var dd = String(today.getDate()).padStart(2, '0');
// var mm = String(today.getMonth() + 1).padStart(2, '0');
// var yyyy = today.getFullYear();
// // let time = document.querySelectorAll('#time')


// if (mm == 01) {
//     mm = "January"
// } else if (mm == 02) {
//     mm = "February"
// } else if (mm == 03) {
//     mm = "March"
// } else if (mm == 04) {
//     mm = "April"
// } else if (mm == 05) {
//     mm = "May"
// } else if (mm == 06) {
//     mm = "June"
// } else if (mm == 07) {
//     mm = "July"
// } else if (mm == 08) {
//     mm = "August"
// } else if (mm == 09) {
//     mm = "September"
// } else if (mm == 10) {
//     mm = "October"
// } else if (mm == 11) {
//     mm = "November"
// } else if (mm == 12) {
//     mm = "December"
// }

// today = mm + ' ' + dd + ', ' + yyyy;


// let date = document.querySelectorAll('#date')
// dates.push(document.querySelectorAll('#date'))

// alldates.push(date.innerHTML)
let alldates = document.querySelectorAll('#date')


console.log(alldates[0].innerHTML)

for (let i = 0; i < alldates.length; i++) {
    console.log(alldates[i].innerHTML)
}

// function reminder(alldates) {

//     for (let i = 0; i < alldates.length; i++) {
//         if (alldates[i] == ("Start date: " + today)) {
//             console.log("Hello")
//         } else {
//             console.log("woops")
//         }
//     }
// }

// reminder()

// let i = 0; i < dates.length; i++


// var x = document.querySelector('#time')
var x = 30; //minutes interval
var times = []; // time array
var tt = 0; // start time
var ap = ['AM', 'PM']; // AM-PM

//loop to increment the time and push results in array
for (var i = 0; tt < 24 * 60; i++) {
    var hh = Math.floor(tt / 60); // getting hours of day in 0-24 format
    var mm = (tt % 60); // getting minutes of the hour in 0-55 format
    times[i] = ("0" + (hh % 12)).slice(-2) + ':' + ("0" + mm).slice(-2) + ap[Math.floor(hh / 12)]; // pushing data in array in [00:00 - 12:00 AM/PM format]
    tt = tt + x;
}

// console.log(times);

let alltimes = document.querySelectorAll('#time')

for (let i = 0; i < alltimes.length; i++) {
    console.log(alltimes[i].innerHTML)
    if (today.getHours() > 12) {
        var time = (today.getHours() - 12 ) + ":" + today.getMinutes() + ' p.m.';
    } else {
            var time = today.getHours() + ":" + today.getMinutes() + ' a.m.';
        }
    
    console.log(time)
    // var minutes = 1000 * 60;
    // var now = Date.now();
    // if alltimes[i] == Math.round(now / minutes) {
    //     console.log(alltimes)
    // }
    if (alltimes[i].innerHTML == time) {
        console.log('hello')
    }
}
