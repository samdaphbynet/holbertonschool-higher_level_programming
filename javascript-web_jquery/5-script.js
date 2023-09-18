// Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:
// - The new element must be: <li>Item</li>
// - The new element must be added to UL.my_list


$(function(){
    let add_item = $('#add_item');
    let my_list = $(".my_list");

    add_item.click(function(){
        my_list.append('<li>Item</li>');
        console.log(my_list.children)
    });
});