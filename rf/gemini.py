from manim import *

class RLCResonance(Scene):
    def construct(self):
        # Introduction and Basic Components
        self.intro()
        self.wait(1)

        # Impedance and Frequency Dependence
        self.impedance_frequency()
        self.wait(2)

        # Resonance
        self.resonance()
        self.wait(2)

        # Applications
        self.applications()
        self.wait(2)

        # Conclusion
        self.conclusion()
        self.wait(1)

    def intro(self):
        title = Text("Resonance Unveiled: The Dance of R, L, and C").scale(0.7)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        voltage_source = Line(LEFT * 2, LEFT * 1.5).add_tip()
        voltage_source_plus = Text("+").next_to(voltage_source.get_start(), UP * 0.2)
        voltage_source_minus = Text("-").next_to(voltage_source.get_start(), DOWN * 0.2)
        voltage_source_group = VGroup(voltage_source, voltage_source_plus, voltage_source_minus)

        resistor = Line(LEFT * 1.5, LEFT * 0.5).add_tip()
        resistor_zigzags = VGroup(*[Line(LEFT*1.5 + RIGHT*x*0.1, LEFT*1.5 + RIGHT*(x+0.5)*0.1).rotate(PI/4 if x%2==0 else -PI/4) for x in range(10)])
        resistor_zigzags.move_to(resistor.get_center())
        R_label = Tex("R").next_to(resistor, UP)

        inductor = Line(LEFT * 0.5, RIGHT * 0.5).add_tip()
        inductor_coil = VGroup(*[Arc(0, PI, radius=0.2, start_angle=PI*x/5) for x in range(5)]).move_to(inductor.get_center())
        L_label = Tex("L").next_to(inductor, UP)

        capacitor = Line(RIGHT * 0.5, RIGHT * 1.5).add_tip()
        capacitor_plates = VGroup(Line(RIGHT * 0.5 + UP * 0.3, RIGHT * 0.5 + DOWN * 0.3), Line(RIGHT * 1.5 + UP * 0.3, RIGHT * 1.5 + DOWN * 0.3))
        C_label = Tex("C").next_to(capacitor, UP)

        circuit = VGroup(voltage_source_group, resistor_zigzags, inductor_coil, capacitor_plates).move_to(DOWN*1)

        self.play(Create(voltage_source_group), Write(Tex("Voltage Source").next_to(voltage_source_group, UP)))
        self.wait(0.5)
        self.play(Create(resistor_zigzags), Write(R_label), Write(Tex("Resistor").next_to(resistor_zigzags, UP)))
        self.wait(0.5)
        self.play(Create(inductor_coil), Write(L_label), Write(Tex("Inductor").next_to(inductor_coil, UP)))
        self.wait(0.5)
        self.play(Create(capacitor_plates), Write(C_label), Write(Tex("Capacitor").next_to(capacitor_plates, UP)))
        self.wait(1)
        self.play(circuit.animate.move_to(ORIGIN))

    def impedance_frequency(self):
        self.play(FadeOut(self.mobjects))
        axes = Axes(x_range=[0, 10, 1], y_range=[-10, 10, 2], x_length=8, y_length=6).add_labels(x_labels_config={"num_decimal_places": 0}, y_labels_config={"num_decimal_places": 0})
        axes.shift(DOWN * 1)
        x_label = axes.get_x_axis_label(Tex("Frequency ($\\omega$)"))
        y_label = axes.get_y_axis_label(Tex("Impedance (Z)"))
        self.play(Create(axes), Create(x_label), Create(y_label))

        R_graph = axes.plot(lambda x: 2, x_range=[0, 10], color=RED)
        L_graph = axes.plot(lambda x: x, x_range=[0, 10], color=GREEN)
        C_graph = axes.plot(lambda x: 10 / x if x > 0 else 10, x_range=[0.1, 10], color=BLUE)

        R_label = Tex("R").next_to(R_graph.get_end(), RIGHT)
        L_label = Tex("j$\\omega$L").next_to(L_graph.get_end(), RIGHT)
        C_label = Tex("1/j$\\omega$C").next_to(C_graph.get_end(), RIGHT)

        self.play(Create(R_graph), Write(R_label))
        self.play(Create(L_graph), Write(L_label))
        self.play(Create(C_graph), Write(C_label))

    def resonance(self):
        resonance_point = Dot(self.axes.c2p(3.16, 3.16), color=YELLOW) #3.16 is sqrt(10)
        resonance_frequency = Tex("$\\omega_0 = 1/\\sqrt{LC}$").next_to(resonance_point, UP)
        current_graph_axes = Axes(x_range=[0, 10, 1], y_range=[0, 5, 1], x_length=8, y_length=4).shift(UP*2)
        current_graph = current_graph_axes.plot(lambda x: 4/(abs(x-3.16)+0.5), x_range=[0.1, 10], color=ORANGE)
        self.play(Create(resonance_point), Write(resonance_frequency))
        self.wait(1)
        self.play(Create(current_graph_axes))
        self.play(Create(current_graph))

    def applications(self):
        self.play(FadeOut(self.mobjects))
        radio = ImageMobject("radio.png").scale(0.5) #Replace with your own image
        wireless = ImageMobject("wireless_charging.png").scale(0.5).next_to(radio, DOWN) #Replace with your own image
        oscillator = ImageMobject("oscillator.png").scale(0.5).next_to(wireless, DOWN) #Replace with your own image

        self.play(FadeIn(radio), Write(Text("Radio Tuning").next_to(radio, UP)))
        self.play(FadeIn(wireless), Write(Text("Wireless Charging").next_to(wireless, UP)))
        self.play(FadeIn(oscillator), Write(Text("Oscillator").next_to(oscillator, UP)))

    def conclusion(self):
        self.play(FadeOut(self.mobjects))
        conclusion = Text("Understanding RLC circuits and resonance is essential.").scale(0.6)
        self.play(Write(conclusion))
        self.wait(2)