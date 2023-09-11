// function that add a new <li> element to the list
function addItems() {
    // Find the <ul> element with class my_list
    let my_list = document.querySelector(".my_list");

    // create a new <li> element
    let newItem = document.createElement("li");
    newItem.textContent = "Item";
    // add the new li element to the <ul> element
    my_list.appendChild(newItem);
}

// add a click event listener to the element with id "add_item"
let add_item = document.getElementById("add_item");
add_item.addEventListener("click", addItems);
