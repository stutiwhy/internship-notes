// let db = {
//     1 : "data 1",
//     2 : "data 2",
//     3 : "data 3",
//     4 : "data 4",
//     5 : "data 5"
// }

// let dataID = [1, 2, 3, 4, 5, 6, 7, 8]

// function getDataByID(id) {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             if(db[id]){
//                 resolve(`Data of ID ${id} : ${db[id]}`)
//             }
//             else {
//                 reject(`Data of ID ${id} not present.`)
//             }
//         }, 1000)
//     })
// }

// async function asyncCall() {
//     console.log("calling.")
//         for(let i of dataID){
//             try {
//                 let res = await getDataByID(i)
//                 console.log(res)
//             } catch(err) {
//                 console.log(err)
//             }
//     }
// }
// asyncCall()

// dataID.forEach((val) => {
//     getDataByID(val)
//     .then((res) => {
//         console.log(`Data of ID ${val} : ${res}`)
//     })
//     .catch((err) => {
//         console.log(err)
//     })
// })

// async function fetchData() {
//     let fetchAPI = await fetch("https://bored-api.appbrewery.com/random")
//     let res = await fetchAPI.json
//     console.log(fetchAPI)
// }
// fetchData()

// function resolveAfter2Seconds() {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             resolve("resolved.")
//         }, 2000);
//     })
// }
// resolveAfter25Seconds().then((res) => console.log(res))
// async function asyncCall() { 
//     console.log("calling.")
//     const result = await resolveAfter2Seconds()
//     console.log(result)
//     console.log("done.")
// }
// asyncCall()

// function time(msg,n) {
//     setTimeout(() => {
//         console.log(msg)
//     }, n);
// }
// time("hello",3000)
// time("hello",5000)
// time("hello",7000)

// let msg = ['hello1', 'hello2', 'hello3']

// // for(i of msg){
// //     console.log(i)
// // }

// for(i of msg){
//     time = 3000
//     while(time <= 7000){
//         setTimeout(() => {
//             console.log(i)
//         }, time)
//         time += 2000
//     }
// }

let dt1 = document.getElementById("div1")
let start = document.getElementById("start")
let stop = document.getElementById("stop")
let timer

start.addEventListener("click", () => {
    timer = setInterval(() => {
        div1.innerText = new Date().toLocaleTimeString()
    }, 1);
})
stop.addEventListener("click", () => {
    clearInterval(timer)
})
