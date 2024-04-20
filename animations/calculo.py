from manim import *
from numpy import log

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{ragged2e}")

def justifyTex(text):        
    return Tex(text, tex_template=myTemplate, tex_environment="justify")

class MainScene(Scene):
    def resaltar(self, objeto, tiempo, color):
        return ShowPassingFlash(SurroundingRectangle(objeto, color = color, buff = 0.25), run_time=tiempo, time_width=0.2)


    def construct(self):
        self.intro()
        self.part1()
        self.part2()
        self.part3()
        self.part4()
        self.outro()
        self.wait()
        pass
    
    def intro(self):

        titulo = Tex("Actividad 2 Calculo Diferencial.").scale(1.25)
        titulo2 = Tex("Los números primos y el logaritmo.").scale(1.25)

        sep = Line(start=titulo.get_left(), end=titulo.get_right(), color=WHITE, buff=0.5).next_to(titulo, DOWN, buff=0.5)
        aut = Tex(r"Por:\\Mariana Hernandez\\Isabella Ortiz Acosta\\Juan Carlos Largo\\Mariangel Posada").scale(0.8)
        aut.next_to(sep, DOWN, buff=0.5)
        
        self.play(Write(titulo), run_time = 2)
        self.wait(1)
        self.play(Transform(titulo, titulo2), Create(sep), Write(aut), run_time = 2)
        self.wait(4)

        self.play(FadeOut(sep),FadeOut(aut), run_time = 1)
        self.play(FadeOut(titulo), run_time = 1)
        self.wait()
        pass
    
    def outro(self):

        titulo = Tex("Animaciones creadas por Juan Carlos Largo :).")
        titulo2 = Tex("Gracias!.")

        self.play(Write(titulo), run_time = 1)
        self.wait(0.5)
        self.play(Transform(titulo, titulo2))
        self.wait(3)
        pass
    


    def part1(self):
        titulo = Text("Punto #1").scale(0.7)
        
        rawText = r"En un mismo plano cartesiano, haga la gráfica de la función $\pi(n)$ para:\\n $\in$ $\{$1, 2, ..., 10$\}$ y la gráfica de la función f para x $\in$ [0, 10].\\Note que estamos combinando variables discretas y continuas. Describa ambas gráficas."
        pregunta = justifyTex(rawText).scale(0.7)
        
        rawSimpleQuestion = r"$\pi(n)$ : n $\in$ $\{$1, 2, ..., 10$\}$ y $f(x)$ : x $\in$ [0, 10]"
        preguntaSimple = Tex(rawSimpleQuestion).scale(0.7)
        
        self.play(Write(titulo))
        self.play(titulo.animate.next_to(pregunta, UP, buff=0.5))
        self.play(Create(pregunta))
        self.play(titulo.animate.to_corner(UP + LEFT))
        self.wait(2)
        self.play(Transform(pregunta, preguntaSimple))
        self.play(pregunta.animate.next_to(titulo, DOWN, aligned_edge=LEFT), buff=0.4)

        valor1Tex = Tex(r"$f(x)$ y $\pi(x)$ para $x$ $\leq$ 100").scale(0.8).to_corner(DOWN)
        graph = Tex("Holi").scale(1.2).next_to(valor1Tex, UP, buff = 0.2)

        self.wait(2)
        self.play(Create(valor1Tex), FadeIn(graph))
        self.wait(1)
        self.play(self.resaltar(valor1Tex, 1, TEAL_C))
        
        pass
    
    def part2(self):
        titulo = Text("Punto #2").scale(0.7)
        rawText = r"Repita el punto anterior para valores de n y x\\menores o iguales a 100 y 1000 (o más)."
        pregunta = Tex(rawText, tex_template=myTemplate, tex_environment="justify").scale(0.7)

        rawSimpleQuestion = r"Repita el punto anterior para valores de n y x menores o iguales a 100 y 1000."
        preguntaSimple = Tex(rawSimpleQuestion).scale(0.7)
        
        self.play(Write(titulo))
        self.play(titulo.animate.next_to(pregunta, UP, buff=0.5))
        self.play(Create(pregunta))

        self.play(titulo.animate.to_corner(UP + LEFT))
        self.wait(3)
        self.play(Transform(pregunta, preguntaSimple))
        self.play(pregunta.animate.next_to(titulo, DOWN, aligned_edge=LEFT), buff=0.5)

        valor1Tex = Tex(r"$f(x)$ y $\pi(x)$ para $x$ $\leq$ 100").scale(0.8).to_corner(DOWN)
        valor2Tex = Tex(r"$f(x)$ y $\pi(x)$ para $x$ $\leq$ 1000").scale(0.8).to_corner(DOWN)

        graph1 = Tex("Holi").scale(1.2).next_to(valor1Tex, UP, buff = 0.2)
        graph2 = Tex("Holi").scale(1.2).next_to(valor1Tex, UP, buff = 0.2)

        self.wait(1)
        self.play(Create(valor1Tex), FadeIn(graph1))
        self.wait(2)
        self.play(self.resaltar(valor1Tex, 1, TEAL_C))
        self.wait(4)
        self.play(FadeOut(graph1))
        self.play(Transform(valor1Tex, valor2Tex)) 
        self.play(FadeIn(graph2))
        self.play(self.resaltar(valor1Tex, 1, TEAL_C))
        self.wait(4)
        pass
    

    def part3(self):
        titulo = Text("Punto #3").scale(0.7)
        rawText = r"Calcule el cociente $\frac{\pi(x)}{f(x)}$ para x = $2 \cdot 10^{6}$, $2 \cdot 10^{10}$ (o más)\\¿Qué observa? Interprete sus resultados."
        pregunta = Tex(rawText, tex_template=myTemplate, tex_environment="justify").scale(0.7)
        
        rawSimpleQuestion = r"$\frac{\pi(x)}{f(x)}$ para x = $2 \cdot 10^{6}$, $2 \cdot 10^{10}$ (o más)"
        preguntaSimple = Tex(rawSimpleQuestion).scale(0.8)
        
        self.play(Write(titulo))
        self.play(titulo.animate.next_to(pregunta, UP, buff=0.5))
        self.play(Create(pregunta))

        self.play(titulo.animate.to_corner(UP + LEFT))
        self.wait(3)
        self.play(Transform(pregunta, preguntaSimple))
        self.play(pregunta.animate.next_to(titulo, DOWN, aligned_edge=LEFT), buff=0.5)
        self.wait(3)

        # Calculos
        resultadoss = [148933, 1270607, 11078937, 98222287, 882206716]
        cocientes = []

        # Calculo 2 x 10 a la 6, 7, 8
        for x in range(6, 11):

            resultF = (2 * (10 ** x)) / (x * log(10)) + log(2)
            resultPi = resultadoss[x - 6]
            resultDiv = round(resultPi / resultF, 5)
            cocientes.append(resultDiv)

            stringPi = f"\\pi(2 \\cdot 10^{{{x}}}) = \\pi({2 * (10 ** x)}) = {resultPi}"
            textPi = MathTex(stringPi).scale(0.7)

            stringLn = f"f(2 \\cdot 10^{{{x}}}) = \\frac{{2 \\cdot 10^{{{x}}}}}{{\\ln(2 \\cdot 10^{{{x}}})}} = \\frac{{{2 * (10 ** x)}}} {{ {x} \\cdot \\ln(10) + \\ln(2) }} = {resultF}"
            textLn = MathTex(stringLn).scale(0.7).next_to(textPi, DOWN, buff=0.5)
            
            stringCociente = f"\\frac{{\\pi(2 \\cdot 10^{{{x}}})}}{{f(2 \\cdot 10^{{{x}}})}} = {resultDiv}"
            textCociente = MathTex(stringCociente).scale(0.7).next_to(textLn, DOWN, buff=0.5)

            self.play(Create(textPi), Create(textLn), Create(textCociente))
            self.wait(2)

            grupo = VGroup(textPi, textLn, textCociente)
            self.play(FadeOut(grupo))

        # Comparar resultados y sacar conclusiones
        grupo = VGroup()
        prev = pregunta
        buff = 0.6
        for i, resultado in enumerate(cocientes):
            stringCociente = f"\\frac{{\\pi(2 \\cdot 10^{{{i + 6}}})}}{{f(2 \\cdot 10^{{{i + 6}}})}} = {resultado}"
            texCociente = MathTex(stringCociente).scale(0.7).next_to(prev, DOWN, aligned_edge=LEFT, buff=buff)
            buff = 0.3
            prev = texCociente
            grupo.add(texCociente)
            self.play(Create(texCociente))
            pass

        self.wait(2)

        # Conclusion con limites
        limitTex = MathTex(r"\lim_{x \to \infty} \frac{\pi(x)}{f(x)} \approx 1")
        self.play(Create(limitTex))
        self.wait(3)
        self.play(self.resaltar(limitTex, 1, TEAL_C))
        self.wait(5)

        #self.play(FadeOut(grupo))
        
        pass
    

    def part4(self):
        titulo = Text("Punto #4").scale(0.7)
        rawText = r"Use lo aprendido para calcular aproximadamente el orden de magnitud\\del número de números primos menores o iguales a $10^{1000}$."
        pregunta = Tex(rawText, tex_template=myTemplate, tex_environment="justify").scale(0.7)
        
        rawSimpleQuestion = r"Orden de magnitud del número de números primos menores o iguales a $10^{1000}$."
        preguntaSimple = Tex(rawSimpleQuestion).scale(0.7)
        
        self.play(Write(titulo))
        self.play(titulo.animate.next_to(pregunta, UP, buff=0.5))
        self.play(Create(pregunta))

        self.play(titulo.animate.to_corner(UP + LEFT))
        self.wait(3)
        self.play(Transform(pregunta, preguntaSimple))
        self.play(pregunta.animate.next_to(titulo, DOWN, aligned_edge=LEFT), buff=0.5)

        # Considerando que
        limitTex = MathTex(r"\lim_{x \to \infty} \frac{\pi(x)}{f(x)} \approx 1")
        limitText = Tex("Considerando que:").scale(0.8).next_to(limitTex, UP, buff=0.5)
        grupo1 = VGroup(limitTex, limitText)

        aproxTex = MathTex(r"\pi(x) \approx f(x)")
        aproxText = Tex("Para valores grandes de x").scale(0.8).next_to(aproxTex, UP, buff=0.5)
        grupo2 = VGroup(aproxText, aproxTex)
        
        functionF = MathTex(r"f(x) = \frac{x}{\ln(x)}")
        functionText = Tex(r"Cantidad de primos $\approx$ $f(x)$").scale(0.8).next_to(functionF, UP, buff=0.5)
        grupo3 = VGroup(functionText, functionF)

        self.play(Create(grupo1))
        self.wait(4)
        self.play(Transform(grupo1, grupo2))
        self.wait(4)
        self.play(Transform(grupo1, grupo3))
        self.wait(3)
        self.play(self.resaltar(grupo1, 1, TEAL_C))
        self.wait(3)
        self.play(FadeOut(grupo1))

        TeXs = [
            MathTex(r"f(10^{1000}) = \frac{10^{1000}}{\ln(10^{1000})}"),
            MathTex(r"= \frac{10^{1000}}{1000 \cdot \ln(10)}"),
            MathTex(r"= \frac{ 10^{3} \cdot 10^{997} }{1000 \cdot \ln(10)}"),
            MathTex(r"= \frac{ 1000 \cdot 10^{997} }{1000 \cdot \ln(10)}"),
            MathTex(r"= \frac{10^{997}}{\ln(10)}"),
            MathTex(r"= \frac{10}{\ln(10)} \cdot 10^{996}"),
            MathTex(f"\\frac{{{10}}}{{{round(log(10), 5)}}} \\cdot 10^{{{996}}}"),
            MathTex(f"\\approx {round(10/log(10), 5)} \\cdot 10^{{{996}}}")
        ]

        init = TeXs[0]

        self.play(Create(init))
        self.wait(2)
        self.play(self.resaltar(init, 1, TEAL_C))
        self.wait(3)
        for i in range(1, len(TeXs)):
            self.play(Transform(init, TeXs[i]))
            self.wait(2)

        self.play(self.resaltar(init, 1, TEAL_C))
        self.wait(5)
        self.play(FadeOut(init))
        pass
