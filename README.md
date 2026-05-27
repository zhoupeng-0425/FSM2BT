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
    <tr>
      <td>1</td>
      <td rowspan="6">Robot</td>
      <td rowspan="6">FSM</td>
      <td>
        <a href="https://github.com/ethz-asl/bt_fsm_comparison">bt_fsm_comparison</a>
      </td>
      <td>
        Warehouse robotics project, supporting operations such as movement, gripping, and charging.
      </td>
      <td>5</td>
      <td rowspan="6">65</td>
    </tr>
    <tr>
      <td>2</td>
      <td>
        <a href="https://wiki.ros.org/smach/Tutorials">SMACH Tutorials</a>
      </td>
      <td>
        General-purpose robotics library.
      </td>
      <td>20</td>
    </tr>
    <tr>
      <td>3</td>
      <td>
        <a href="https://github.com/unitreerobotics/unitree_guide">unitree_guide</a><br>
        <a href="https://github.com/mit-biomimetics/Cheetah-Software">Cheetah-Software</a>
      </td>
      <td>
        Quadruped robots, including the initial state, stationary state, trotting state, balanced state, and free state.
      </td>
      <td>17</td>
    </tr>
    <tr>
      <td>4</td>
      <td>
        <a href="https://github.com/robertandreibarbulesscu/FSM_wall_following">FSM_wall_following</a>
      </td>
      <td>
        FSM for obstacle avoidance and wall-following in mobile robots, primarily comprising the states Wander, WallDetected, FollowWall, and Turn.
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>
        <a href="https://neurobionics.github.io/opensourceleg/examples/fsm_walking_controller">fsm_walking_controller</a>
      </td>
      <td>
        Mechanical leg.
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>
        <a href="https://github.com/nicholasmiller1/Robot-Line-Follower">Robot-Line-Follower</a>
      </td>
      <td>
        The FSM states for the line-following robot include FSMCentered, FSMTurnLeft, FSMTurnHardLeft, FSMTurnRight, FSMTurnHardRight, and FSMLos.
      </td>
      <td>1</td>
    </tr>
  </tbody>
</table>

---

## 2. 合成行为模型数据集

下表展示了合成行为模型数据集的信息。

| Type | Scenario | Tree Depth | Node Type | Total |
|---|---|---|---|---:|
| BT | Basic symbols | Set the tree depth to 2–10; for each depth, randomly construct 25 B-trees. | Use English letters to represent leaf nodes. The initial number of leaf nodes per level is 3–5, and 3–5 leaf nodes are added for each additional level. Select nodes so that they are evenly distributed, forming a B-tree. | 225 |
| BT | Robot | Set the tree depth to 2–10; for each depth, randomly construct 15 B-trees. | Construct leaf nodes based on the basic behaviors of warehouse robots. The initial number of leaf nodes per level is 3–5, and 3–5 leaf nodes are added for each additional level. Select nodes and arrange them in a uniform distribution to form a BT tree using appropriate behavioral logic. | 135 |
| BT | Game AI | Set the tree depth to 2–10; for each depth, randomly construct 15 B-trees. | Construct leaf nodes based on the fundamental behaviors of the agent AI in the PartoPrey. The initial layer should have 3–5 leaf nodes, and 3–5 leaf nodes should be added with each additional layer. Select nodes and arrange them in a uniform sequence to form a BT using reasonable behavioral logic. | 135 |

---

## 数据集统计

### 开源行为模型数据集

| Dataset | Scenario | Type | Number |
|---|---|---|---:|
| Open-source behavior models | Robot | FSM | 65 |

### 合成行为模型数据集

| Dataset | Type | Scenario | Number |
|---|---|---|---:|
| Synthetic behavioral models | BT | Basic symbols | 225 |
| Synthetic behavioral models | BT | Robot | 135 |
| Synthetic behavioral models | BT | Game AI | 135 |
| **Total** | - | - | **495** |
