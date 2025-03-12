import manim


class MyScene(manim.Scene):
    def construct(self):

        # name = manim.Text("Hello, I am Shawal!",
        #                   font="Comfortaa").to_edge(manim.UL, buff=1)
        # self.play(manim.Create(name))
        # self.wait(1)
        # self.play(name.animate.to_edge(manim.DL, buff=1))
        # self.play(manim.FadeOut(name))

        # circle = manim.Circle()
        # circle.set_fill(manim.PINK, opacity=0.5)

        # square = manim.Square()
        # square.flip(manim.RIGHT)
        # square.rotate(-3 * manim.TAU / 8)

        # self.play(manim.Create(square))
        # self.play(manim.Transform(square, circle))
        # self.play(manim.FadeOut(square))

        # # axes
        # self.wait(1)
        # ax = manim.Axes(x_range=[-3, 3], y_range=[-1, 1])
        # self.play(manim.Create(ax))
        # self.play(manim.FadeOut(ax))

        # # 3d axes
        # ax_3d = manim.ThreeDAxes()
        # self.play(manim.Create(ax_3d))
        # self.play(manim.FadeOut(ax_3d))

        # # getters
        # rect = manim.Rectangle(color=manim.BLUE, height=2,
        #                        width=3).to_corner(manim.UL)
        # circle = manim.Circle(color=manim.RED, radius=1).to_corner(manim.DR)
        # # arrow = manim.Arrow( start=rect.get_bottom(), end=circle.get_top())
        # arrow = manim.always_redraw(lambda: manim.Arrow(
        #     start=rect.get_bottom(), end=circle.get_top()))
        # self.play(manim.Create(rect))
        # self.play(manim.Create(circle))
        # self.play(manim.Create(arrow))

        # self.play(rect.animate.shift(2*manim.RIGHT))
        # self.play(circle.animate.shift(2*manim.UP))
        # self.play(circle.animate.scale(0.5))
        # self.play(rect.animate.rotate(manim.PI/2))
        # self.play(manim.FadeOut(rect), manim.FadeOut(circle), manim.FadeOut(arrow))
        # num = manim.MathTex("ln(2)")
        # box = manim.SurroundingRectangle(
        #     num, color=manim.RED, buff=1
        # )
        # name = manim.Text("natural log!",font="Comfortaa").next_to(box, direction=manim.DOWN)
        # self.play(manim.Create(manim.VGroup(name, num, box)))
        # self.wait(1)
        # self.play(num.animate.move_to(box.get_right()))
        # self.wait(1)
        # self.play(manim.FadeOut(manim.VGroup(name, num, box)))
        
        
        
        
        
        # k = manim.ValueTracker(8.80)
        # num = manim.always_redraw(lambda: manim.MathTex(str(k.get_value())))
        # self.play(manim.FadeIn(num))
        # self.play(k.animate.set_value(2.70), run_time=5,rate_func=manim.smooth)
        # self.wait(1)
        # self.play(k.animate.set_value(3.14), run_time=5,rate_func=manim.linear)
        # self.wait(1)
        
        #graph plot parabola
        import numpy as np
        ax = manim.Axes().add_coordinates()
        curve = ax.plot(lambda x: 2 * np.sin(x), color=manim.DARK_BLUE)
        area = ax.get_area(
            curve,
            x_range=(manim.PI / 2, 3 * manim.PI / 2),
            color=(manim.GREEN_B, manim.GREEN_D),
            opacity=1,
        )

        self.add(ax, curve, area)
        self.play(ax.animate.set_x_range([0, 2 * manim.PI]).set_y_range([-2, 2]) )
        self.wait(1)