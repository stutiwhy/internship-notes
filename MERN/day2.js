// global scope
// const pi = 3.14

// function areaOfCircle() {
//     // local scope
//     let r = 10
//     return pi * r * r
// }

// a = areaOfCircle()
// console.log("area of circle = " + a)

// const w = 10
// function areaOfRect() {
//     // local scope
//     let h = 13
//     return h * w
// }

// b = areaOfRect()
// console.log("area of rectangle = " + b)

// const half = .5
// function areaOfTriangle() {
//     // local scope
//     let b = 3
//     let h = 7
//     return half * b * h
// }

// c = areaOfTriangle()
// console.log("area of triangle = " + c)

// let a = 23 // int
// let b = 12.3 // float
// let st1 = "stuti" // string
// let st2 = "s" // char
// let bo = true // bool
// let ab // undefined
// let un = undefined // also undefined
// let n = null // null

// // falsy truthy value
// // "", [], {} --> falsy because nothing
// // "sihfkasjf", ["stuti", "stuti2"], {name : "stuti"} --> falsy why

// let arr = [1, 2, 3, 4]
// let obj = {
//     name : "stuti",
//     roll : 72
// }

// function normal() {

// }

// notNormal: () => {
//     pass
// }

// const phone = {
//     iphone : {
//         model : "15",
//         price : 70299
//     },
//     realme : {
//         model : "Note 8",
//         price : 12699
//     },
//     samsung : {
//         model : "A55",
//         price : 24599
//     },
//     motorola : {
//         model : "G4",
//         price : 17999
//     },
//     nokia : {
//         model : "Lumia",
//         price : 15000
//     },
//     pixel : {
//         model : "8 pro",
//         price : 75899
//     }
// }

// console.log(phone.pixel)

// const arr = [1, 2, 3, 4, 5, 6]
// const res = arr.map((x) => x * 2).reduce
// ((sum, x) => sum + x, 0)
// console.log(res)

// const arr = [5, 3, 8, 1, 2, 7]
// const result = arr.filter((x) => x > 3).sort((a, b) => b - a)
// console.log(result)

// const arr = [1, [2, [3, [4, 5]]]]
// const res = arr.flat(Infinity)
// console.log(res)

// const arr1 = [1, 2, 3, 4, 5]
// const arr2 = [6, 7, 8, 9, 0]
// const result = arr1.filter((x) => arr2.includes(x))
// console.log(result)

let age = 10

// if(age >= 18) {
//     console.log("Adult.")
//     if(age >= 21) {
//         console.log("Drinking age.")
//     } else {
//         console.log("Not drinking age.")
//     }
//     if(age >= 100){
//         console.log("Way past expiry date.")
//     }
// } else {
//     console.log("Not adult.")
//     if(age >= 13) {
//         console.log("Teenager.")
//     } else {
//         console.log("Preteen.")
//     }
// }

// age >= 18 ? console.log("Adult"): console.log("Not adult.")

let ch = 8

switch(ch){
    case 1: console.log("1")
    break
    case 2: console.log("2")
    break
    case 3: console.log("3")
    break
    case 4: console.log("4")
    break
    case 5: console.log("5")
    break
    default: console.log("invalid input.")
}