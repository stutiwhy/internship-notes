/// looping
// for(let i = 2; i<= 10; i += 2){
//     console.log(i)
// }

// for(i = 10; i >= 0; i--){
//     console.log(i)
// }

// for (let i = 0; i <= 10; i += 2){
//     if(i != 0){
//         console.log(i)
//     }
// }

// // for of loop 
// let arr = [1, 2, 3, 4, 5]
// for(let i of arr){
//     console.log(i)
// }

// let obj = {
//     name : 'stuti',
//     age : 17
// }

// // for in loop
// for(let i in obj){
//     console.log(obj[i])
// }

// let i = 0
// while(i != 11){
//     console.log(i)
//     i++
// }

// let i = 1
// do {
//     console.log(i)
//     i++
// } while(i != 11)

// for(let i = 0; i <= 10; i++){
//     if(i == 6)
//         // break // prints 0 - 5
//         continue // prints 0 - 10 except 6
//     console.log(i)
// }

// for(i = 1; i <= ii; i++){
//     for(ii = 1; ii <= 5; ii++){
//         console.log("*")
//     }
//     console.log("\n")
// }

// function add(a, b){
//     return a + b
// }
// c = add( 3, 8)
// console.log(c)

// const add = function(a, b){
//     return a + b
// }
// c = add(3, 8)
// console.count(c)

// const add = (a, b) => {
//     return a + b
// }
// console.log(add(9,4))

// const add = (a, b) => a + b
// console.log(add(3, 8))

// (function add(a, b){
//     console.log(a + b)
// })(3,8)

// let name = prompt("Enter your name : ")
// console.log(`Hello, ${name}`)

// let a = 10 // global variable
// function printing(){
//     let a = 100 // local variable
//     console.log(a)
// }

// // lexical scope
function outer(){
    let a = 100
    function inner(){
        let b = 10
        console.log(a + b)
    }
    inner()
}
// inner()
outer()