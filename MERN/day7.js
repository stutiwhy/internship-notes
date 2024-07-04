function getData(id, data) {
    setTimeout(() => {
        console.log("Data : " + id)
        if(data)
            data()
    }, 1000)
}

getData(1,() => {
    getData(2, () => {
        getData(3, () => {
            getData(4, () => {
                getData(5, () =>{
                    getData(6)
                })
            })
        })
    })
})