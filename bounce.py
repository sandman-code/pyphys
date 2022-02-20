#!/usr/bin/env python3

import sys, pygame

pygame.init()
fps = 60
clock = pygame.time.Clock()

# Draws the circle
class circle:

    acc = (0, -10)  
    # takes in a number for radius and vector as position
    def __init__(self, rad, pos, vel):
        self.rad = rad
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.vel_x = vel[0]
        self.vel_y = vel[1]

    def update_pos(self, d_time):
        self.pos_x = get_pos(d_time, self.pos_x, self.vel_x)
        self.pos_y = get_pos(d_time, self.pos_y, self.vel_y)

    def update_vel(self, d_time):
        self.vel_x = get_vel(d_time, self.vel_x, self.acc[0])
        self.vel_y = get_vel(d_time, self.vel_y, self.acc[1])


def distance(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def get_vel(d_time, v, a):
    return v + a * d_time

def get_pos(d_time, p, v):
    return p + v * d_time

def collision_sat(obj, x, y):
    if ((obj.pos_x + obj.rad) > x or (obj.pos_x - obj.rad) < 0):
        obj.vel_x = -obj.vel_x
    if((obj.pos_y + obj.rad) > y or (obj.pos_y - obj.rad) < 0):
        obj.vel_y = -obj.vel_y
        
if __name__ == "__main__":
    circ = circle(5, (350,0), (1,0))

    width = 700
    height = 400
    screen = pygame.display.set_mode((width, height))
    
    t_0 = 0

    yellow = (255, 255, 0)
    black = (0,0,0)

    while 1: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)
        pygame.draw.circle(screen, yellow, (circ.pos_x, circ.pos_y), circ.rad)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        
        time = pygame.time.get_ticks()
        circ.update_pos((time - t_0)/1000)
        circ.update_vel((time - t_0)/1000)
        t_0 = time

        collision_sat(circ, width, height)
         
        print(circ.pos_x)
        print(circ.pos_y)
        print(circ.vel_x)
        print(circ.vel_y)
        print(pygame.time.get_ticks())
        clock.tick(fps)
