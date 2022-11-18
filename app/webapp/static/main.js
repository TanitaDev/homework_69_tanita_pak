fetch(url = 'http://localhost:8000/add/')
    .then(response => {
        return response.json();
    })
    .then(data => {
        $("#button_add").on('click', function () {
            $("#result_item").text(data['answer'])
        })
    })

fetch(url = 'http://localhost:8000/subtract/')
    .then(response => {
        return response.json();
    })
    .then(data => {
        $("#button_subtract").on('click', function () {
            $("#result_item").text(data['answer'])
        })
    })

fetch(url = 'http://localhost:8000/multiply/')
    .then(response => {
        return response.json();
    })
    .then(data => {
        $("#button_multiply").on('click', function () {
            $("#result_item").text(data['answer'])
        })
    })

fetch(url = 'http://localhost:8000/divide/')
    .then(response => {
        return response.json();
    })
    .then(data => {
        $("#button_divide").on('click', function () {
            $("#result_item").text(data['answer'])
        })
    })
