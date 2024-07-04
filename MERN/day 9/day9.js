console.log("hello world!")

const express = require('express')
const app = express()

app.get('/',(req, res) => {
    res.end('hello world')
    console.log(req.body)
})

app.listen(2125, () => {
    console.log('server is running at http://localhost:2125')
})