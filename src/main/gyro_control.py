from spike import Motor, ColorSensor, DistanceSensor
from spike.control import wait_for_seconds
from time import sleep_ms

# Hardware Setup
steer = Motor('B')
drive = Motor('D')
floor = ColorSensor('A')
dist = DistanceSensor('C')

# Steering Parameters
CENTER = 2
LEFT = 337
RIGHT = 28
STEER_SPEED = 85

# Real-time P-Steering
X_CENTER = 156
DEADBAND = 8
KP = 0.25
MIN_DELTA = -25.0
MAX_DELTA = 26.0

# Speed Parameters
FAST = 20
SLOW = 12
TURN_SPEED = 18
AVOID_SPEED = 14

# Safety & Distance Limits
OBSTACLE_CM = 48.0
SLOW_CM = 65.0
EMERGENCY_WALL_CM = 18.0

ORANGE_TURNS = ["RIGHT", "RIGHT", "RIGHT", "RIGHT"]

current_steer_state = "UNKNOWN"
obstacle_lock = False

def center_safe():
    global current_steer_state
    if current_steer_state != "CENTER":
        steer.run_to_position(CENTER, "shortest path", STEER_SPEED)
        current_steer_state = "CENTER"

def left():
    global current_steer_state
    if current_steer_state != "LEFT":
        steer.run_to_position(LEFT, "shortest path", STEER_SPEED)
        current_steer_state = "LEFT"

def right():
    global current_steer_state
    if current_steer_state != "RIGHT":
        steer.run_to_position(RIGHT, "shortest path", STEER_SPEED)
        current_steer_state = "RIGHT"

def stop_car():
    drive.stop()
    center_safe()

def real_time_steer(block):
    global current_steer_state
    if block is None:
        center_safe()
        return

    error = block.x - X_CENTER
    if abs(error) <= DEADBAND:
        center_safe()
        return

    delta_theta = error * KP

    if delta_theta < MIN_DELTA:
        delta_theta = MIN_DELTA
    elif delta_theta > MAX_DELTA:
        delta_theta = MAX_DELTA

    target_angle = int((CENTER + delta_theta) % 360)
    steer.run_to_position(target_angle, "shortest path", STEER_SPEED)
    current_steer_state = "P_STEER_" + str(target_angle)

def get_rgb():
    v = floor.get_rgb_intensity()
    if v is None or len(v) < 3:
        return None
    return v[0], v[1], v[2]

def is_blue(v):
    try:
        if floor.get_color() == 'blue':
            return True
    except:
        pass
    if v is None:
        return False
    r, g, b = v[0], v[1], v[2]
    return (b > r * 1.15) and (b > g * 1.08)

def is_orange(v):
    try:
        c = floor.get_color()
        if c in ['red', 'orange']:
            return True
    except:
        pass
    if v is None:
        return False
    r, g, b = v[0], v[1], v[2]
    return (r > b * 1.2) and (r > g * 1.05)

def marker():
    v = get_rgb()
    if is_orange(v):
        return "ORANGE"
    if is_blue(v):
        return "BLUE"
    return None

def orange_turn(n):
    d_wall = dist.get_distance_cm()
    if d_wall is None:
        turn_time = 2.70
    else:
        turn_time = 1.80 + (d_wall / 100.0) * 1.60
        if turn_time < 2.20:
            turn_time = 2.20
        if turn_time > 3.20:
            turn_time = 3.20

    d = ORANGE_TURNS[(n - 1) % len(ORANGE_TURNS)]
    print(">>> DYNAMIC ORANGE TURN:", n, d, "| WALL DIST:", d_wall, "cm -> TIME:", turn_time, "s")

    drive.stop()
    if d == "LEFT":
        left()
    else:
        right()

    drive.start(TURN_SPEED)
    wait_for_seconds(turn_time)

    drive.stop()
    center_safe()
    sleep_ms(100)
    drive.start(FAST)

def avoid(direction):
    global obstacle_lock
    print(">>> EXECUTING TRACK-FITTED DODGE DIR:", direction)
    drive.stop()

    if direction == "RIGHT":
        opp_dir = "LEFT"
    else:
        opp_dir = "RIGHT"

    if direction == "LEFT":
        left()
    else:
        right()
    drive.start(AVOID_SPEED)
    wait_for_seconds(0.38)

    if opp_dir == "LEFT":
        left()
    else:
        right()
    wait_for_seconds(0.35)

    center_safe()
    wait_for_seconds(0.45)

    if opp_dir == "LEFT":
        left()
    else:
        right()
    wait_for_seconds(0.35)

    if direction == "LEFT":
        left()
    else:
        right()
    wait_for_seconds(0.25)

    drive.stop()
    center_safe()
    sleep_ms(50)
    drive.start(FAST)

    obstacle_lock = False

def emergency_wall_avoid():
    print("EMERGENCY: WALL DETECTED NEARBY!")
    drive.stop()
    drive.start(-AVOID_SPEED)
    wait_for_seconds(0.30)
    drive.stop()
    right()
    drive.start(AVOID_SPEED)
    wait_for_seconds(0.40)
    center_safe()
    drive.start(FAST)