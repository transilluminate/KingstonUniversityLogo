# Author:  Adrian Robinson <a.j.robinson@kingston.ac.uk>
# Date:    08/01/2025
#
# Code:    Unilicense (done on personal time :)
# KU Logo: Copyight Kingston University (kingston.ac.uk)
#
# Creates an animated Kingston University Logo outputting to mp4 video for slides / media (1080p x 60fps)
#
# uses Manim: https://docs.manim.community/en/stable/installation.html
# run with: $ manim -pqh KingstonUniversityLogo_WithTitleText.py KingstonUniversityLogo_WithTitleText

# required python3 library
from manim import *

class KingstonUniversityLogo_WithTitleText(Scene):
    def construct(self):

        # define the KU brand colours
        colourWhite  = "#FFFFFF"
        colourBlack  = "#000000"    # Full Marque
        colourGrey   = "#777777"    # dark grey colour (for footer)
        colourBlue   = "#0092D4"    # Kingston University
        colourYellow = "#FFED00"    # Kingston School of Art
        colourTeal   = "#45B8A9"    # Kingston Business School
        colourOrange = "#F8971D"    # Faculty of Arts and Social Sciences
        colourGreen  = "#62B22F"    # Faculty of Health, Social Care and Education
        colourPurple = "#95549C"    # Faculty of Science, Engineering and Computing

        # options for generating the logo
        logoPlayGlimmer = True           # flicker of white around the KU logo
        logoColour      = colourBlue     # select these from above
        logoTextColour  = colourWhite
        logoPauseTime   = 0              # 2 seconds seems ok here if *only* displaying logo

        # optional text
        playTitleText       = True
        titleText           = "Festival of Learning 2024"
        titleTextColour     = colourWhite
        subtitleText        = "Our Access & Participation Plan in Practice: an Intersectional Approach"
        subtitleTextColour  = colourBlue
        footerText          = "Wednesday 30 October 2024"
        footerTextColour    = colourGrey
        titleTextPauseTime  = 2

        # calculate some widths (total, and usable)
        # The screen is 8 units high with 16:9, with centred coordinates (so divide by 2), and has a 0.5 buffer
        # see: https://docs.devtaoism.com/docs/html/contents/_2_basic_mobjects.html#camera-dimensions
        SCREEN_WIDTH = 8 * (16/9)
        SCENE_WIDTH  = SCREEN_WIDTH - (2 * DEFAULT_MOBJECT_TO_EDGE_BUFFER)

        # define the KU square
        logoBackgroundSquare = Square(side_length=3.5, color=logoColour, fill_opacity=1, sheen_factor=0)
        
        # define KU text block
        logoTextLine1 = Text("Kingston", color=logoTextColour, weight=BOLD, font="Helvetica Neue")
        logoTextLine2 = Text("University", color=logoTextColour, weight=BOLD, font="Helvetica Neue")
        logoTextLine3 = Text("London", color=logoTextColour, weight=LIGHT, font="Helvetica Neue")
        logoTextGroup = VGroup(logoTextLine1,logoTextLine2,logoTextLine3) # add text to group
        logoTextGroup.arrange(DOWN * 0.2, aligned_edge = LEFT)            # linespaced to be close together and left aligned
        logoTextGroup.shift(0.7 * UP + 0.05  * LEFT)                      # shifted towards top left of KU square
        logoObject = VGroup(logoBackgroundSquare,logoTextGroup)           # group objects together

        # define the starting animation actions
        logoAnimateStart = [
            DrawBorderThenFill(logoBackgroundSquare), # animate boundary before filling solid
            FadeIn(logoTextGroup, scale=0.9),         # slight scale in
        ]
        # play these animations
        self.play(LaggedStart(*logoAnimateStart, lag_ratio=0.65))  # lag to make text appear as box fills

        # optional glimmer (does not look so good with the light colour themes)
        # there *is* a Circumscribe function, however, this is a solid colour and I like the sheen factor look
        # https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html
        # gradients could be an option...
        if (logoPlayGlimmer == True):
            logoGlimmerSquare = Square(side_length=3.5, color=logoColour, fill_opacity=0, sheen_factor=0.3)
            self.play(Create(logoGlimmerSquare))                      # add box glimmer with sheen_factor
            self.play(FadeOut(logoGlimmerSquare))                     # fade this out before animateFinish to have a cleaner look
    
        # pause to appreciate the logo :)
        self.wait(logoPauseTime)

        if (playTitleText == True):

            # move logo to top left
            self.play(logoObject.animate.scale(0.5).to_corner(UL))        # move to top left

            # define title text object
            titleTextObject = Text(titleText, color=titleTextColour, font="Helvetica Neue", weight=BOLD)

            # scale this to fit the scene width
            titleTextObject.scale_to_fit_width(SCENE_WIDTH)

            # align this to below the logo (which has moved to the top left)
            titleTextObject.next_to(logoObject,DOWN).align_on_border(LEFT)

            # define subtitle text object
            subtitleTextObject = Text(subtitleText, color=subtitleTextColour, font="Helvetica Neue", weight=LIGHT)

            # scale this to fit the scene width if this overflows
            if (subtitleTextObject.width > SCENE_WIDTH):
                subtitleTextObject.scale_to_fit_width(SCENE_WIDTH)

            # algn this to below the title test object
            subtitleTextObject.next_to(titleTextObject,DOWN).align_on_border(LEFT)

            # define the footer text object
            footerTextObject = Text(footerText, color=footerTextColour, font="Helvetica Neue", weight=LIGHT)

            # resize footer text
            if (footerTextObject.width > SCENE_WIDTH):
                # if the footer text overflows, then resize to fit
                footerTextObject.scale_to_fit_width(SCENE_WIDTH)
            else:
                # otherwise match the font size of the subtitle text
                footerTextObject.scale_to_fit_height(subtitleTextObject.height)

            # move this to the bottom left corner
            footerTextObject.to_corner(DL)

            # define the starting animations
            animateStart = [
                Write(titleTextObject, run_time=1),
                FadeIn(subtitleTextObject),
                FadeIn(footerTextObject)
            ]
            # animate these objects, with a lag so they finish at similar times and looks good
            self.play(LaggedStart(*animateStart, lag_ratio=0.8))

            # brief pause
            self.wait(titleTextPauseTime)

            # define the finishing animations
            animateFinish = [
                Unwrite(titleTextObject, run_time=1, reverse=True),
                FadeOut(subtitleTextObject),
                FadeOut(footerTextObject),
                FadeOut(logoObject),
            ]
            # play these animations
            self.play(AnimationGroup(*animateFinish))
            self.wait(0.2) # allow the unwrite time to finish

        else:

            # define the finishing animations
            animateFinish = [
                FadeOut(logoObject),
            ]
            # play these animations
            self.play(AnimationGroup(*animateFinish))                 # fade out together
