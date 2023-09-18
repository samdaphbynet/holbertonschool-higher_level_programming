// JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

$(function() {
    let header = $("header");
    const add_class = $("#red_header");
    add_class.click(function(){
        header.addClass("red");
    });
});