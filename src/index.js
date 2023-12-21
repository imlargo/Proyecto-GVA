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


function concierto() {
    // Fecha y hora actual
    const fechaActual = new Date();

    // Fecha y hora objetivo (23 de febrero de 2024 a las 8:00 PM)
    const fechaObjetivo = new Date('2024-02-23T20:00:00');

    // Calcula la diferencia en milisegundos
    const diferenciaEnMilisegundos = fechaObjetivo - fechaActual;

    // Calcula días, horas y minutos
    const dias = Math.floor(diferenciaEnMilisegundos / (1000 * 60 * 60 * 24));
    const horas = Math.floor((diferenciaEnMilisegundos % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutos = Math.floor((diferenciaEnMilisegundos % (1000 * 60 * 60)) / (1000 * 60));

    // Muestra el resultado
    document.getElementById("concierto").textContent = `Faltan ${dias} días, ${horas} horas y ${minutos} minutos hasta el 23 de febrero de 2024 a las 8:00 PM.`
}