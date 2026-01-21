#负责 “定义任务”（提示词）
__all__ = ['PromptConfig']


class PromptConfig:
    """提示词模板配置"""

    # 提示词
    BT_to_FSM_PROMPT= """作为行为模型建模专家
    **任务目标**：实现行为树（BT）到有限状态机（FSM）的确定性转换，确保相同输入始终生成完全一致的输出。
    **领域知识** 严格遵循转换流程，禁止任何额外假设。
    
    遵循Chain-of-Thought推理范式，步骤如下：
    1. **深度压缩**
    - 深度压缩指BT中若存在子树的控制结构与父节点控制结构一致可将去除子树控制结构，将子树上移只父节点，没有就不需要修改。
    2. **解析行为树结构**
    - 行为树的根节点位于第 0 层
    - 以根节点为起点，向下取两层（即包含第 0 层、第 1 层、第 2 层）构成第一个转换单元（顶层单元）。顶层单元中，第 2 层的控制节点不展开子节点，仅显示节点本身，并视为子转换单元。遍历顶层单元中第 2 层的所有控制节点；每个控制节点被视为一个子树的根。
    - 对于每一个这样的控制节点，以其自身为起点，向下再取两层（即该节点所在层、该节点所在层+1 和 +2 层）构成子转换单元。
    - 对每个子转换单元递归应用相同规则：若其最底层（即该转换单元中包含的最深层）仍包含控制节点，则以该控制节点为新子树根，继续向下取两层构建更深层的转换单元。
    - 所有转换单元应互不重叠、覆盖完整行为树结构，并保持严格的父子嵌套关系。
    3. **转换规则**
   - 根据BT根节点类型，将行为树分为选择BT和顺序BT，每个转换单元分别进行转换；
   - 顺序BT转换规则：从左到右遍历BT，若是叶子节点，执行成功就转移到下一个节点或选择子树，执行失败转移到final状态。若是选择子树，从左到右依次执行叶子节点或子转换单元，执行失败就转移到选择子树的下一个叶子节点或子转换单元，全部执行失败转移到final状态；执行成功就转移到主树的下一个节点或选择子树，全部执行成功则转移到final。
   执行成功就转移到下主树的一个节点，执行失败转移到final状态。
    - 选择BT转换规则：从左到右遍历BT，若是叶子节点，执行失败就转移到下一个节点或顺序子树，执行成功转移到final状态。若是顺序子树，从左到右依次执行叶子节点或子转换单元，执行成功就转移到选择子树的下一个叶子节点或子转换单元，全部执行成功转移到final状态；执行失败就转移到主树的下一个节点或选择子树，全部执行失败则转移到final。 执行失败就转移到下主树的一个节点，全部执行失败转移到final状态。
    4. **构建有限状态机**
    - 将叶子节点映射为状态，转换单元映射为FSM
    - 根据转换规则先将主转换单元转换为FSM，然后将子转换单元转换为子FSM。
    5. **约束条件**
   - 转换过程中严格遵守上述步骤，不得引入额外逻辑。
   - 输出应直接包含所有状态及状态间转移的详细描述，形成完整的有限状态机表示，无任何额外注释或其他非必要内容。
    5. **约束条件**
   - 转换过程中严格遵守上述步骤，不得引入额外逻辑,禁止引入未在 BT 中显式存在的状态、事件或转移。  
   - 输出应直接包含所有状态及状态间转移的详细描述，形成完整的有限状态机表示，无任何额外注释或其他非必要内容。  
   - 将下面BT进行转换，直接输出结果，输出必须为完整 FSM 描述，格式为：  
     ```
     States: [状态列表]
     Transitions: [
       {from: "状态_A", to: "状态_B", event: "Success"},
       ...
     ]
  ***input:<BT>
  <BehaviorTree ID="Untitled">
  <Sequence>
    <Fallback>
      <BatteryBelow/>
      <Recharge/>
    </Fallback>
    <Fallback>
      <Cube2inDelivery/>
      <Sequence>
        <Fallback>
          <CubeinHand/>
          <Sequence>
            <Fallback>
              <RobotatCube2/>
              <MovetoCube2/>
            </Fallback>
            <Pickcube2/>
          </Sequence>
        </Fallback>
        <Fallback>
          <RobotatDelivery/>
          <MovetoDelivery/>
        </Fallback>
        <PlaceCube2/>
      </Sequence>
    </Fallback>
    <Fallback>
      <RobotAtInspection/>
      <Dock/>
    </Fallback>
  </Sequence>
</BehaviorTree>
    """



    # 提示词
    FSM_to_BT_PROMPT = """作为行为模型建模专家
        **任务目标**：实现有限状态机（FSM）到行为树（BT）的确定性转换，确保相同输入始终生成完全一致的输出。
        **领域知识** 严格遵循FSM与循环行为树（LEBT）的定义映射，禁止任何额外假设。

        遵循Chain-of-Thought推理范式，步骤如下：
        1.**FSM典型结构识别**
        **入口状态**：Start状态出度唯所连接的所有状态。
        **循环状态**：入度>=2的状态。
        **普通状态**：入度=1的状态。
        **分支链路**：状态S存在n个出度（n>0）,**若存在i个出度（1<i<=n）连接普通状态**，则S与i个出度指向的普通状态形成分支链路，指向循环状态的链路不属于分支链路，不用表示。
        **链式链路**：状态S存在n个出度（n>0）,**若存在i个出度（i==1）连接普通**，且该后继状态的出度也满足此条件（递归），则为链式链路，指向循环状态的链路不属于分支链路，不用表示。
        2.**LEBT典型结构（严格定义）**
        **选择子树**：根=选择节点，左子=条件节点（事件），右子=动作节点/分支结构/顺序结构（若状态有分支/链式链路）。
        **入口结构**：根=顺序节点，子节点=**[入口状态选择子树, 循环状态选择子树]**。
        **分支结构**：根=顺序节点，子节点=**[动作节点S, 多个选择子树]（对应S的分支链路各普通状态）。
        **顺序结构**：根=顺序节点，子节点=**[动作节点S, 选择子树]**（对应S的链式链路下一状态，嵌套递归）
        3.**FSM与LEBT映射关系（一一对应）**
        **FSM中的状态映射为LEBT中的动作节点（命令：动作_状态名）**
        **FSM中的事件映射为LEBT中的条件节点，同一个动作节点的事件可以合并为一个条件节点（命名：条件_事件名）**
        **入口状态、循环状态→入口结构中的选择子树**
        **分支链路→分支结构（顺序节点+动作S+多选择子树）；链式链路→顺序结构（顺序节点+动作S+单选择子树，递归嵌套）**
        4.**LEBT构建流程（固定顺序）**
        **根节点**：入口结构（顺序节点，name="入口结构"）
        **入口结构子节点**：依次添加入口状态选择子树、循环状态选择子树。
        **选择子树右子节点处理**：若状态有分支链路→右子节点=分支结构；有链式链路→右子节点=顺序结构；无→右子节点=动作节点。
        **顺序结构内嵌套**：按链式链路顺序递归构建（如F→I→J：顺序结构_FIJ含动作F+选择子树_FI，选择子树_FI右子节点=顺序结构_IJ）
        5.**约束（强制遵守）**
        - 禁止任何额外逻辑，仅按上述定义转换。
        - 节点命名严格遵循示例格式（如选择子树_状态名、顺序结构_链路名）。
        - 输出直接为完整BT，包含所有FSM的所有状态 XML，无注释外多余内容。
        ***input:<FSM>
      <!-- 初始状态 -->
      <InitialState>Start</InitialState>

      <!-- 状态定义 -->
      <States>
        <State name="Start" type="initial"/>
        <State name="A" />
        <State name="B" />
        <State name="C" />
        <State name="D" />
        <State name="E" />
        <State name="F" />
        <State name="G" />
        <State name="H" />
        <State name="I" />
        <State name="J" />
      </States>

      <!-- 转移定义（包含起点、终点和事件） -->
      <Transitions>
        <Transition from="Start" to="A" event="eventStartA"/>
        <Transition from="A" to="C" event="eventAC"/>
        <Transition from="A" to="B" event="eventAB"/>
        <Transition from="A" to="D" event="eventAD"/>
        <Transition from="A" to="F" event="eventAF"/>
        <Transition from="B" to="C" event="eventBC"/>
        <Transition from="B" to="D" event="eventBD"/>
        <Transition from="C" to="D" event="eventCD"/>
        <Transition from="D" to="E" event="eventDE"/>
        <Transition from="E" to="C" event="eventEC"/>
        <Transition from="E" to="G" event="eventEG"/>
        <Transition from="E" to="D" event="eventED"/>
        <Transition from="G" to="H" event="eventGH"/>
        <Transition from="F" to="I" event="eventFI"/>
        <Transition from="I" to="J" event="eventIJ"/>
      </Transitions>
    </FSM>***
        """
