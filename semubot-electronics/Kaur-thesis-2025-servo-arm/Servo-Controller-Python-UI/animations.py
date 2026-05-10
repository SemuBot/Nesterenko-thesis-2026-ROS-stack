#Hardcoded animations
#meant to be called within sercom thread 3
#blocking functions

import time
import numpy as np

#animation definitions
# format:  [  detsi-deree postitions uint16 0..1800 | times to finish motion in ms uint16 0..65535 | current limits uint16 in mA 0....10000
#           [(ddeg1, ddeg2, ddeg3, ddeg4, ddeg5,) (c_lim1, c_lim2, c_lim3, c_lim4, c_lim5,) (time_ms1, time_ms2, time_ms3, time_ms4, time_ms5,) debug?, time_to_wait],
#           [--,,--], 
#          ]
#BASICALLY LUT style animations


def animation_init(speedmult=1, debug=0):
    
    init = np.array([
        [900, 900, 900, 900, 900, 3000, 3000, 3000, 3000, 3000, np.uint16(2000/speedmult), np.uint16(2000/speedmult), np.uint16(2000/speedmult), np.uint16(2000/speedmult), np.uint16(2000/speedmult), debug, np.uint16(2000/speedmult)]
        ], dtype=np.uint16)
    
    return init.astype(np.uint16)


def animation_wave(speedmult=1, debug=0):

    anim = np.array([
        [1000, 1200, 900, 900, 900, 3000, 3000, 3000, 3000, 3000, np.uint16(400/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), debug, np.uint16(500/speedmult)],
        [800, 600, 900, 900, 900, 3000, 3000, 3000, 3000, 3000, np.uint16(400/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), debug, np.uint16(500/speedmult)],
        [1000, 1200, 900, 900, 900, 3000, 3000, 3000, 3000, 3000, np.uint16(400/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), debug, np.uint16(500/speedmult)],
        [800, 600, 900, 900, 900, 3000, 3000, 3000, 3000, 3000, np.uint16(400/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(500/speedmult), debug, np.uint16(500/speedmult)],
        [900, 900, 900, 900, 900, 3000, 3000, 3000, 3000, 3000, np.uint16(500/speedmult), np.uint16(500/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), debug, np.uint16(1000/speedmult)]
        ], dtype=np.uint16)
    
    return anim.astype(np.uint16)


def animation_highend(speedmult=1, debug=0):

    anim = np.array([
        [1800, 1800, 900, 900, 900, 3000, 3000, 3000, 3000, 3000, np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), debug, np.uint16(1000/speedmult)],
        [900, 900, 900, 900, 900, 3000, 3000, 3000, 3000, 3000, np.uint16(700/speedmult), np.uint16(700/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), debug, np.uint16(1000/speedmult)]
        ], dtype=np.uint16)
    
    return anim.astype(np.uint16)

def animation_lowend(speedmult=1,  debug=0):

    anim = np.array([
        [10, 10, 900, 900, 900, 1000, 1000, 1000, 1000, 1000, np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), debug, np.uint16(1000/speedmult)],
        [900, 900, 900, 900, 900, 1000, 1000, 1000, 1000, 1000, np.uint16(700/speedmult), np.uint16(700/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), np.uint16(1000/speedmult), debug, np.uint16(1000/speedmult)]
        ], dtype=np.uint16)
    
    return anim.astype(np.uint16)

if __name__ == "__main__":
    print("Wrong file.")
    