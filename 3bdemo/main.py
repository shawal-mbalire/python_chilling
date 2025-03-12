from manim import *
import os

# run the manim command every time I run the python file
if __name__ == "__main__":
    os.system(f"manim -pql {os.path.realpath(__file__)} MainScene")
    
class MainScene(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        self.add(circle)
        self.add(square)
        
        square.to_corner(UL)