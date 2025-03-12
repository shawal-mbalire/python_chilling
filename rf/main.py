from manim import *
import os
# Run the script using Manim
if __name__ == "__main__":
    os.system(f"manim -pql {os.path.realpath(__file__)} TurtleIntro")

class TurtleIntro(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Python Turtle", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Code block
        code = '''import turtle

t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()'''
        
        code_block = Code(code_string=code, language="Python").scale(0.9)
        self.play(Create(code_block))
        self.wait(2)

        # Turtle movement visualization
        turtle_path = VMobject().set_color(YELLOW)
        dot = Dot(radius=0.1, color=BLUE).move_to(LEFT * 3)

        self.play(FadeIn(dot))
        self.wait(1)

        path = [
            LEFT * 3,  # Start
            LEFT * 3 + RIGHT * 2,  # Move forward
            LEFT * 3 + RIGHT * 2 + UP * 2,  # Turn left, move forward
        ]

        turtle_path.set_points_as_corners(path)
        self.play(MoveAlongPath(dot, turtle_path), run_time=3)
        self.wait(1)

        # Conclusion
        conclusion = Text("Turtle makes Python fun!", font_size=36).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)

        self.play(FadeOut(title, code_block, dot, turtle_path, conclusion))
