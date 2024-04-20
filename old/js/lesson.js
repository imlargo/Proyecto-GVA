/**
 * Loads a lesson from the lessons.json file and renders it.
 * @param {number} index - The index of the lesson to load.
 */
function loadLesson(index) {
    // Fetch the lessons.json file
    fetch("../../src/lessons.json")
        .then(res => res.json())
        .then(lessons => {
            console.log("Lecciones");
            console.log(lessons);
            // Render the lesson with the given index
            renderLesson(index, lessons[index]);
        })
        .catch(error => {
            console.error("Error al cargar las lecciones:", error);
        });
}

// Function to render a lesson
/**
 * Renders a lesson by fetching the lesson markdown file, adding LaTeX support to the markdown renderer,
 * customizing the heading renderer to add custom IDs, adding a badge indicating the lesson index,
 * adding the title and video URL of the lesson, and rendering the lesson content.
 * 
 * @param {number} index - The index of the lesson.
 * @param {object} lesson - The lesson object containing the title and video URL.
 */
function renderLesson(index, lesson) {
    // Construct the path to the lesson markdown file
    const path = `../../lessons/lesson-${index}.md`;

    // Fetch the lesson markdown file
    fetch(path)
        .then(response => response.text())
        .then(content => {
            // Add LaTeX support to the markdown renderer
            marked.use(markedKatex());

            // Customize the heading renderer to add custom IDs
            marked.use({
                renderer: {
                    heading(text, level, raw, slugger) {
                        const headingIdRegex = /(?: +|^)\{#([a-z][\w-]*)\}(?: +|$)/i;
                        const hasId = text.match(headingIdRegex);
                        if (!hasId) {
                            // Fallback to the original heading renderer
                            return false;
                        }
                        return `<h${level} id="${hasId[1]}">${text.replace(headingIdRegex, '')}</h${level}>\n`;
                    }
                }
            });

            // Add badge indicating the lesson index
            document.getElementById("leccion").textContent = `Leccion ${index}`;

            // Add title of the lesson
            document.getElementById("tittle").textContent = lesson.title;

            // Add video URL of the lesson
            document.getElementById("lesson-video").src = lesson.video;

            // Render the lesson content
            const contenedor = document.getElementById('rendered');
            contenedor.innerHTML = marked.parse(content);
        })
        .catch(error => {
            console.error("Error al renderizar la lección:", error);
        });
}