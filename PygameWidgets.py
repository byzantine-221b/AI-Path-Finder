import pygame
import os
import sys


class Text:
    def __init__(self, name="", text="", align="left", font="calibri", fontsize=12, pos=(0, 0), dim=(0, 0),
                 fg=(0, 0, 0), bg=(255, 255, 255), bg_on=False, bold=False, italic=False, underline=False, wrap=False,
                 visible=True, enabled=True):
        self.name = name
        self.text = text
        self.font = font
        self.fontsize = fontsize
        self.pos = pos
        self.left, self.top = pos
        self.dim = dim
        self.width, self.height = dim
        self.align = align
        self.fg = fg
        self.bg = bg
        self.bg_on = bg_on
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.wrap = wrap
        self.visible = visible
        self.enabled = enabled

    def draw(self, window):
        if self.visible:
            objfont = pygame.font.SysFont(self.font, self.fontsize, self.bold, self.italic)
            objfont.set_underline(self.underline)

            objfont_w, objfont_h = objfont.size(self.text)
            if self.wrap:
                self.width, self.height = self.dim
                line = ""
                sentence = self.text
                objtext = []
                for letter in sentence:
                    temp = line + letter
                    if objfont.size(temp)[0] > self.width:
                        objtext.append(line)
                        line = letter
                    else:
                        line += letter
                else:
                    objtext.append(line)
            else:
                objtext = [self.text]
                if self.width < objfont_w:
                    self.width = objfont_w
                if self.height < objfont_h:
                    self.height = objfont_h

            for i in range(len(objtext)):
                line = objtext[i]
                line_w, line_h = objfont.size(line)
                indent = round(line_h * 1.2) * i
                location = {"left": (self.pos[0], self.pos[1] + indent),
                            "center": (self.pos[0] + round((self.width - objfont_w) // 2), self.pos[1] + indent),
                            "right": (self.pos[0] + self.width - objfont_w, self.pos[1] + indent)}
                if self.bg_on:
                    window.blit(objfont.render(line, True, self.fg, self.bg), location[self.align])
                else:
                    window.blit(objfont.render(line, True, self.fg), location[self.align])


