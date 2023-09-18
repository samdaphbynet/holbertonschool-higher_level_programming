// JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:

// The <header> element must always have one class: red or green, never both in the same time and never empty.
// If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.


$(function(){
    let header = $("header");
    const toggleHeader = $("#toggle_header");
    toggleHeader.click(function(){
        if (header.hasClass("green")) {
            header.removeClass("green");
            header.addClass("red");
        }
        else {
            header.removeClass("red");
            header.addClass("green");
        }
        console.log(header);
    })
})