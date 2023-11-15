from manim import *
from numpy import log

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{ragged2e}")

def justifyTex(text):        
    return Tex(text, tex_template=myTemplate, tex_environment="justify")

class MainnScene(Scene):
    def construct(self):
        #self.intro()
        self.part3()
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
        self.wait(3)

        self.play(FadeOut(sep),FadeOut(aut), run_time = 1)
        self.play(FadeOut(titulo), run_time = 1)
        self.wait()
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
        self.play(Transform(pregunta, preguntaSimple))
        self.play(pregunta.animate.next_to(titulo, DOWN, aligned_edge=LEFT), buff=0.5)
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
        self.play(Transform(pregunta, preguntaSimple))
        self.play(pregunta.animate.next_to(titulo, DOWN, aligned_edge=LEFT), buff=0.5)
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
        self.play(Transform(pregunta, preguntaSimple))
        self.play(pregunta.animate.next_to(titulo, DOWN, aligned_edge=LEFT), buff=0.5)


        # Calculos
        resultadoss = [148933, 1270607, 11078937, 98222287, 882206716]
        # Calculo 2 x 10 a la 6, 7, 8
        for x in range(6, 11):

            resultF = (2 * (10 ** x)) / (x * log(10)) + log(2)
            resultPi = resultadoss[x - 6]
            resultDiv = round(resultPi / resultF, 5)

            stringPi = f"\\pi(2 \\cdot 10^{{{x}}}) = \\pi({2 * (10 ** x)}) = {resultPi}"
            textPi = MathTex(stringPi).scale(0.8)

            stringLn = f"f(2 \\cdot 10^{{{x}}}) = \\frac{{2 \\cdot 10^{{{x}}}}}{{\\ln(2 \\cdot 10^{{{x}}})}} = \\frac{{{2 * (10 ** x)}}} {{ {x} \\cdot \\ln(10) + \\ln(2) }} = {resultF}"
            textLn = MathTex(stringLn).scale(0.8).next_to(textPi, DOWN, buff=0.5)
            
            stringCociente = f"\\frac{{\\pi(2 \\cdot 10^{{{x}}})}}{{f(2 \\cdot 10^{{{x}}})}} = {resultDiv}"
            textCociente = MathTex(stringCociente).scale(0.8).next_to(textLn, DOWN, buff=0.5)

            self.play(Create(textPi), Create(textLn), Create(textCociente))
            self.wait(3)

            grupo = VGroup(textPi, textLn, textCociente)
            self.play(FadeOut(grupo))

        # Calculo 2 x 10 a la 10




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
        self.play(Transform(pregunta, preguntaSimple))
        self.play(pregunta.animate.next_to(titulo, DOWN, aligned_edge=LEFT), buff=0.5)
        pass
