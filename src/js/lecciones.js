// Render lessons
(async () => {
    const lessonsPath = "../src/lessons.json";
    const lessonContainer = document.getElementById("contenedor-lecciones");
    
    // Fetch lessons data from JSON file
    fetch(lessonsPath)
        .then(res => res.json())
        .then(lessons => {
            console.log(lessons);
            const indexs = Object.keys(lessons);
            
            // Iterate through each lesson and create lesson elements
            indexs.forEach(index => {
                lessonContainer.appendChild(newLessonElement(
                    index,
                    lessons[index]
                ));
            });
        });
})();

// Function to create a new lesson element
/**
 * Creates a new lesson element based on the provided index and lesson data.
 * 
 * @param {string} index - The index of the lesson.
 * @param {object} lesson - The lesson data.
 * @param {string} lesson.img - The image source for the lesson.
 * @param {string} lesson.tittle - The title of the lesson.
 * @param {string} lesson.descripcion - The description of the lesson.
 * @returns {HTMLElement|HTMLElement[]} - The created lesson element(s).
 */
function newLessonElement(index, lesson) {
    const template = document.createElement('template');
    const isFree = index == "1" || index == "2" ? '<span class="insignia-green">Gratis</span>' : '';

    // Create the HTML structure for the lesson element
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
                <span class="insignia-purple">Leccion ${index}</span>
                ${isFree}
            </span>
        </div>
    </a>`;

    console.log(template.innerHTML);

    const lessonElement = template.content.children;
    if (lessonElement.length === 1) return lessonElement[0];
    return lessonElement;
}