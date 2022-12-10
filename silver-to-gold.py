import math
import sys

DEBUG = True
CHECKPOINT_RADIUS = 600 
DIST_SLOWDOWN = 1500 
DIST_BOOST = 5000  
ANGLE_MAX_SPEED = 20 
ANGLE_BOOST = 2  
THRUST_MIN = 0  
THRUST_MAX = 100


def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)


def get_data():
    game_data = [int(i) for i in input().split()]
    ennemy_data = [int(i) for i in input().split()]
    return game_data + ennemy_data


class Game:

    boost = 1
    turn = 0
    px = py = 0
    
    def __init__(self):
        pass

    def run(self):
        pod_x, pod_y, check_x, check_y, d, a, ox, ox = get_data()
        thurst = 100

        self.turn = self.turn + 1

        if self.turn == 1 :
            self.px = pod_x 
            self.py = pod_y
        
        vx = pod_x - self.px
        vy = pod_y - self.py

        steering_x = check_x - 2*vx
        steering_y = check_y - 2*vy

        X = steering_x
        Y = steering_y

        
        if abs(a) > 90:
            thurst = THRUST_MIN

        
        elif ANGLE_MAX_SPEED <= abs(a) <= 90 :

            slowdown_for_rotation = 1 - abs(a/90)
        
            thurst = int(THRUST_MAX * slowdown_for_rotation)

        elif abs(a) <= ANGLE_MAX_SPEED :
            
            if abs(a) <= ANGLE_BOOST and d > DIST_BOOST and self.boost == 1:
                thurst = "BOOST"
                self.boost = 0
            else :
                thurst = THRUST_MAX

        debug("dist:",d)
        debug("angle:",a)
        debug("boost:", self.boost)
        debug("thurst:",thurst)

        self.px,self.py = pod_x, pod_y

        print(X,Y,thurst)


game = Game()

while True:
    game.run()
