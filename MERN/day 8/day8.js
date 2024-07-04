let header = document.getElementById("header")
// console.log(header)
// let list = document.getElementsByClassName("list")
// console.log(list)
// let div = document.getElementsByTagName("div")
// console.log(div)

// header.innerText = "header"
// let list = document.querySelectorAll(".list")
// console.log(list)

let unorder = document.getElementById("unorder")
let li = document.createElement('li')
li.innerText = "this is a list"
li.style.color = "green"
unorder.appendChild(li)

let btn = document.getElementById("btn")
btn.addEventListener("click",() => {
    console.log("Button clicked.")
})
btn.addEventListener("mouseover",() => {
    console.log("Button hovered.")})

let textelement = document.getElementById("textElement")
let btn1 = document.getElementById("btn1")
btn1.addEventListener("click",() => {
    textelement.innerText = "This is not original text"
    textelement.style.color = "green"
})


let div1 = document.getElementById("div1")
let copy = document.getElementById("copy")
let div2 = document.getElementById("div2")

copy.addEventListener("click",() => {
    div2.innerText = div1.innerText
})