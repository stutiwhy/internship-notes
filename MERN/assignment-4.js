// // Question 1
// // Task: Write a function that takes an object and returns an array of the object's keys and values.

// function getKeysAndValues(person) {
//     let person_arr = []
//     for (let k of Object.keys(person)) {
//         person_arr.push([k, person[k]])
//     }
//     return person_arr
// }

// let person = {name : 'Stuti', age : 17, hobby : 'sleep'}

// console.log(getKeysAndValues(person))


// // Question 2
// // Task: Create a function to convert a string to title case.

// function toTitleCase(inp_str) {
//     let str = inp_str.toLowerCase().split(' ')
//     let str_arr = []

//     for (let i of str) {
//         str_arr.push(i.charAt(0).toUpperCase() + i.slice(1))
//     }

//     return str_arr.join(' ')
// }

// console.log(toTitleCase("this is TO TITLE CaSe."))

// // Question 3
// // Task: Implement a function that checks if an object is empty.

// function isObjEmpty(obj) {
//     empty = false
//     if(Object.keys(obj).length == 0)
//         empty = true
//     return empty
// }

// let person = {name : 'Stuti', age : 17, hobby : 'sleep'}
// let not_person = {}

// console.log(isObjEmpty(person))
// console.log(isObjEmpty(not_person))

// // Question 4
// // Task: Write a function to count the number of occurrences of each character in a string.

// function countChars(word) {
//     let char_count = {}
//     for(let i = 0; i < word.length; i++) {
//         let char = word[i]
//         if(char_count[char] != undefined) {
//             char_count[char] += 1
//         } else {
//             char_count[char] = 1
//         }
//     }
//     return char_count
// }

// console.log(countChars("hheeelllllo ssstuuti"))