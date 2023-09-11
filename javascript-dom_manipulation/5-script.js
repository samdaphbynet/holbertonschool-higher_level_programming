// Find the element header
let header = document.querySelector("header");

// Find element with id update_header
let update_header = document.getElementById("update_header");

// add event listener for header update
update_header.addEventListener("click", () => {
    header.innerHTML = "New Header!!!";
})
