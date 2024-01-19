import moderngl as gl
import pygame
import sys
from objects import *
from math import pi


white = (255, 255, 255)
black = (0, 0, 0)
indigo = (75,0,130)
sensi = 1
t=0


class grph_engine:
    def __init__(self, win_size=(1200, 600)) -> None:
        self.win_size = win_size
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION,3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        
        pygame.display.set_mode(self.win_size, flags=pygame.OPENGL | pygame.DOUBLEBUF)
        
        self.ctx = gl.create_context()
        #self.fb = self.ctx.framebuffer()
        #self.fb.depth_mask = True
        
        
        self.clock = pygame.time.Clock()
        
        self.scene = triangle(self)

        self.mx, self.my = 0, 0
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.scene.zbl()
                pygame.quit()
                sys.exit()
        
    def rendering(self):
        self.ctx.clear(color=black)
        self.ctx.enable(gl.DEPTH_TEST | gl.CULL_FACE)
        self.scene.render([(sensi*self.mx), -(sensi*self.my), 0])
        pygame.display.flip()
        
    def run(self):
        global t
        while 1:
            t+=0.1
            self.events()
            rx, ry = pygame.mouse.get_rel()
            self.mx += rx     
            self.my += ry
            self.rendering()

            self.clock.tick(120)
            pygame.display.set_caption("fps: " + str(self.clock.get_fps()) + ";mx :"+ str((self.mx*sensi)))
            #

inst = grph_engine()
inst.run()