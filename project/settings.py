from numba import njit
import numpy as np
import glm
import math

#window 
WIN_RES = glm.vec2(900,480)

#chunk
CHUNK_SIZE = 32
H_CHUNK_SIZE = CHUNK_SIZE//2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_SIZE * CHUNK_AREA

#camera 
ASPECT_RATIO = WIN_RES.x/WIN_RES.y
FOV_DEG = 50
V_FOV =glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89.0)

#player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(H_CHUNK_SIZE,H_CHUNK_SIZE,1.5*CHUNK_SIZE)
MOUSE_SENSITIVITY = 0.0008

#colors
BG_COLOR = glm.vec3(0.1,0.16,0.25)