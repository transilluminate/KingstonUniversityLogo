# Author:  Adrian Robinson <a.j.robinson@kingston.ac.uk>
# Date:    08/01/2025
#
# Code:    Unlicense (done on personal time :)
# KU Logo: Copyight (c) Kingston University (kingston.ac.uk)
#
# Creates an animated Kingston University Logo outputting to mp4 video for slides / media (1080p x 60fps)
#
# uses Manim: https://docs.manim.community/en/stable/installation.html
# run with: $ manim -pqh KingstonUniversityLogo.py KingstonUniversityLogo

# required python3 library
from manim import *

class KingstonUniversityLogo(Scene):
    def construct(self):

        # define the KU brand colours
        colourWhite  = "#FFFFFF"
        colourBlack  = "#000000"    # Full Marque
        colourBlue   = "#0092D4"    # Kingston University
        colourYellow = "#FFED00"    # Kingston School of Art
        colourTeal   = "#45B8A9"    # Kingston Business School
        colourOrange = "#F8971D"    # Faculty of Arts and Social Sciences
        colourGreen  = "#62B22F"    # Faculty of Health, Social Care and Education
        colourPurple = "#95549C"    # Faculty of Science, Engineering and Computing

        # options for generating the logo
        logoColour = colourBlue     # select these from above
        textColour = colourWhite
        playGlimmer = True          # True or False
        pauseTime = 2               # 2 seconds seems ok here

        # define the KU square
        backgroundSquare = Square(side_length=3.5, color=logoColour, fill_opacity=1, sheen_factor=0)
        
        # define KU text block
        line1 = Text("Kingston", color=textColour, weight=BOLD, font="Helvetica Neue")
        line2 = Text("University", color=textColour, weight=BOLD, font="Helvetica Neue")
        line3 = Text("London", color=textColour, weight=LIGHT, font="Helvetica Neue")
        textGroup = VGroup(line1,line2,line3)                     # add text to group
        textGroup.arrange(DOWN * 0.2, aligned_edge = LEFT)        # linespaced to be close together and left aligned
        textGroup.shift(0.7 * UP + 0.05  * LEFT)                  # shifted towards top left of KU square
        
        # define the starting animation actions
        animateStart = [
            DrawBorderThenFill(backgroundSquare),                 # animate boundary before filling solid
            FadeIn(textGroup, scale=0.9),                         # slight scale in
        ]
        # play these animations
        self.play(AnimationGroup(*animateStart, lag_ratio=0.65))  # lag to make text appear as box fills

        # optional glimmer (does not look so good with the light colour themes)
        if (playGlimmer == True):
            glimmerSquare = Square(side_length=3.5, color=logoColour, fill_opacity=0, sheen_factor=2)
            self.play(Create(glimmerSquare))                      # add box glimmer with sheen_factor
            self.play(FadeOut(glimmerSquare))                     # fade this out before animateFinish to have a cleaner look
    
        # pause to appreciate the logo :)
        self.wait(pauseTime)

        # define the finishing animations
        animateFinish = [
            FadeOut(backgroundSquare),
            FadeOut(textGroup),
        ]
        # play these animations
        self.play(AnimationGroup(*animateFinish))                 # fade out together
