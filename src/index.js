fetch("../Leccion 1/Leccion 1.md").then(response => response.text()).then(content => {
    marked.use(
        markedKatex()
    );

    const contenedor = document.getElementById('rendered')
    contenedor.innerHTML = marked.parse(content);
});