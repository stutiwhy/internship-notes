// add(30, 27)
// function add(n1, n2){
//     console.log(n1 + n2)
// }

// let arr = [1, 2, 3, 4]
// console.log(arr)

// let emp_arr = [] // created empty array with size 10

// console.log(arr[arr.length - 1])

// arr.forEach((val) => {
//     // console.log(val, val * 2)
//     emp_arr[emp_arr.length] = val * 2
// })

// console.log(emp_arr)

// emp_arr = arr.map((val, index) => {
//     return val * 2
// })

// emp_arr = arr.map((val) => val ** val)
// console.log(emp_arr)

// const arr = [1, 9, 0, 8, 3, 6, 2, 5, 7, 4]
// // let new_arr = arr.filter((val) => val > 4)
// // console.log(new_arr);

// function idk(a, b){
//     if(a > b)
//         return 1
//     else if(a < b)
//         return -1
//     else
//         return 0
// }
// arr.sort(idk)

// let arr = [1, 2, 3, 4]
// // let res = arr.reduce((sum, val) => sum *= val)
// // console.log(res);
// // console.log(arr);

// let bla = arr.slice(1,2)
// console.log(bla);

// let fruits = ['apple', 'banana', 'cherry', 'banana', 'banana']

// let banana = fruits.filter((value) => value == 'banana') 
// console.log(banana)

// let users = [
//     {name : "Stuti", age : 17},
//     {name : "Swara", age : 16}
// ]
// // console.log(users[0].name);

// users.forEach((val, index) => {
//     console.log(val.name);
// })

// let scores = [95, 50, 70, 65, 75]
// console.log(scores.every((val) => val> 90))
// console.log(scores.some((val) => val> 90))

let arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

console.log(arr.forEach((val1) => {
    val1.forEach((val2) => {
        console.log(val2)
    })}))