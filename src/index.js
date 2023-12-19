fetch("../Leccion 2/Leccion 2.md").then(response => response.text()).then(content => {
    const contenedor = document.getElementById('rendered')
    contenedor.innerHTML = marked.parse(content);
});