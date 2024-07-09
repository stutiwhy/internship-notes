// let empty_arr = []

// for(i = 1; i <= 20; i++) 
//     empty_arr.push(i)

// console.log(empty_arr)

// // let double_arr = empty_arr.map((val) => val * 2)
// // console.log(double_arr)

// const doublee = (val) => {
//     return val * 2
// }
// const double_arr_map = empty_arr.map(doublee)
// console.log(double_arr_map)

// let filtered_arr = empty_arr.filter((val) => val % 2 == 0)

// async > promises > callbackhell

async function asyncFunc() {
    console.log(1)
    await new Promise((resolve, reject) => { 
        setTimeout(() => {
            console.log(2)
            resolve()
        }, 1000);
    })
    console.log(3)
    console.log(4)
}
asyncFunc()