fetch(url = 'http://localhost:8000/add/')
    .then(response => {
        return response.json();
    })
    .then(data => {
        console.log(data)
//        for (let i = 0; i < data.length; i++) {
//            let char_data = data[i]
//            let markUp = `<a href="character.html?id=${char_data['char_id']}" id="characterIitem" class="character_item">
//                                <div class="img">
//                                <img src="${char_data['img']}" alt="" />
//                                </div>
//                                <p class="name_label">${char_data['name']}</p>
//                            </a>`
//            $(".characters_block").append(markUp)
//        }
    })