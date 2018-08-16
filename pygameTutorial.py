import numpy as np
import pygame as pg
import time

# create a rotating cube
vertexes = np.array([[-1,-1,-1],[-1,-1,1],
                     [-1,1,-1],[-1,1,1],
                     [1,-1,-1],[1,-1,1],
                     [1,1,-1],[1,1,1]])

num_pts = len(vertexes)

# List of Vertices, Angle -> List of Vertices
# Performs a rotation transformation around the z-axis
# returns the result of the operation
def rotateY(verts, angle) :
    rot = np.array([[np.cos(angle), 0, np.sin(angle)],
                    [0, 1, 0],
                    [-np.sin(angle), 0, np.cos(angle)]])
    return np.matmul(verts, rot)


def run():
    # initialize pygame
    global vertexes
    pg.init()

    hh = 240
    ww = 240
    disp = pg.display.set_mode((hh, ww))

    # main loop
    while True:
        # Iterate over events
        for ee in pg.event.get():
            if ee.type == pg.QUIT:
                pg.quit()
            if ee.type ==pg.KEYDOWN:
                if ee.key == pg.K_LEFT:
                    vertexes = rotateY(vertexes, np.pi/36)
                elif ee.key == pg.K_RIGHT:
                    vertexes = rotateY(vertexes, -np.pi/36)


        # Draw Screen
        # 1. World -> Cam
        # Camera is 4 units in front of (0, 0, 0)
        cam_coords = vertexes - np.array([0, 0, 4])
        # 2. Cam -> Film
        film_coords = np.zeros((num_pts, 2))
        for ii, vv in enumerate(cam_coords):
            film_coords[ii] = np.array([-vv[0]/vv[2], -vv[1]/vv[2]])

        # 3. Film -> Screen
        screen_coords = np.zeros((num_pts, 2))
        for ii, vv in enumerate(film_coords):
            screen_coords[ii] = np.array([ww*((vv[0]+1)/2),
                                          hh*((1-vv[1])/2)])

        disp.fill((255,255,255))
        for pt in screen_coords.astype(np.int16):
            pg.draw.circle(disp, [0,0,255], pt, 2)

        pg.display.flip()

        # sleep, so as not to use every cpu cycle
        time.sleep(.01)
        

if __name__ == "__main__":
    run()
