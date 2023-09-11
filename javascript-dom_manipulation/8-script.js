// script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML element with id hello
fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then(res => {
        return res.json();
    })
    .then(hello => {
        const hell = `${hello.hello}`;
        document.getElementById("hello").innerText = hell;
    })
    