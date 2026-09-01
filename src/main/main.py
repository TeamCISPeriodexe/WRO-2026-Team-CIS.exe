import time
from time import sleep_ms
from huskylens import HuskyLens, find_obstacle
import gyro_control as gc

# Target & Run Configuration
GREEN_ID = 1
RED_ID = 2
SWAP_AVOID_LOGIC = False

BLUE_PER_LAP = 4
TARGET_LAPS = 3

BLUE_LOCK = 1000
ORANGE_LOCK = 900
SAFE_TEST = True
TEST_TIMEOUT_S = 180

print("WRO FE CAR V6.1 - REAL-TIME STEERING INTEGRATED")
gc.center_safe()

husky = HuskyLens('E', 9600)
if husky.version is None or not husky.mode_object_recognition():
    gc.stop_car()
    raise RuntimeError("HuskyLens Init Failed")
print("HUSKYLENS READY")

print("GO!")
gc.drive.start(gc.FAST)

lap = 0
orange = 0
blue = 0
last_marker = None
last_marker_ms = 0
last_obstacle_ms = 0
last_known_dir = None
start_ms = time.ticks_ms()

while True:
    now = time.ticks_ms()

    if SAFE_TEST and time.ticks_diff(now, start_ms) >= TEST_TIMEOUT_S * 1000:
        print("SAFE TEST TIMEOUT")
        gc.stop_car()
        break

    if time.ticks_diff(now, start_ms) > 500:
        m = gc.marker()
    else:
        m = None

    if m == "ORANGE":
        if last_marker != "ORANGE" or time.ticks_diff(now, last_marker_ms) > ORANGE_LOCK:
            last_marker = "ORANGE"
            last_marker_ms = now
            orange += 1
            gc.orange_turn(orange)
            continue
    elif m == "BLUE":
        if last_marker != "BLUE" or time.ticks_diff(now, last_marker_ms) > BLUE_LOCK:
            last_marker = "BLUE"
            last_marker_ms = now
            blue += 1
            print("BLUE LAP MARKER:", blue, "/ 4")
            if blue >= BLUE_PER_LAP:
                blue = 0
                lap += 1
                print(">>> LAP COMPLETED:", lap, "/ 3 <<<")
                if lap >= TARGET_LAPS:
                    print("ALL LAPS FINISHED!")
                    gc.stop_car()
                    break
    else:
        last_marker = None

    d = gc.dist.get_distance_cm()

    direction, b = find_obstacle(husky, GREEN_ID, RED_ID, SWAP_AVOID_LOGIC)
    if direction is not None:
        last_known_dir = direction

    if d is not None:
        if d <= gc.EMERGENCY_WALL_CM and not gc.obstacle_lock:
            gc.emergency_wall_avoid()
            continue

        if lap < TARGET_LAPS and d > gc.OBSTACLE_CM and d <= gc.SLOW_CM:
            gc.drive.start(gc.SLOW)
        elif d <= gc.SLOW_CM:
            gc.drive.start(gc.SLOW)
        else:
            gc.drive.start(gc.FAST)

        if lap < TARGET_LAPS and d <= gc.OBSTACLE_CM:
            if (not gc.obstacle_lock) or time.ticks_diff(now, last_obstacle_ms) > 500:
                gc.obstacle_lock = True
                last_obstacle_ms = now

                if direction is not None:
                    target_dir = direction
                elif last_known_dir is not None:
                    target_dir = last_known_dir
                else:
                    target_dir = "LEFT"

                print("OBSTACLE AT:", d, "cm | AVOID DIR:", target_dir)
                gc.avoid(target_dir)
                last_known_dir = None

        elif d > gc.OBSTACLE_CM:
            gc.obstacle_lock = False
            gc.real_time_steer(b)

    else:
        gc.real_time_steer(b)

    sleep_ms(20)