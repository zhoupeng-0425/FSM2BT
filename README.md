# LLM-based BT and FSM Conversion

## 项目简介

本项目基于大语言模型（Large Language Models, LLMs）实现行为树（Behavior Tree, BT）与有限状态机（Finite State Machine, FSM）之间的相互转换。项目重点研究如何利用提示词工程（Prompt Engineering）引导 LLM 理解、解析和生成不同形式的行为模型，从而完成 BT 到 FSM、FSM 到 BT 的自动化转换。

行为树和有限状态机是机器人控制、游戏 AI、智能体决策系统中常用的行为建模方法。FSM 具有结构直观、状态转移明确等优点，而 BT 具有模块化、可扩展性强和层次化表达能力强等特点。本项目尝试利用 LLM 的语义理解与代码/结构生成能力，在两种行为模型之间建立转换流程。

## 项目内容

本项目主要包含以下内容：

- 使用 LLM 实现 BT 与 FSM 的双向转换；
- 设计用于模型转换的提示词模板；
- 提供完整的转换示例；
- 构建并整理开源行为模型数据集；
- 构建合成行为模型数据集；
- 对不同场景下的行为模型转换效果进行实验分析。

## 功能特性

### 1. BT 到 FSM 转换

给定一个行为树结构，LLM 能够分析节点之间的执行逻辑，并将其转换为有限状态机表示，包括：

- 状态定义；
- 初始状态；
- 状态转移条件；
- 成功、失败或运行状态处理；
- FSM 的结构化输出。

### 2. FSM 到 BT 转换

给定一个有限状态机，LLM 能够分析状态之间的转移关系，并将其转换为行为树结构，包括：

- 行为节点提取；
- 条件节点生成；
- Sequence、Fallback、Parallel 等控制节点设计；
- 行为树层级结构生成。

### 3. 提示词工程

项目设计了多种提示词模板，用于提升 LLM 在行为模型转换任务中的表现。提示词设计主要包括：

- 角色设定；
- 输入格式约束；
- 转换规则说明；
- 输出格式限制；
- 示例驱动提示；
- 错误修正提示；
- 结构一致性检查。

### 4. 完整转换实例

项目提供了从输入模型到输出模型的完整示例，包括：

- 原始 BT 示例；
- 生成的 FSM 示例；
- 原始 FSM 示例；
- 生成的 BT 示例；
- 中间推理过程；
- 转换结果分析。

## 数据集信息

本项目的数据集主要包括两部分：

1. 开源行为模型数据集；
2. 合成行为模型数据集。

---

## 1. 开源行为模型数据集

下表展示了从开源项目中收集的行为模型信息。
<h3>Table 1. Information on Open-source Behavior Models</h3>

<table>
  <thead>
    <tr>
      <th>No.</th>
      <th>Scenario</th>
      <th>Type</th>
      <th>Project Address</th>
      <th>Description</th>
      <th>Num</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <!-- Robot / FSM -->
    <tr>
      <td>1</td>
      <td rowspan="14">Robot</td>
      <td rowspan="7">FSM</td>
      <td>
        <a href="https://github.com/ethz-asl/bt_fsm_comparison">https://github.com/ethz-asl/bt_fsm_comparison</a>
      </td>
      <td>
        Warehouse robotics project, supporting operations such as movement, gripping and charging etc.
      </td>
      <td>5</td>
      <td rowspan="7">65</td>
    </tr>
    <tr>
      <td>2</td>
      <td>
        <a href="https://wiki.ros.org/smach/Tutorials">https://wiki.ros.org/smach/Tutorials</a>
      </td>
      <td>
        General-purpose robotics library.
      </td>
      <td>20</td>
    </tr>
    <tr>
      <td>3</td>
      <td>
        <a href="https://github.com/unitreerobotics/unitree_guide">https://github.com/unitreerobotics/unitree_guide</a><br>
        <a href="https://github.com/mit-biomimetics/Cheetah-Software">https://github.com/mit-biomimetics/Cheetah-Software</a>
      </td>
      <td>
        Quadruped robots, including the initial state, stationary state, trotting state, balanced state and free state.
      </td>
      <td>17</td>
    </tr>
    <tr>
      <td>4</td>
      <td>
        <a href="https://github.com/robertandreibarbulescu/FSM_wall_following">https://github.com/robertandreibarbulescu/FSM_wall_following</a>
      </td>
      <td>
        FSM for obstacle avoidance and wall-following in mobile robots primarily comprises the states Wander, WallDetected, FollowWall and Turn.
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>
        <a href="https://neurobionics.github.io/opensourceleg/examples/fsm_walking_controller">https://neurobionics.github.io/opensourceleg/examples/fsm_walking_controller</a>
      </td>
      <td>
        Mechanical leg.
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>
        <a href="https://github.com/nicholasmiller1/Robot-Line-Follower">https://github.com/nicholasmiller1/Robot-Line-Follower</a>
      </td>
      <td>
        The FSM states for the line-following robot include: FSMCentered, FSMTurnLeft, FSMTurnHardLeft, FSMTurnRight, FSMTurnHardRight, and FSMLos etc.
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>7</td>
      <td>
        https://lonelyranger1@gitee.com/familyyao/Engineer2024_ROS2_Controller
      </td>
      <td>
        Robotic Arm Controller FSM.
      </td>
      <td>20</td>
    </tr>

    <!-- Robot / BT -->
    <tr>
      <td>8</td>
      <td rowspan="7">BT</td>
      <td>
        <a href="https://github.com/ethzasl/bt_fsm_comparison">https://github.com/ethzasl/bt_fsm_comparison</a>
      </td>
      <td>
        Warehouse robots are capable of performing tasks such as moving, picking up, and charging.
      </td>
      <td>10</td>
      <td rowspan="7">96</td>
    </tr>
    <tr>
      <td>9</td>
      <td>
        <a href="https://github.com/ros-planning/navigation2/tree/main/nav2_behavior_tree">https://github.com/ros-planning/navigation2/tree/main/nav2_behavior_tree</a>
      </td>
      <td>
        ROS2 Nav2 Navigation BT.
      </td>
      <td>15</td>
    </tr>
    <tr>
      <td>10</td>
      <td>
        <a href="https://github.com/splintered-reality/py_trees_ros_tutorials">https://github.com/splintered-reality/py_trees_ros_tutorials</a>
      </td>
      <td>
        Mobile Robot Obstacle Avoidance BT.
      </td>
      <td>28</td>
    </tr>
    <tr>
      <td>11</td>
      <td>
        <a href="https://gitee.com/weibosi/ros2_turtle_bt_tree">https://gitee.com/weibosi/ros2_turtle_bt_tree</a>
      </td>
      <td>
        Robot Patrol.
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>12</td>
      <td>
        <a href="https://github.com/SMAminNP/ROS-Behavior-Tree-for-UR-Robot-and-MiR-Platform-Integration">https://github.com/SMAminNP/ROS-Behavior-Tree-for-UR-Robot-and-MiR-Platform-Integration</a>
      </td>
      <td>
        Industrial hybrid robot featuring a Universal Robots (UR) robotic arm, a Robotiq gripper, and a MiR mobile robot.
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>13</td>
      <td>
        <a href="https://github.com/sandialabs/spot_bt_ros">https://github.com/sandialabs/spot_bt_ros</a>
      </td>
      <td>
        The Spot quadruped robot includes officially predefined scenarios such as patrol, marker search, and robotic arm operation.
      </td>
      <td>20</td>
    </tr>
    <tr>
      <td>14</td>
      <td>
        <a href="https://github.com/seabass/turtlebot3_behavior_demos">https://github.com/seabass/turtlebot3_behavior_demos</a>
      </td>
      <td>
        Navigation and Object Search Tasks for Wheeled Mobile Robots.
      </td>
      <td>21</td>
    </tr>

    <!-- Game AI / FSM -->
    <tr>
      <td>15</td>
      <td rowspan="7">Game AI</td>
      <td rowspan="3">FSM</td>
      <td>
        <a href="https://github.com/NUDTQI/PartoPrey-BT-RL">https://github.com/NUDTQI/PartoPrey-BT-RL</a>
      </td>
      <td>
        PartoPrey simulation game: Implement AI logic for feeding, attacking, tracking, and patrolling.
      </td>
      <td>21</td>
      <td rowspan="3">120</td>
    </tr>
    <tr>
      <td>16</td>
      <td>
        <a href="https://github.com/Metsker/limboai">https://github.com/Metsker/limboai</a><br>
        <a href="https://github.com/FlavioFS/godot-platformer-statemachine/tree/master/godot">https://github.com/FlavioFS/godot-platformer-statemachine/tree/master/godot</a>
      </td>
      <td>
        A mainstream open-source BT solution for the Godot ecosystem, covering typical game character behaviors such as enemy patrolling, pursuit, attacks, and reactions to damage.
      </td>
      <td>2</td>
    </tr>
    <tr>
      <td>17</td>
      <td>
        <a href="https://github.com/nhjschulz/cfsm">https://github.com/nhjschulz/cfsm</a><br>
        <a href="https://gitcode.com/gh_mirrors/sm6/sm64">https://gitcode.com/gh_mirrors/sm6/sm64</a>
      </td>
      <td>
        Classic Mario FSM, including Mini Mario/Super/Fire/Cloak state switching and various NPC behavior logic.
      </td>
      <td>97</td>
    </tr>

    <!-- Game AI / BT -->
    <tr>
      <td>18</td>
      <td rowspan="4">BT</td>
      <td>
        <a href="https://github.com/NUDTQI/PartoPrey-BT-RL">https://github.com/NUDTQI/PartoPrey-BT-RL</a>
      </td>
      <td>
        PartoPrey simulation game: Implement AI logic for feeding, attacking, tracking, and patrolling.
      </td>
      <td>21</td>
      <td rowspan="4">88</td>
    </tr>
    <tr>
      <td>19</td>
      <td>
        <a href="https://github.com/Jack-Pettigrew/Resident-Evil-2-Behaviour-Tree-System">https://github.com/Jack-Pettigrew/Resident-Evil-2-Behaviour-Tree-System</a>
      </td>
      <td>
        The AI logic behind Mr. X's patrols, room searches, player pursuit, and reactions to being hit in Resident Evil 2 Remake.
      </td>
      <td>39</td>
    </tr>
    <tr>
      <td>20</td>
      <td>
        <a href="https://github.com/Metsker/limboai">https://github.com/Metsker/limboai</a><br>
        <a href="https://github.com/FlavioFS/godot-platformer-state-machine/tree/master/godot">https://github.com/FlavioFS/godot-platformer-state-machine/tree/master/godot</a>
      </td>
      <td>
        A mainstream open-source BT solution for the Godot ecosystem, covering typical game character behaviors such as enemy patrolling, pursuit, attacks, and reactions to damage.
      </td>
      <td>17</td>
    </tr>
    <tr>
      <td>21</td>
      <td>
        <a href="https://github.com/HoriK816/EnemyBehaviorTreeDemo">https://github.com/HoriK816/EnemyBehaviorTreeDemo</a>
      </td>
      <td>
        Enemy AI in 2D Shooter Games.
      </td>
      <td>11</td>
    </tr>
  </tbody>
</table>

---

## 2. 合成行为模型数据集

<h3>Table 2. Information on Synthetic Behavioral Models</h3>

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Scenario</th>
      <th>Generation Setting</th>
      <th>Node / Structural Type</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <!-- BT Synthetic Models -->
    <tr>
      <td rowspan="3">BT</td>
      <td>Basic symbols</td>
      <td>
        Set the tree depth to 2–10; for each depth, randomly construct 25 B-trees.
      </td>
      <td>
        Use English letters to represent leaf nodes. The initial number of leaf nodes per level is 3–5, and 3–5 leaf nodes are added for each additional level. Select nodes so that they are evenly distributed, forming a B-tree.
      </td>
      <td>225</td>
    </tr>
    <tr>
      <td>Robot</td>
      <td>
        Set the tree depth to 2–10; for each depth, randomly construct 15 B-trees.
      </td>
      <td>
        Construct leaf nodes based on the basic behaviors of warehouse robots. The initial number of leaf nodes per level is 3–5, and 3–5 leaf nodes are added for each additional level. Select nodes and arrange them in a uniform distribution to form a BT tree using appropriate behavioral logic.
      </td>
      <td>135</td>
    </tr>
    <tr>
      <td>Game AI</td>
      <td>
        Set the tree depth to 2–10; for each depth, randomly construct 15 B-trees.
      </td>
      <td>
        Construct leaf nodes based on the fundamental behaviors of the agent AI in the PartoPrey. The initial layer should have 3–5 leaf nodes, and 3–5 leaf nodes should be added with each additional layer. Select nodes and arrange them in a uniform sequence to form a BT using reasonable behavioral logic.
      </td>
      <td>135</td>
    </tr>

    <!-- FSM Synthetic Models -->
    <tr>
      <td rowspan="3">FSM</td>
      <td>Basic symbols</td>
      <td>
        The FSMs have 2–26 states and are uniformly distributed, with each state having 1–5 transitions associated with it.
      </td>
      <td>
        States are represented by English characters, and branch structures, chain structures, and loop structures are evenly distributed within the FSM.
      </td>
      <td>225</td>
    </tr>
    <tr>
      <td>Robot</td>
      <td>
        FSMs with 2–30 states are uniformly distributed, and each state has 1–8 associated transitions.
      </td>
      <td>
        Define states and events based on the basic behaviors of warehouse robots, and construct an FSM using sound logic, ensuring that branch structures, chained structures, and loop structures are evenly distributed within the FSM.
      </td>
      <td>135</td>
    </tr>
    <tr>
      <td>Game AI</td>
      <td>
        FSMs with 2–30 states are uniformly distributed, and each state has 1–8 associated transitions.
      </td>
      <td>
        Use the basic behaviors of the agent AI in the “Tag” game to construct states and events, and organize them into an FSM using sound logic, ensuring that branching, chained, and looping structures are evenly distributed within the FSM.
      </td>
      <td>100</td>
    </tr>
  </tbody>
</table>


---
### Dataset Summary

| Dataset | Type | Scenario | Number |
|---|---|---|---:|
| Open-source behavior models | FSM | Robot | 65 |
| Open-source behavior models | BT | Robot | 96 |
| Open-source behavior models | FSM | Game AI | 120 |
| Open-source behavior models | BT | Game AI | 88 |
| Synthetic behavioral models | BT | Basic symbols | 225 |
| Synthetic behavioral models | BT | Robot | 135 |
| Synthetic behavioral models | BT | Game AI | 135 |
| Synthetic behavioral models | FSM | Basic symbols | 225 |
| Synthetic behavioral models | FSM | Robot | 135 |
| Synthetic behavioral models | FSM | Game AI | 100 |

