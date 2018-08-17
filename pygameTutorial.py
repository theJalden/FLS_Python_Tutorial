import numpy as np
import pygame as pg
import time

# create a rotating cube
vertexes = np.array([[-1,-1,-1],[-1,-1,1],
                     [-1,1,-1],[-1,1,1],
                     [1,-1,-1],[1,-1,1],
                     [1,1,-1],[1,1,1]])

class Face:
    def __init__(self, points, color):
        self.points = points
        self.color = color
        self.updateZ()

    def updateZ(self):
        global vertexes
        zsum = 0
        for point in self.points:
            zsum += vertexes[point][2]
        self.z_val = zsum / len(vertexes)

edges = [(0,1),
         (0,2),
         (1,3),
         (2,3),
         (0,4),
         (1,5),
         (2,6),
         (3,7),
         (4,5),
         (4,6),
         (5,7),
         (6,7)]

faces = [ Face([1, 5, 7, 3], [0,0,0]),
          Face([2, 3, 7, 6], [255, 0, 0]),
          Face([0, 2, 6, 4], [0, 255, 0]),
          Face([0, 1, 5, 4], [0, 0, 255]),
          Face([0, 1, 3, 2], [255, 255, 0]),
          Face([4, 6, 7, 5], [255, 0, 255])]


num_pts = len(vertexes)

# List of Vertices, Angle -> List of Vertices
# Performs a rotation transformation around the Y-axis
# returns the result of the operation
def rotateY(verts, angle) :
    rot = np.array([[np.cos(angle), 0, np.sin(angle)],
                    [0, 1, 0],
                    [-np.sin(angle), 0, np.cos(angle)]])
    return np.matmul(verts, rot)

# List of Vertices, Angle -> List of Vertices
# Performs a rotation transformation around the X-axis
# returns the result of the operation
def rotateX(verts, angle) :
    rot = np.array([[1, 0, 0],
                    [0,np.cos(angle), -np.sin(angle)],
                    [0,np.sin(angle), np.cos(angle)]])
    return np.matmul(verts, rot)


def run():
    # initialize pygame
    global vertexes
    playing = False
    done = False
    wireframe = False
    pg.init()

    hh = 240
    ww = 240
    disp = pg.display.set_mode((hh, ww))

    # main loop
    while True:
        # Iterate over events
        for ee in pg.event.get():
            if ee.type == pg.QUIT:
                done = True
            if ee.type ==pg.KEYDOWN:
                if ee.key == pg.K_LEFT:
                    vertexes = rotateY(vertexes, np.pi/36)
                elif ee.key == pg.K_RIGHT:
                    vertexes = rotateY(vertexes, -np.pi/36)
                elif ee.key == pg.K_UP:
                    vertexes = rotateX(vertexes, np.pi/36)
                elif ee.key == pg.K_DOWN:
                    vertexes = rotateX(vertexes, -np.pi/36)
                elif ee.key == pg.K_X:
                    wireframe = not wireframe
                elif ee.key == pg.K_SPACE:
                    playing = not playing

        # State Decisions
        if done:
            pg.quit()
            break # out of the main loop
        
        if playing:
            vertexes = rotateY(vertexes, np.pi/100)
            

                    
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

        if wireframe:
            for edge in edges:
                p1 = screen_coords.astype(np.int16)[edge[0]]
                p2 = screen_coords.astype(np.int16)[edge[1]]
                pg.draw.line(disp, [0,0,0], p1, p2, 1)
        else:
            for face in faces:
                face.updateZ()
            import heapq
            # sort a list of faces by face.zval
            

        

        pg.display.flip()

        # sleep, so as not to use every cpu cycle
        time.sleep(.01)
        

if __name__ == "__main__":
    run()
