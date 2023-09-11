// script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then(res => {
        return res.json();
    })
    .then(data => {
            const nameData = `${data.name}`;
            console.log(nameData);

            document.getElementById("character").innerText = nameData;
        });
