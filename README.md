# LLM-based BT and FSM Conversion

## Project Overview

This project uses large language models (LLMs) to enable the mutual conversion between behavior trees (BTs) and finite state machines (FSMs). The project focuses on how to use prompt engineering to guide LLMs in understanding, parsing, and generating behavior models in various formats, thereby achieving automated conversion from BT to FSM and from FSM to BT.

Behavior trees and finite state machines are commonly used behavioral modeling methods in robotics control, game AI, and agent decision-making systems. FSMs offer advantages such as intuitive structure and clear state transitions, while BTs are characterized by modularity, strong scalability, and robust hierarchical expression capabilities. This project aims to leverage the semantic understanding and code/structure generation capabilities of LLMs to establish a conversion process between these two behavioral models.

## Project Scope

This project primarily includes the following:

- Implementing bidirectional conversion between BT and FSM using LLM;
- Designing prompt templates for model conversion;
- Providing complete conversion examples;
- Building and curating an open-source behavioral model dataset;
- Building a synthetic behavioral model dataset;
- Conducting experimental analysis of behavioral model conversion performance across different scenarios.

## Features

### 1. BT to FSM Conversion

Given a behavior tree structure, the LLM can analyze the execution logic between nodes and convert it into a finite state machine representation, including:

- State definitions;
- Event definitions;
- State transition conditions;
- Handling of success, failure, or running states;
- Structured FSM output.

### 2. FSM to BT Conversion

Given a finite state machine, the LLM can analyze the transition relationships between states and convert them into a behavior tree structure, including:

- Extraction of behavior nodes;
- Generation of condition nodes;
- Design of control nodes such as Sequence, Fallback, and Parallel;
- Generation of the behavior tree hierarchy.

### 3. Prompt Engineering

The project has designed a variety of prompt templates to enhance the performance of LLMs in behavioral model translation tasks. Prompt design primarily includes:

- Character set;
- Input format constraints;
- Conversion rule descriptions;
- Output format constraints;
- Example-driven prompts;
- Error correction prompts;
- Structural consistency checks.

### 4. Complete conversion example

The project provides a complete example from the input model to the output model, including:

- Basic BT Example；
- Generated FSM example；
- Basic FSM Example;
- Generated BT example;
- Intermediate reasoning process;
- Analysis of Conversion Results.

## Dataset Information

The dataset for this project consists primarily of two parts：

1. Open-source Behavior Models dataset;
2. Synthetic behavioral models dataset.

---

## 1. Open-source behavior models

### Table 1. Information on open-source behavior models

| No. | Scenario | Type | Project Address | Description | Num |
|---:|---|---|---|---|---:|
| 1 | Robot | FSM | [bt_fsm_comparison](https://github.com/ethz-asl/bt_fsm_comparison) | Warehouse robotics project, supporting operations such as movement, gripping and charging etc. | 5 |
| 2 | Robot | FSM | [SMACH Tutorials](https://wiki.ros.org/smach/Tutorials) | General-purpose robotics library. | 20 |
| 3 | Robot | FSM | [unitree_guide](https://github.com/unitreerobotics/unitree_guide)<br>[Cheetah-Software](https://github.com/mit-biomimetics/Cheetah-Software) | Quadruped robots, including the initial state, stationary state, trotting state, balanced state and free state. | 17 |
| 4 | Robot | FSM | [FSM_wall_following](https://github.com/robertandreibarbulescu/FSM_wall_following) | FSM for obstacle avoidance and wall-following in mobile robots primarily comprises the states Wander, WallDetected, FollowWall and Turn. | 1 |
| 5 | Robot | FSM | [fsm_walking_controller](https://neurobionics.github.io/opensourceleg/examples/fsm_walking_controller) | Mechanical leg. | 1 |
| 6 | Robot | FSM | [Robot-Line-Follower](https://github.com/nicholasmiller1/Robot-Line-Follower) | The FSM states for the line-following robot include: FSMCentered, FSMTurnLeft, FSMTurnHardLeft, FSMTurnRight, FSMTurnHardRight, and FSMLos etc. | 1 |
| 7 | Robot | FSM | [Engineer2024_ROS2_Controller](https://gitee.com/familyyao/Engineer2024_ROS2_Controller) | Robotic Arm Controller FSM. | 20 |
| 8 | Robot | BT | [bt_fsm_comparison](https://github.com/ethzasl/bt_fsm_comparison) | Warehouse robots are capable of performing tasks such as moving, picking up, and charging. | 10 |
| 9 | Robot | BT | [nav2_behavior_tree](https://github.com/rosplanning/navigation2/tree/main/nav2_behavior_tree) | ROS2 Nav2 Navigation BT. | 15 |
| 10 | Robot | BT | [py_trees_ros_tutorials](https://github.com/splintered-reality/py_trees_ros_tutorials) | Mobile Robot Obstacle Avoidance BT. | 28 |
| 11 | Robot | BT | [ros2_turtle_bt_tree](https://gitee.com/weibosi/ros2_turtle_bt_tree) | Robot Patrol. | 1 |
| 12 | Robot | BT | [ROS-Behavior-Tree-for-UR-Robot-and-MiR-Platform-Integration](https://github.com/SMAminNP/ROS-Behavior-Tree-for-UR-Robot-and-MiR-Platform-Integration) | Industrial hybrid robot featuring a Universal Robots, UR, robotic arm, a Robotiq gripper, and a MiR mobile robot. | 1 |
| 13 | Robot | BT | [spot_bt_ros](https://github.com/sandialabs/spot_bt_ros) | The Spot quadruped robot includes officially predefined scenarios such as patrol, marker search, and robotic arm operation. | 20 |
| 14 | Robot | BT | [turtlebot3_behavior_demos](https://github.com/seabass/turtlebot3_behavior_demos) | Navigation and Object Search Tasks for Wheeled Mobile Robots. | 21 |
| 15 | Game AI | FSM | [PartoPrey-BT-RL](https://github.com/NUDTQI/PartoPrey-BT-RL) | PartoPrey simulation game: Implement AI logic for feeding, attacking, tracking, and patrolling. | 21 |
| 16 | Game AI | FSM | [limboai](https://github.com/Metsker/limboai)<br>[godot-platformer-statemachine](https://github.com/FlavioFS/godot-platformer-statemachine/tree/master/godot) | A mainstream open-source BT solution for the Godot ecosystem, covering typical game character behaviors such as enemy patrolling, pursuit, attacks, and reactions to damage. | 2 |
| 17 | Game AI | FSM | [cfsm](https://github.com/nhjschulz/cfsm)<br>[sm64](https://gitcode.com/gh_mirrors/sm6/sm64) | Classic Mario FSM, including Mini Mario/Super/Fire/Cloak state switching and various NPC behavior logic. | 97 |
| 18 | Game AI | BT | [PartoPrey-BT-RL](https://github.com/NUDTQI/PartoPrey-BT-RL) | PartoPrey simulation game: Implement AI logic for feeding, attacking, tracking, and patrolling. | 21 |
| 19 | Game AI | BT | [Resident-Evil-2-Behaviour-Tree-System](https://github.com/Jack-Pettigrew/Resident-Evil-2-Behaviour-Tree-System) | The AI logic behind Mr. X's patrols, room searches, player pursuit, and reactions to being hit in Resident Evil 2 Remake. | 39 |
| 20 | Game AI | BT | [limboai](https://github.com/Metsker/limboai)<br>[godot-platformer-state-machine](https://github.com/FlavioFS/godot-platformer-state-machine/tree/master/godot) | A mainstream open-source BT solution for the Godot ecosystem, covering typical game character behaviors such as enemy patrolling, pursuit, attacks, and reactions to damage. | 17 |
| 21 | Game AI | BT | [EnemyBehaviorTreeDemo](https://github.com/HoriK816/EnemyBehaviorTreeDemo) | Enemy AI in 2D Shooter Games. | 11 |

#### Summary of Open-source Behavior Models

| Scenario | Type | Total |
|---|---|---:|
| Robot | FSM | 65 |
| Robot | BT | 96 |
| Game AI | FSM | 120 |
| Game AI | BT | 88 |

---

## 2. Synthetic behavioral models

| Type | Scenario | Generation Setting | Node / Structural Type | Total |
|---|---|---|---|---:|
| BT | Basic symbols | Set the tree depth to 2–10; for each depth, randomly construct 25 B-trees. | Use English letters to represent leaf nodes. The initial number of leaf nodes per level is 3–5, and 3–5 leaf nodes are added for each additional level. Select nodes so that they are evenly distributed, forming a B-tree. | 225 |
| BT | Robot | Set the tree depth to 2–10; for each depth, randomly construct 15 B-trees. | Construct leaf nodes based on the basic behaviors of warehouse robots. The initial number of leaf nodes per level is 3–5, and 3–5 leaf nodes are added for each additional level. Select nodes and arrange them in a uniform distribution to form a BT tree using appropriate behavioral logic. | 135 |
| BT | Game AI | Set the tree depth to 2–10; for each depth, randomly construct 15 B-trees. | Construct leaf nodes based on the fundamental behaviors of the agent AI in the PartoPrey. The initial layer should have 3–5 leaf nodes, and 3–5 leaf nodes should be added with each additional layer. Select nodes and arrange them in a uniform sequence to form a BT using reasonable behavioral logic. | 135 |
| FSM | Basic symbols | The FSMs have 2–26 states and are uniformly distributed, with each state having 1–5 transitions associated with it. | States are represented by English characters, and branch structures, chain structures, and loop structures are evenly distributed within the FSM. | 225 |
| FSM | Robot | FSMs with 2–30 states are uniformly distributed, and each state has 1–8 associated transitions. | Define states and events based on the basic behaviors of warehouse robots, and construct an FSM using sound logic, ensuring that branch structures, chained structures, and loop structures are evenly distributed within the FSM. | 135 |
| FSM | Game AI | FSMs with 2–30 states are uniformly distributed, and each state has 1–8 associated transitions. | Use the basic behaviors of the agent AI in the “Tag” game to construct states and events, and organize them into an FSM using sound logic, ensuring that branching, chained, and looping structures are evenly distributed within the FSM. | 100 |

test.smv is a test case for the NuSMV tool
