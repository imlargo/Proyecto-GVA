function loadLesson(index) {
    fetch("../../src/lessons.json").then(res => res.json())
    .then(lessons => {
        renderLesson(
            index,
            lessons[index]
        )
    })
}

function renderLesson(index, lesson) {
    const path = `../../lessons/lesson-${index}.md`;

    fetch(path).then(response => response.text()).then(content => {
        // Add latex
        marked.use(markedKatex());

        // Custom id
        marked.use(
            {
                renderer: {
                    heading(text, level, raw, slugger) {
                        const headingIdRegex = /(?: +|^)\{#([a-z][\w-]*)\}(?: +|$)/i;
                        const hasId = text.match(headingIdRegex);
                        if (!hasId) {
                            // fallback to original heading renderer
                            return false;
                        }
                        return `<h${level} id="${hasId[1]}">${text.replace(headingIdRegex, '')}</h${level}>\n`;
                    }
                }
            }
        );
    
        // Add badget
        document.getElementById("leccion").textContent = `Leccion ${index}`;

        // Add tittle
        document.getElementById("tittle").textContent = lesson.tittle;

        // Add video url
        document.getElementById("lesson-video").src = lesson.video;

        // Render content
        const contenedor = document.getElementById('rendered')
        contenedor.innerHTML = marked.parse(content);
    });
}