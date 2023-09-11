let characters = document.getElementById('character');



const nameData = fetch("https://swapi-api.hbtn.io/api/people/5/?format=json", {
    method: 'GET',
})
    .then(res => {
        if (res.ok) {
            console.log("Success");
        }else {
            console.log("Error");
        }
    })
    .then(data => console.log(data))


characters.textContent(nameData);