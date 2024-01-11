import { GoogleGenerativeAI } from "https://esm.run/@google/generative-ai";

const genAI = new GoogleGenerativeAI("AIzaSyDQ-5w9CkZMk-QOMR3h0Zg93-3ht67q0s0");
const model = genAI.getGenerativeModel({ model: "gemini-pro" });

async function run() {
    marked.use(markedKatex());

    const prompt = document.getElementById("prompt");
    const presentacion = " '**Hola, soy imlargo y soy tu asistente virtual diseñado para explicarte geometría vectorial.**'"
    const notes = "para generar texto latex, usa el simbolo $ antes y despues de la expresion latex"
    const instruction = "Ahora responde la pregunta o explica este texto de un curso de geometria vectorial (Solamente en R2) de manera mas sencilla y facil de entender, deja la idea clara. El texto o pregunta se dara a continuacion"

    const result = await model.generateContentStream(
        `Antes de responder, presentate diciendo: ${presentacion}.
        Nota: ${notes}.
        ${instruction}:
        
        '${prompt.value}'`
    );

    let text = '';
    for await (const chunk of result.stream) {
        const chunkText = chunk.text();
        text += chunkText;
        document.getElementById("output").innerHTML = marked.parse(text);
    }
}

//const button = document.getElementById("generate");
//button.addEventListener("click", run);