const movisList = document.getElementById("list_movies");


fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(res => {
        return res.json();
    })

    .then(data => {
        data.results.forEach(movis => {
            const listItems = document.createElement("li");
            listItems.textContent = movis.title;
            movisList.appendChild(listItems);
        })
    })