// JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

// - All movie titles must be list in the HTML tag UL#list_movies


$(function(){
    let list_movies = $("#list_movies");
    $.ajax({
        type: "GET",
        url: "https://swapi-api.hbtn.io/api/films/?format=json",
        success: function(data) {
            $.map(data.results, function(movie, i) {
                list_movies.append(`<li>${data.results[i].title}</li>`)
            })
        },

        // method 2 
        // success: function(data) {
        //     data.results.forEach(function(movie, i) {
        //         list_movies.append(`<li>${data.results[i].title}</li>`)
        //     })
        // }
        
    })
})