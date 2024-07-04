console.log(5 / 0) // cool shit

// try{
//     let result =  idk()
//     console.log(result)
// } catch(e){ 
//     console.log("An error occured : " + e)
// }

// try{
//     let age = -21
//     if(age < 0){
//         throw new RangeError("Age cannot be less than zero.")
//     }
// } catch(r){
//     console.log(r.name + " : " + r.message)
// }

// try{
//     let x = Number(prompt("Enter first number : "))
//     let y = Number(prompt("Enter second number : "))
//     if(x == 0 || y == 0){
//         throw new Error("Numbers should not be zero.")
//     }
// } catch(e){
//     console.log(e.name + " : " + e.message)
// }

// try{
//     let a 
//     if(a == undefined){
//         throw new Error("variable cannot be undefined.")
//     }
//     console.log(a)
// } catch(e){
//     console.log(e.name + " : " + e.message)
// }

// class CustomError extends Error{
//     constructor(msg){
//         super(msg)
//         this.name = this.constructor.name
//     }
// }

// try{
//     let a 
//     if(a == undefined){
//         throw new CustomError("variable cannot be undefined.")
//     }
//     console.log(a)
// } catch(e){
//     console.log(e.name + " : " + e.message)
// }

class IndexOut extends Error{
    constructor(msg){
        super(msg)
        this.name = this.constructor.name
    }
}

let arr = [1, 2, 3]
let index = 3
try{
    if(arr[index] == undefined){
        throw new IndexOut("ArrayIndexOutOfBounds.")
    }
} catch(e){
    console.log(e.name + " : " + e.message)
}