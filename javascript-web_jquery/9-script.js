// JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

// - The translation of “hello” must be displayed in the HTML tag DIV#hello


$(document).ready(function(){
    const hellow = $('#hello');
    $.ajax({
        type: 'GET',
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        success: function(data){
            hellow.text(data.hello);
        }
    })
})