// JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header


$(function(){
    let header = $("header");
    const update_header = $("#update_header");

    update_header.click(function(e){
        header.text("New Header!!!")

        console.log(header.text());
    })
})