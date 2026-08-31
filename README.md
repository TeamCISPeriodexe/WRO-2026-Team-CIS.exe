

<img width="442" height="413" alt="Screenshot 2026-08-29 211434" src="https://github.com/user-attachments/assets/099787d8-1e56-4f12-98e7-680bc308c1cb" />


WRO Future Engineers 2026 - Engineering Journal

Category: WRO Future Engineers 2026
Document Status: Initial Template & Hardware Setup

Team Name: [CIS.exe]
Country: Thailand
Category: WRO Future Engineers




1. Team Introduction
1.1 Team Members
[thanarat chansamak]
	Role: Hardware Engineer
	Responsibilities: Mechanical Chassis Design, Steering Mechanism, 3D Component Printing, and Electronics Wiring.
	[Sorawit Namwongsa]
	Role: Software Engineer
	Responsibilities: MicroPython Programming, HuskyLens AI Vision System, Sensor Calibration, and Navigation Algorithms.
	[Puttipong Kittichotthaworn]
	Role: Software Engineer
	Responsibilities: MicroPython Programming, HuskyLens AI Vision System, Sensor Calibration, and Navigation Algorithms.

1.2 Team Goals & Motivation
1.2 Team Goals & Motivation
	Our primary goal for the WRO Future Engineers 2026 challenge is to develop a fully autonomous vehicle capable of navigating complex field paths using Ackermann steering and vision-based decision making. Driven by our passion for robotics and embedded software engineering, we aimed to implement a sensor fusion strategy combining a Color Sensor, Distance Sensor, and HuskyLens AI Camera.
	Through this project, our team strives to master the engineering design process by systematically testing, calibrating, and resolving hardware-software bottlenecks (such as steering angles and timing limits). Our target is to create a robust, adaptable system that consistently completes all 3 laps and parks successfully, while documenting our entire journey open-source on GitHub.

2. Competition & Field
2. Competition & Field
2.1 Game Overview
The WRO Future Engineers 2026 challenge requires teams to design, build, and program a fully autonomous vehicle capable of navigating a structured indoor racetrack. The vehicle must make real-time decisions, maintain path stability, avoid obstacle traffic blocks, and complete the designated mission without any external human control or remote signals.
2.2 Field Layout & Specifications
	Track Dimensions: The overall field mat measures approximately 3000" mm"×2000" mm" , enclosed by 100" mm"  high outer and inner white walls, creating a driving lane width of 400"-" 500" mm" .
	Traffic Markings:
	Blue Lines: Transverse lines used to mark sector transitions and count completed laps.
	Orange Lines: Directional guide lines placed at corners and turns to signal steering maneuvers.
	Parking Zone: A designated rectangular zone marked on the field mat where the vehicle must perform a controlled stop upon mission completion.
2.3 Obstacle Rules & Pillar Logic
During the Obstacle Challenge, traffic pillars (50" mm"×50" mm"  base, 100"-" 250" mm"  height) are placed randomly along the driving lanes:
	Green Pillar (ID 1): The vehicle must identify the color/ID using onboard vision and pass on the LEFT side of the pillar.
	Red Pillar (ID 2): The vehicle must identify the color/ID using onboard vision and pass on the RIGHT side of the pillar.
	Safety Constraint: Touching, moving, or knocking over any pillar or wall results in point deductions or run invalidation.
2.4 Technical Constraints & Mission Objectives
	Autonomous Operation: 100% onboard execution using the LEGO SPIKE Prime hub, Color Sensor, Distance Sensor, and HuskyLens AI Camera.
	Ackermann Steering Mandate: The vehicle design must utilize realistic front-wheel Ackermann steering geometry rather than differential drive.
	Dimensional Limits: The vehicle dimensions must fit within 300" mm (Length)"×200" mm (Width)"×300" mm (Height)" .
	Primary Objectives: Complete 3 consecutive laps accurately, navigate all obstacles successfully, and execute a final parking maneuver in the designated zone.







3. Robot Overview
3.1 Design Philosophy
The core design strategy of our robot centers on modularity, mechanical stability, and high operational reliability. Rather than building a complex or over-engineered frame, we focused on a lightweight, low-center-of-gravity chassis using LEGO Technic structural components. This ensures predictable driving dynamics, minimal structural flex, and rapid maintenance during competition rounds.
3.2 Vehicle Architecture & Drive System
	Ackermann Steering Mechanism: The front axle features a true Ackermann steering geometry powered by a dedicated steering motor (Port B). This mechanism ensures that the inner and outer front wheels turn at appropriate relative angles during cornering, drastically reducing tire slip and maintaining precise directional control through sharp turns.
	Rear Wheel Drive Train: Propulsion is delivered by a drive motor (Port D) connected directly to the rear axle. Rear-wheel drive provides strong traction and predictable acceleration without interfering with the front steering assembly.






3.3 Strategic Sensor Integration
To execute accurate line-tracking and obstacle avoidance, sensors are positioned to maximize data reliability:
	Color Sensor (Port A): Mounted at the lower front chassis facing downward, close to the surface, to instantly detect Orange corner lines and Blue lap markers without interference from ambient light.
	Distance Sensor (Port C): Positioned on the front bumper facing directly ahead to trigger the obstacle avoidance state when an object comes within 25 cm.
	HuskyLens AI Camera (Port E): Elevated on the upper front frame with a clear field of view to inspect and classify obstacle pillars (Red ID 2 / Green ID 1) as the vehicle approaches.
3.4 Key Technical Specifications
	Main Controller: LEGO SPIKE Prime Hub
	Programming Language: MicroPython
	Drive Mechanism: Rear-wheel drive (Port D)
	Steering Mechanism: Ackermann geometry front axle (Port B)
	Vision System: DFRobot HuskyLens AI Camera (Port E)
	Primary Sensors: 1x SPIKE Color Sensor (Port A), 1x SPIKE Distance Sensor (Port C)



4. Mechanical Design
4.1 Steering & Drive System
	Steering Mechanism: Ackermann Geometry เพื่อลดการไถลของล้อขณะเลี้ยวโค้ง
	Drive Train: มอเตอร์ขับเคลื่อนต่อตรงกับเฟืองล้อหลัง
4.2 Vehicle Photos (6-Axis Views)
(ใส่รูปถ่ายตัวรถในมุมต่างๆ ตามตำแหน่งด้านล่าง)
	[Front View] — รูปถ่ายด้านหน้า
<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/d59f58d2-8e83-41b2-ae9d-0a88f793d09e" />

	[Back View] — รูปถ่ายด้านหลัง
<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/d3f52923-5123-4cff-af48-4de36add21e4" />

	[Left View] — รูปถ่ายด้านซ้าย
<img width="2048" height="1536" alt="image" src="https://github.com/user-attachments/assets/8e3eb4c2-5f66-4709-9eac-5c9e77db2ac1" />

	[Right View] — รูปถ่ายด้านขวา
<img width="2048" height="1536" alt="image" src="https://github.com/user-attachments/assets/bee6e1d1-aaa5-4cb8-8be9-263e0ac518bd" />

	[Top View] — รูปถ่ายด้านบน (เห็นการจัดวางสายไฟ)
<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/3ddca024-9a70-4c44-98d2-fabb07cd4666" />

	[Bottom View] — รูปถ่ายด้านล่าง (เห็นตำแหน่ง Color Sensor)
<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/0b0ee73c-b49a-4667-bd77-9e77fc4c64da" />


5. Electronics & Sensors
5.1 Hardware Port Mapping
Port	Component	Model / Specs	Primary Function / Mission Role
A	Color Sensor	LEGO SPIKE Color Sensor	Detects RGB values and color intensity for Orange corner lines and Blue lap counter markers.
B	Steering Motor	LEGO SPIKE Medium Angular Motor	Controls front axle steering angle based on Ackermann geometry.
C	Distance Sensor	LEGO SPIKE Distance Sensor	Measures frontal clearance distance to obstacle pillars SSs
D	Drive Motor	LEGO SPIKE Medium Angular Motor	Drives rear axle for vehicle forward and reverse propulsion.
E	AI Vision Camera	DFRobot HuskyLens	Performs real-time image processing and classification of Red (ID 2) and Green (ID 1) obstacle pillars.


5.2 Power & Communication Architecture
	Main Microcontroller: LEGO SPIKE Prime Hub equipped with an ARM Cortex-M4 processor running embedded MicroPython firmware.
	Power Supply: Integrated 2100 mAh Li-ion rechargeable battery pack housed inside the SPIKE Prime Hub, providing stable and regulated power distribution to all connected actuators and sensors.
	Camera Interface: DFRobot HuskyLens communicates with the SPIKE Prime Hub through Port E via UART serial protocol, transmitting detected object IDs, coordinates, and bounding box dimensions in real-time.
5.3 Sensor Placement & Mounting Rationale
	Color Sensor (Port A):
	Position: Mounted at the lower center-front chassis, facing downwards with a 5 mm ground clearance.
	Rationale: Keeps the optical sensor close to the track surface to eliminate ambient light interference, ensuring high accuracy when distinguishing Orange turn markers and Blue lap-counting lines.
	Distance Sensor (Port C):
	Position: Mounted on the front bumper, aligned precisely with the vehicle’s central axis.
	Rationale: Provides an unobstructed, straight-line conical field of view to reliably detect approaching obstacle pillars without triggering false positives from outer perimeter walls.
	HuskyLens AI Camera (Port E):
	Position: Elevated on the top front frame with a 15-degree downward pitch angle.
	Rationale: Prevents blind spots caused by the front bumper and expands the field of view to classify Red (Right Pass) and Green (Left Pass) pillars well in advance of steering execution.
5.4 Wiring Schematic
(Insert exported hardware wiring diagram image from draw.io or Fritzing here)
Figure 5.1: Complete System Hardware Wiring Diagram and Port Allocation Schematic.


6.Key Components Used
The robot system integrates the operation of the main processing unit, positional sensors, drive mechanisms, and an AI vision processing camera, categorized into the following key components:

6.1 LEGO SPIKE Prime Large Hub (Main Controller)

<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/3b2fa273-933d-4826-9789-48e307887146" />

Device Name: LEGO SPIKE Prime Large Hub

Role and Function: Serves as the Main Processing Unit to run the MicroPython program. It processes data from all sensors, controls the steering direction, manages drive motor speeds, and communicates with the HuskyLens camera.

Key Features Used on the Field:

Built-in 6-axis Gyro Sensor (IMU): Reads orientation angles (Yaw Angle) for the Gyro Control algorithm, allowing the robot to drive precisely straight along the track.

6 Multi-function Ports (A–F): Connects devices according to the robot's Port Mapping (Port A: Color Sensor, Port B: Steering Motor, Port C: Distance Sensor, Port D: Drive Motor, Port E: HuskyLens UART).

MicroPython Execution: Supports high-speed loop processing, enabling real-time sensor reading and immediate, lag-free obstacle response.

6.2 LEGO SPIKE Prime Distance Sensor (Port C)

<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/61ab8054-1613-4838-a463-81446ca28860" />

Device Name: LEGO SPIKE Prime Distance Sensor (Ultrasonic Sensor)

Role and Function: Measures the distance to objects directly in front of the robot using ultrasonic waves. It serves as the primary trigger for detecting obstacles (pillars) along the race track.

Key Features Used on the Field:

Obstacle Detection Threshold: Continuously monitors the front path with a distance threshold of 35.0 cm (OBSTACLE_CM).

Avoidance State Trigger: When an object is detected within 35.0 cm, it immediately signals the system to read the HuskyLens AI camera and execute the dodge maneuver.

Non-blocking Distance Checking: Reads real-time distance data via dist.get_distance_cm() without delaying the main control loop.

6.3 LEGO SPIKE Prime Color Sensor (Port A)

<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/b42349ae-01b2-4880-b0ac-c2bc0d6a8d8f" />

Device Name: LEGO SPIKE Prime Color Sensor

Role and Function: Positioned facing downward toward the track surface to read ground colors. It acts as the primary navigation sensor for corner detection, lap counting, and track boundary safety.

Key Features Used on the Field:

Cornering Trigger: Continuously scans ground colors to detect the orange line (ORANGE), triggering the autonomous cornering sequence.

Turn Exit & Lap Counter: Detects the blue line (BLUE) to confirm the end of a turn, lock the new Gyro target heading, and increment the lap counter (lap_count).

Track Boundary Recovery: Detects green lines (GREEN) along track boundaries for emergency path correction to prevent the robot from driving off-course.

6.4 LEGO SPIKE Prime Medium Angular Motor – Drive (Port D)

<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/8e0495f7-cb0e-4a37-a6b2-13e6f6867f97" />

Device Name: LEGO SPIKE Prime Medium Angular Motor (Drive)

Role and Function: Powers the main drive axle to propel the robot forward with dynamic speed management across different navigation states.

Key Features Used on the Field:

Dynamic Speed Control: Adjusts power dynamically according to active states (Cruise Speed: 15%, Obstacle Avoidance: 11%, Cornering: 12%).

Precise Execution: Responds instantly to stop commands upon completing 3 full laps (lap_count >= 3).

6.5 LEGO SPIKE Prime Medium Angular Motor – Steering (Port B)

<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/b1951947-e961-4fbd-9ca7-981e9c89a8e5" />


Device Name: LEGO SPIKE Prime Medium Angular Motor (Steering)

Role and Function: Drives the front steering mechanism, providing precise angular adjustments for vehicle turning and directional alignment.

Key Features Used on the Field:

Absolute Encoder Positioning: Allows precise steering angle calibration for straight driving and sharp cornering (Center = 2, Max Left = 337, Max Right = 28).

State-Locked Steering Control: Uses efficient positioning functions (center_safe(), left_max(), right_max()) to eliminate redundant motor commands and minimize system response time.


7. Computer Vision & AI Integration
7.1 HuskyLens Configuration & Color Training
The DFRobot HuskyLens is set to Color Recognition mode and calibrated under venue lighting:
	Color ID 1 (Green Pillar): Triggers a LEFT bypass steering maneuver.
	Color ID 2 (Red Pillar): Triggers a RIGHT bypass steering maneuver.
7.2 UART Data Decoding
The SPIKE Hub reads binary data packets from HuskyLens via Port E at 115,200 baud. The algorithm verifies header bytes (0x55, 0xAA) to extract the detected object ID and update the vehicle state without delaying the main control loop.

















