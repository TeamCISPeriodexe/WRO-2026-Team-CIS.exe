# 

# 

# 

# 

# 

# 

# 

# WRO Future Engineers 2026 - Engineering Journal

# 

# Category: WRO Future Engineers 2026

# Document Status: Initial Template \& Hardware Setup

# 

# Team Name: \[CIS.exe]

# Country: Thailand

# Category: WRO Future Engineers

# 

# 

# 1\. Team Introduction

# 1.1 Team Members

# &#x09;Puttipong Kittichotthaworn

# &#x09;Role: Software Engineer

# &#x09;Responsibilities: MicroPython Programming, HuskyLens AI Vision System, Sensor Calibration, and Navigation Algorithms.

# &#x09;\[Puttipong Kittichotthaworn]

# &#x09;Role: Hardware Engineer

# &#x09;Responsibilities: Mechanical Chassis Design, Steering Mechanism, 3D Component Printing, and Electronics Wiring.

# &#x09;\[Puttipong Kittichotthaworn]

# &#x09;Role: Hardware Engineer

# &#x09;Responsibilities: Mechanical Chassis Design, Steering Mechanism, 3D Component Printing, and Electronics Wiring.

# 

# 1.2 Team Goals \& Motivation

# 1.2 Team Goals \& Motivation

# &#x09;Our primary goal for the WRO Future Engineers 2026 challenge is to develop a fully autonomous vehicle capable of navigating complex field paths using Ackermann steering and vision-based decision making. Driven by our passion for robotics and embedded software engineering, we aimed to implement a sensor fusion strategy combining a Color Sensor, Distance Sensor, and HuskyLens AI Camera.

# &#x09;Through this project, our team strives to master the engineering design process by systematically testing, calibrating, and resolving hardware-software bottlenecks (such as steering angles and timing limits). Our target is to create a robust, adaptable system that consistently completes all 3 laps and parks successfully, while documenting our entire journey open-source on GitHub.

# 

# 2\. Competition \& Field

# 2\. Competition \& Field

# 2.1 Game Overview

# The WRO Future Engineers 2026 challenge requires teams to design, build, and program a fully autonomous vehicle capable of navigating a structured indoor racetrack. The vehicle must make real-time decisions, maintain path stability, avoid obstacle traffic blocks, and complete the designated mission without any external human control or remote signals.

# 2.2 Field Layout \& Specifications

# &#x09;Track Dimensions: The overall field mat measures approximately 3000" mm"×2000" mm" , enclosed by 100" mm"  high outer and inner white walls, creating a driving lane width of 400"-" 500" mm" .

# &#x09;Traffic Markings:

# &#x09;Blue Lines: Transverse lines used to mark sector transitions and count completed laps.

# &#x09;Orange Lines: Directional guide lines placed at corners and turns to signal steering maneuvers.

# &#x09;Parking Zone: A designated rectangular zone marked on the field mat where the vehicle must perform a controlled stop upon mission completion.

# 2.3 Obstacle Rules \& Pillar Logic

# During the Obstacle Challenge, traffic pillars (50" mm"×50" mm"  base, 100"-" 250" mm"  height) are placed randomly along the driving lanes:

# &#x09;Green Pillar (ID 1): The vehicle must identify the color/ID using onboard vision and pass on the LEFT side of the pillar.

# &#x09;Red Pillar (ID 2): The vehicle must identify the color/ID using onboard vision and pass on the RIGHT side of the pillar.

# &#x09;Safety Constraint: Touching, moving, or knocking over any pillar or wall results in point deductions or run invalidation.

# 2.4 Technical Constraints \& Mission Objectives

# &#x09;Autonomous Operation: 100% onboard execution using the LEGO SPIKE Prime hub, Color Sensor, Distance Sensor, and HuskyLens AI Camera.

# &#x09;Ackermann Steering Mandate: The vehicle design must utilize realistic front-wheel Ackermann steering geometry rather than differential drive.

# &#x09;Dimensional Limits: The vehicle dimensions must fit within 300" mm (Length)"×200" mm (Width)"×300" mm (Height)" .

# &#x09;Primary Objectives: Complete 3 consecutive laps accurately, navigate all obstacles successfully, and execute a final parking maneuver in the designated zone.

# 

# 

# 

# 

# 

# 

# 

# 3\. Robot Overview

# 3.1 Design Philosophy

# The core design strategy of our robot centers on modularity, mechanical stability, and high operational reliability. Rather than building a complex or over-engineered frame, we focused on a lightweight, low-center-of-gravity chassis using LEGO Technic structural components. This ensures predictable driving dynamics, minimal structural flex, and rapid maintenance during competition rounds.

# 3.2 Vehicle Architecture \& Drive System

# &#x09;Ackermann Steering Mechanism: The front axle features a true Ackermann steering geometry powered by a dedicated steering motor (Port B). This mechanism ensures that the inner and outer front wheels turn at appropriate relative angles during cornering, drastically reducing tire slip and maintaining precise directional control through sharp turns.

# &#x09;Rear Wheel Drive Train: Propulsion is delivered by a drive motor (Port D) connected directly to the rear axle. Rear-wheel drive provides strong traction and predictable acceleration without interfering with the front steering assembly.

# 

# 

# 

# 

# 

# 

# 3.3 Strategic Sensor Integration

# To execute accurate line-tracking and obstacle avoidance, sensors are positioned to maximize data reliability:

# &#x09;Color Sensor (Port A): Mounted at the lower front chassis facing downward, close to the surface, to instantly detect Orange corner lines and Blue lap markers without interference from ambient light.

# &#x09;Distance Sensor (Port C): Positioned on the front bumper facing directly ahead to trigger the obstacle avoidance state when an object comes within 25 cm.

# &#x09;HuskyLens AI Camera (Port E): Elevated on the upper front frame with a clear field of view to inspect and classify obstacle pillars (Red ID 2 / Green ID 1) as the vehicle approaches.

# 3.4 Key Technical Specifications

# &#x09;Main Controller: LEGO SPIKE Prime Hub

# &#x09;Programming Language: MicroPython

# &#x09;Drive Mechanism: Rear-wheel drive (Port D)

# &#x09;Steering Mechanism: Ackermann geometry front axle (Port B)

# &#x09;Vision System: DFRobot HuskyLens AI Camera (Port E)

# &#x09;Primary Sensors: 1x SPIKE Color Sensor (Port A), 1x SPIKE Distance Sensor (Port C)

# 

# 

# 

# 4\. Mechanical Design

# 4.1 Steering \& Drive System

# &#x09;Steering Mechanism: Ackermann Geometry เพื่อลดการไถลของล้อขณะเลี้ยวโค้ง

# &#x09;Drive Train: มอเตอร์ขับเคลื่อนต่อตรงกับเฟืองล้อหลัง

# 4.2 Vehicle Photos (6-Axis Views)

# (ใส่รูปถ่ายตัวรถในมุมต่างๆ ตามตำแหน่งด้านล่าง)

# &#x09;\[Front View] — รูปถ่ายด้านหน้า 

# &#x09;\[Back View] — รูปถ่ายด้านหลัง

# &#x09;\[Left View] — รูปถ่ายด้านซ้าย

# &#x09;\[Right View] — รูปถ่ายด้านขวา

# &#x09;\[Top View] — รูปถ่ายด้านบน (เห็นการจัดวางสายไฟ)

# &#x09;\[Bottom View] — รูปถ่ายด้านล่าง (เห็นตำแหน่ง Color Sensor)

# 

# 

# 

# 

# 

# 

# 

# 

# 5\. Electronics \& Sensors

# 5.1 Hardware Port Mapping

# Port	Component	Model / Specs	Primary Function / Mission Role

# A	Color Sensor	LEGO SPIKE Color Sensor	Detects RGB values and color intensity for Orange corner lines and Blue lap counter markers.

# B	Steering Motor	LEGO SPIKE Medium Angular Motor	Controls front axle steering angle based on Ackermann geometry.

# C	Distance Sensor	LEGO SPIKE Distance Sensor	Measures frontal clearance distance to obstacle pillars SSs

# D	Drive Motor	LEGO SPIKE Medium Angular Motor	Drives rear axle for vehicle forward and reverse propulsion.

# E	AI Vision Camera	DFRobot HuskyLens	Performs real-time image processing and classification of Red (ID 2) and Green (ID 1) obstacle pillars.

# 

# 

# 

# 5.2 Power \& Communication Architecture

# &#x09;Main Microcontroller: LEGO SPIKE Prime Hub equipped with an ARM Cortex-M4 processor running embedded MicroPython firmware.

# &#x09;Power Supply: Integrated 2100 mAh Li-ion rechargeable battery pack housed inside the SPIKE Prime Hub, providing stable and regulated power distribution to all connected actuators and sensors.

# &#x09;Camera Interface: DFRobot HuskyLens communicates with the SPIKE Prime Hub through Port E via UART serial protocol, transmitting detected object IDs, coordinates, and bounding box dimensions in real-time.

# 5.3 Sensor Placement \& Mounting Rationale

# &#x09;Color Sensor (Port A):

# &#x09;Position: Mounted at the lower center-front chassis, facing downwards with a 5 mm ground clearance.

# &#x09;Rationale: Keeps the optical sensor close to the track surface to eliminate ambient light interference, ensuring high accuracy when distinguishing Orange turn markers and Blue lap-counting lines.

# &#x09;Distance Sensor (Port C):

# &#x09;Position: Mounted on the front bumper, aligned precisely with the vehicle’s central axis.

# &#x09;Rationale: Provides an unobstructed, straight-line conical field of view to reliably detect approaching obstacle pillars without triggering false positives from outer perimeter walls.

# &#x09;HuskyLens AI Camera (Port E):

# &#x09;Position: Elevated on the top front frame with a 15-degree downward pitch angle.

# &#x09;Rationale: Prevents blind spots caused by the front bumper and expands the field of view to classify Red (Right Pass) and Green (Left Pass) pillars well in advance of steering execution.

# 5.4 Wiring Schematic

# (Insert exported hardware wiring diagram image from draw.io or Fritzing here)

# Figure 5.1: Complete System Hardware Wiring Diagram and Port Allocation Schematic.

# 

# 6\. Software Architecture

# 6.1 Control Logic Structure

# โปรแกรมเขียนด้วยภาษา MicroPython บนระบบปฏิบัติการ LEGO SPIKE Prime ทำงานแบบ Loop ควบคุมหลัก:

# 

# 7\. Computer Vision \& AI Integration

# 7.1 HuskyLens Configuration \& Color Training

# The DFRobot HuskyLens is set to Color Recognition mode and calibrated under venue lighting:

# &#x09;Color ID 1 (Green Pillar): Triggers a LEFT bypass steering maneuver.

# &#x09;Color ID 2 (Red Pillar): Triggers a RIGHT bypass steering maneuver.

# 7.2 UART Data Decoding

# The SPIKE Hub reads binary data packets from HuskyLens via Port E at 115,200 baud. The algorithm verifies header bytes (0x55, 0xAA) to extract the detected object ID and update the vehicle state without delaying the main control loop.

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 



