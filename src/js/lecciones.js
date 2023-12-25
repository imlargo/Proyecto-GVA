// Render lessons
(async () => {
    const lessonsPath = "../src/lessons.json"
    const lessonContainer = document.getElementById("contenedor-lecciones");
    
    fetch(lessonsPath).then(res => res.json())
        .then(lessons => {
            console.log(lessons);
            const indexs = Object.keys(lessons);
            indexs.forEach(index => {
                lessonContainer.appendChild(newLessonElement(
                    index,
                    lessons[index]
                ))
            })
        })
})();

function newLessonElement(index, lesson) {
    const template = document.createElement('template');
    template.innerHTML = `
    <a class="lesson container rounded-3" href="./lessons/lesson-${index}.html">
        <div class="lesson-card-image">
            <img src="${lesson.img}" alt="">
        </div>
        <div class="lesson-card-info">
            <span class="lesson-card-tittle">${lesson.tittle}</span>
            <span class="lesson-card-description">
            ${lesson.descripcion}
            </span>
            <span>
                <span class="lesson-card-lesson">Leccion ${index}</span>
            </span>
        </div>
    </a>`;

    console.log(template.innerHTML);

    const lessonElement = template.content.children;
    if (lessonElement.length === 1) return lessonElement[0];
    return lessonElement;
}