from manim import *

#Aqui empieza la aventura
#---------------------------------------------------#
#Proyecto GVA:
#Creado por @imlargo
#...................................................


class Intro(Scene):

    def construct(self):
        #---Presentacion---
        self.inicio()

    def inicio(self):
        titulo = Tex("GVA")
        subtitulo = Tex("Creado por: Juan Carlos Largo")    
        self.play(Write(titulo))
        self.play(titulo.animate.next_to(subtitulo, UP, buff=0.5))
        self.play(FadeIn(subtitulo))
        self.wait(3)