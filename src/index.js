fetch("../Leccion 2/Leccion 2.md").then(response => response.text()).then(content => {
    marked.use(
        markedKatex()
    );

    const contenedor = document.getElementById('rendered')
    contenedor.innerHTML = marked.parse(content);

    document.getElementById("leccion").textContent = "Lección 2";
    document.getElementById("tittle").textContent = "Operaciones fundamentales con vectores y sus propiedades";

    /*
    document.getElementById("leccion").textContent = "Lección 1";
    document.getElementById("tittle").textContent = "Vectores";

    
    */
});