// JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// - The name must be displayed in the HTML tag DIV#character


$(function(){
    let = character = $('#character');
    $.ajax({
        type: "GET",
        url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
        success: function(data){
            character.text(data.name);
        }
    })
    
})