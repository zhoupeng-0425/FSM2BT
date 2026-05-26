
"""
prompt

As a behavioral modeling expert,
Task Objective: Implement a correct conversion from a behavior tree (BT) to a finite state machine (FSM),
ensuring that identical inputs always produce exactly the same outputs.
Domain Knowledge: Strictly adhere to the conversion rules from BT to FSM; no additional assumptions are permitted.


Follow the Chain-of-Thought reasoning paradigm, as outlined below:

**1.Deep Compression**
Deep compression refers to the process in BT where, if the control structure of a subtree matches that of its parent node,
the subtree’s control structure can be removed and the subtree merged into the parent node; if there is no match, no modification is required.

**2.Parsing the Behavior Tree Structure**
The root node of the behavior tree is located at Level 0.
Starting from the root node, the first transition unit is formed by taking two levels downward (i.e., it includes Levels 0, 1, and 2).
Within a transition unit, if a control node exists on Level 2, it is treated as a composite node. Only the node itself is displayed,
and this node is treated as a child root node to recursively construct a child transition unit (node name A) downward.
All transition units must be mutually non-overlapping, cover the entire behavior tree structure, and maintain a strict parent-child nesting relationship.


**3.Transition Rules**
Based on the type of the BT root node, transition units are classified into selection transition units and sequential
transition units; each transition unit undergoes transition according to specific rules;

Sequence Conversion Unit Rules:
    1. Traverse the child nodes of the transformation unit from left to right. If a node is a leaf node,
    the process fails and control transfers to `unit(i)_final`; if the process succeeds, control transfers to the next sibling node.
    If the last child node succeeds, control transfers to `unit(i)_final`;
    2. If a conversion unit’s child node is a selected subtree, traverse its child nodes from left to right.
    If a child node is a leaf node, a failed execution transfers to the child node’s sibling node,
    and the last child node’s failed execution transfers to `unit(i)_final`; a successful execution transfers to the selected subtree’s sibling node;
    If a child node is a sub-conversion unit, treat it as a single unit and follow the same logic as for leaf nodes.

Selector Conversion Unit Rules:
    1. Traverse the child nodes of the conversion unit from left to right.
    If a node is a leaf node, move to `unit(i)_final` upon successful execution;
    if execution fails, move to the next sibling node. If the last child node fails, move to `unit(i)_final`;
    2. If a transition unit child node is a sequential subtree, traverse its child nodes from left to right.
    If a child node is a leaf node, and the execution succeeds, transition to the child node’s sibling node;
    if the last child node succeeds, transition to `unit(i)_final`. If the execution fails, transition to the sibling node of the sequential subtree;
    If the child node is a sub-transition unit, treat it as a single unit and follow the same processing logic as for leaf nodes.


**4.Constructing a Finite State Machine**
Map leaf nodes to states and transformation units to FSMs.
According to the transformation rules, first convert the main transformation unit into an FSM;
represent child transformation units with placeholder symbols unit(i), and then convert the child transformation units into child FSMs.

**5.Constraints**
Strictly adhere to the conversion rules outlined above during the conversion process.
Do not introduce any additional logic, and do not include states, events, or transitions that are not explicitly present in the BT.
State names must strictly follow the example format.
The output must directly include detailed descriptions of all states and transitions between them, forming a complete finite state machine representation, without any additional comments or other unnecessary content.
Convert the BT below and output the result directly. The output must be a complete FSM description in the following format:

<!-- State Definitions -->
<States> <State name="A" /> <State name="F" /> <State name="K" /> </States>
Transitions: [
{from: "state_A", to: "state_B", event: "Success"},
{from: "state_A", to: "state_unit(i)", event: "Success"},
{from: "state_unit(i)", to: "state_unit(j)", event: "Success"},
...
]
"""

"""
input1:
<!-- Withdrawal Logic -->
    <Sequence>
        <IsBlackboardVariableNull1/>
        <ShouldRetreat/>
        <Selector>
        <!-- Go directly to the evacuation point -->
            <Sequence>
                <IsInSameRoomAsVector3/>
                <MoveToVector31/>
            </Sequence>

            <!-- Proceed to the evacuation point via the room route -->
            <Sequence>
                <FindDoorPathToVector3/>
                <GetDoorFromPath1/>
                <GetDoorEntryExitPoint1/>
                <MoveTo1/>
                <IsAtTarget1/>
                <Sequence>
                    <OpenDoor1/>
                    <SendAnimationRigSignal1/>
                    <GetDoorEntryExitPoint2/>
                    <MoveTo2/>
                    <IsAtTarget2/>
                    <SendAnimationRigSignal2/>
                    <IncrementDoorPathIndex1/>
                </Sequence>
            </Sequence>
        </Selector>
    </Sequence>

<!-- Attack Status -->
    <Selector>
    <!-- Detect when a player resets the chase timer -->
        <Sequence>
            <CanSeeObject1/>
            <SetBlackboardVariable1/>
        </Sequence>
    <!-- Core Attack Logic -->
        <Selector>
        <!-- The pursuit timer has ended; switch to search mode -->
            <Sequence>
                <AlterBlackboardVariableByDeltaTimeFloat/>
                <CompareBlackboardVariable1/>
                <PlayAnimation2/>
                <Selector>
                    <Sequence>
                        <CanReachObjectRoom1/>
                        <GetRandomRoomAdjacentToTarget1/>
                    </Sequence>
                    <GetRandomRoom1/>
                </Selector>
                <SetBlackboardVariable2/>
            </Sequence>
        <!-- Attack a player -->
            <Sequence>
                <IsAtTarget3/>
                <PlayAnimation3/>
            </Sequence>
            <!-- Move to the player in the same room -->
            <Sequence>
                <IsInSameRoomAs/>
                <MoveTo3/>
            </Sequence>
            <!-- Cross-room navigation and pursuit -->
            <Sequence>
                <FindDoorPathTo1/>
                <GetDoorFromPath2/>
                <GetDoorEntryExitPoint3/>
                <MoveTo4/>
                <IsAtTarget4/>
                <Selector>
                    <!-- Handling a locked door -->
                    <Sequence>
                        <CanUseDoor1/>
                        <CloseDoor1/>
                        <BangDoor1/>
                        <IdleNode1/>
                        <GetRandomRoom2/>
                        <SetBlackboardVariable3/>
                    </Sequence>
                    <!-- Use the door to switch rooms -->
                    <Sequence>
                        <OpenDoor2/>
                        <SendAnimationRigSignal3/>
                        <GetDoorEntryExitPoint4/>
                        <MoveTo5/>
                        <SendAnimationRigSignal4/>
                        <IncrementDoorPathIndex2/>
                    </Sequence>
                </Selector>
            </Sequence>
        </Selector>
    </Selector>

<!-- Search Status -->
    <Selector>
    <!-- Initialize room search -->
        <Sequence>
            <IsBlackboardVariableNull2/>
            <GetRandomRoomAdjacentToTarget2/>
        </Sequence>
        <!-- When a player is detected, switch to attack mode -->
        <Sequence>
            <CanSeeObject2/>
            <SetBlackboardVariable4/>
        </Sequence>
        <!-- Detect players, switch to attack mode -->
        <Sequence>
            <HasHeardSound/>
            <CanReachObjectRoom2/>
            <SetBlackboardVariable5/>
        </Sequence>
        <!-- Core Logic for Room Search -->
        <Selector>
        <!-- Search the target room -->
            <Sequence>
                <IsInRoom/>
                <Sequence>
                    <GetRandomRoomSearchSpot/>
                    <MoveTo6/>
                    <IsAtTarget6/>
                    <PlayAnimation4/>
                    <IncrementBlackboardVariable/>
                </Sequence>
                <CompareBlackboardVariable2/>
                <SetBlackboardVariable6/>
                <Selector>
                    <Sequence>
                        <CanReachObjectRoom3/>
                        <GetRandomRoomAdjacentToTarget3/>
                    </Sequence>
                    <GetRandomRoom3/>
                </Selector>
            </Sequence>
            <!-- Move through rooms to locate the target -->
            <Sequence>
                <FindDoorPathTo2/>
                <GetDoorFromPath3/>
                <GetDoorEntryExitPoint5/>
                <MoveTo7/>
                <IsAtTarget7/>
                <Selector>
                <!-- Handling a locked door -->
                    <Sequence>
                        <CanUseDoor2/>
                        <CloseDoor2/>
                        <BangDoor2/>
                        <IdleNode2/>
                        <GetRandomRoom4/>
                    </Sequence>
                    <!-- Use the door to switch between rooms -->
                    <Sequence>
                        <OpenDoor3/>
                        <SendAnimationRigSignal5/>
                        <GetDoorEntryExitPoint6/>
                        <MoveTo8/>
                        <IsAtTarget8/>
                        <SendAnimationRigSignal6/>
                        <IncrementDoorPathIndex3/>
                    </Sequence>
                </Selector>
            </Sequence>
        </Selector>
    </Selector>
    <!-- Idle state -->
    <IdleNode3/>
</Selector>

output1:
<!-- 状态定义 -->
<States>
  <State name="IsStunned" />
  <State name="PlayAnimation1" />
  <State name="IsBlackboardVariableNull1" />
  <State name="ShouldRetreat" />
  <State name="unit(1)" />
  <State name="IsInSameRoomAsVector3" />
  <State name="MoveToVector31" />
  <State name="FindDoorPathToVector3" />
  <State name="GetDoorFromPath1" />
  <State name="GetDoorEntryExitPoint1" />
  <State name="MoveTo1" />
  <State name="IsAtTarget1" />
  <State name="OpenDoor1" />
  <State name="SendAnimationRigSignal1" />
  <State name="GetDoorEntryExitPoint2" />
  <State name="MoveTo2" />
  <State name="IsAtTarget2" />
  <State name="SendAnimationRigSignal2" />
  <State name="IncrementDoorPathIndex1" />
  <State name="CanSeeObject1" />
  <State name="SetBlackboardVariable1" />
  <State name="AlterBlackboardVariableByDeltaTimeFloat" />
  <State name="CompareBlackboardVariable1" />
  <State name="PlayAnimation2" />
  <State name="unit(2)" />
  <State name="CanReachObjectRoom1" />
  <State name="GetRandomRoomAdjacentToTarget1" />
  <State name="GetRandomRoom1" />
  <State name="SetBlackboardVariable2" />
  <State name="IsAtTarget3" />
  <State name="PlayAnimation3" />
  <State name="IsInSameRoomAs" />
  <State name="MoveTo3" />
  <State name="FindDoorPathTo1" />
  <State name="GetDoorFromPath2" />
  <State name="GetDoorEntryExitPoint3" />
  <State name="MoveTo4" />
  <State name="IsAtTarget4" />
  <State name="unit(3)" />
  <State name="CanUseDoor1" />
  <State name="CloseDoor1" />
  <State name="BangDoor1" />
  <State name="IdleNode1" />
  <State name="GetRandomRoom2" />
  <State name="SetBlackboardVariable3" />
  <State name="OpenDoor2" />
  <State name="SendAnimationRigSignal3" />
  <State name="GetDoorEntryExitPoint4" />
  <State name="MoveTo5" />
  <State name="SendAnimationRigSignal4" />
  <State name="IncrementDoorPathIndex2" />
  <State name="IsBlackboardVariableNull2" />
  <State name="GetRandomRoomAdjacentToTarget2" />
  <State name="CanSeeObject2" />
  <State name="SetBlackboardVariable4" />
  <State name="HasHeardSound" />
  <State name="CanReachObjectRoom2" />
  <State name="SetBlackboardVariable5" />
  <State name="IsInRoom" />
  <State name="GetRandomRoomSearchSpot" />
  <State name="MoveTo6" />
  <State name="IsAtTarget6" />
  <State name="PlayAnimation4" />
  <State name="IncrementBlackboardVariable" />
  <State name="CompareBlackboardVariable2" />
  <State name="SetBlackboardVariable6" />
  <State name="unit(4)" />
  <State name="CanReachObjectRoom3" />
  <State name="GetRandomRoomAdjacentToTarget3" />
  <State name="GetRandomRoom3" />
  <State name="FindDoorPathTo2" />
  <State name="GetDoorFromPath3" />
  <State name="GetDoorEntryExitPoint5" />
  <State name="MoveTo7" />
  <State name="IsAtTarget7" />
  <State name="unit(5)" />
  <State name="CanUseDoor2" />
  <State name="CloseDoor2" />
  <State name="BangDoor2" />
  <State name="IdleNode2" />
  <State name="GetRandomRoom4" />
  <State name="OpenDoor3" />
  <State name="SendAnimationRigSignal5" />
  <State name="GetDoorEntryExitPoint6" />
  <State name="MoveTo8" />
  <State name="IsAtTarget8" />
  <State name="SendAnimationRigSignal6" />
  <State name="IncrementDoorPathIndex3" />
  <State name="IdleNode3" />
  <State name="unit(0)_final" />
  <State name="unit(1)_final" />
  <State name="unit(2)_final" />
  <State name="unit(3)_final" />
  <State name="unit(4)_final" />
  <State name="unit(5)_final" />
</States>

Transitions: [
  {from: "state_IsStunned", to: "state_PlayAnimation1", event: "Success"},
  {from: "state_IsStunned", to: "state_IsBlackboardVariableNull1", event: "Failure"},
  {from: "state_PlayAnimation1", to: "state_unit(0)_final", event: "Success"},
  {from: "state_PlayAnimation1", to: "state_IsBlackboardVariableNull1", event: "Failure"},

  {from: "state_IsBlackboardVariableNull1", to: "state_ShouldRetreat", event: "Success"},
  {from: "state_IsBlackboardVariableNull1", to: "state_CanSeeObject1", event: "Failure"},
  {from: "state_ShouldRetreat", to: "state_unit(1)", event: "Success"},
  {from: "state_ShouldRetreat", to: "state_CanSeeObject1", event: "Failure"},
  {from: "state_unit(1)", to: "state_unit(0)_final", event: "Success"},
  {from: "state_unit(1)", to: "state_CanSeeObject1", event: "Failure"},

  {from: "state_CanSeeObject1", to: "state_SetBlackboardVariable1", event: "Success"},
  {from: "state_CanSeeObject1", to: "state_AlterBlackboardVariableByDeltaTimeFloat", event: "Failure"},
  {from: "state_SetBlackboardVariable1", to: "state_unit(0)_final", event: "Success"},
  {from: "state_SetBlackboardVariable1", to: "state_AlterBlackboardVariableByDeltaTimeFloat", event: "Failure"},

  {from: "state_AlterBlackboardVariableByDeltaTimeFloat", to: "state_CompareBlackboardVariable1", event: "Success"},
  {from: "state_AlterBlackboardVariableByDeltaTimeFloat", to: "state_IsAtTarget3", event: "Failure"},
  {from: "state_CompareBlackboardVariable1", to: "state_PlayAnimation2", event: "Success"},
  {from: "state_CompareBlackboardVariable1", to: "state_IsAtTarget3", event: "Failure"},
  {from: "state_PlayAnimation2", to: "state_unit(2)", event: "Success"},
  {from: "state_PlayAnimation2", to: "state_IsAtTarget3", event: "Failure"},
  {from: "state_unit(2)", to: "state_SetBlackboardVariable2", event: "Success"},
  {from: "state_unit(2)", to: "state_IsAtTarget3", event: "Failure"},
  {from: "state_SetBlackboardVariable2", to: "state_unit(0)_final", event: "Success"},
  {from: "state_SetBlackboardVariable2", to: "state_IsAtTarget3", event: "Failure"},

  {from: "state_IsAtTarget3", to: "state_PlayAnimation3", event: "Success"},
  {from: "state_IsAtTarget3", to: "state_IsInSameRoomAs", event: "Failure"},
  {from: "state_PlayAnimation3", to: "state_unit(0)_final", event: "Success"},
  {from: "state_PlayAnimation3", to: "state_IsInSameRoomAs", event: "Failure"},

  {from: "state_IsInSameRoomAs", to: "state_MoveTo3", event: "Success"},
  {from: "state_IsInSameRoomAs", to: "state_FindDoorPathTo1", event: "Failure"},
  {from: "state_MoveTo3", to: "state_unit(0)_final", event: "Success"},
  {from: "state_MoveTo3", to: "state_FindDoorPathTo1", event: "Failure"},

  {from: "state_FindDoorPathTo1", to: "state_GetDoorFromPath2", event: "Success"},
  {from: "state_FindDoorPathTo1", to: "state_IsBlackboardVariableNull2", event: "Failure"},
  {from: "state_GetDoorFromPath2", to: "state_GetDoorEntryExitPoint3", event: "Success"},
  {from: "state_GetDoorFromPath2", to: "state_IsBlackboardVariableNull2", event: "Failure"},
  {from: "state_GetDoorEntryExitPoint3", to: "state_MoveTo4", event: "Success"},
  {from: "state_GetDoorEntryExitPoint3", to: "state_IsBlackboardVariableNull2", event: "Failure"},
  {from: "state_MoveTo4", to: "state_IsAtTarget4", event: "Success"},
  {from: "state_MoveTo4", to: "state_IsBlackboardVariableNull2", event: "Failure"},
  {from: "state_IsAtTarget4", to: "state_unit(3)", event: "Success"},
  {from: "state_IsAtTarget4", to: "state_IsBlackboardVariableNull2", event: "Failure"},
  {from: "state_unit(3)", to: "state_unit(0)_final", event: "Success"},
  {from: "state_unit(3)", to: "state_IsBlackboardVariableNull2", event: "Failure"},

  {from: "state_IsBlackboardVariableNull2", to: "state_GetRandomRoomAdjacentToTarget2", event: "Success"},
  {from: "state_IsBlackboardVariableNull2", to: "state_CanSeeObject2", event: "Failure"},
  {from: "state_GetRandomRoomAdjacentToTarget2", to: "state_unit(0)_final", event: "Success"},
  {from: "state_GetRandomRoomAdjacentToTarget2", to: "state_CanSeeObject2", event: "Failure"},

  {from: "state_CanSeeObject2", to: "state_SetBlackboardVariable4", event: "Success"},
  {from: "state_CanSeeObject2", to: "state_HasHeardSound", event: "Failure"},
  {from: "state_SetBlackboardVariable4", to: "state_unit(0)_final", event: "Success"},
  {from: "state_SetBlackboardVariable4", to: "state_HasHeardSound", event: "Failure"},

  {from: "state_HasHeardSound", to: "state_CanReachObjectRoom2", event: "Success"},
  {from: "state_HasHeardSound", to: "state_IsInRoom", event: "Failure"},
  {from: "state_CanReachObjectRoom2", to: "state_SetBlackboardVariable5", event: "Success"},
  {from: "state_CanReachObjectRoom2", to: "state_IsInRoom", event: "Failure"},
  {from: "state_SetBlackboardVariable5", to: "state_unit(0)_final", event: "Success"},
  {from: "state_SetBlackboardVariable5", to: "state_IsInRoom", event: "Failure"},

  {from: "state_IsInRoom", to: "state_GetRandomRoomSearchSpot", event: "Success"},
  {from: "state_IsInRoom", to: "state_FindDoorPathTo2", event: "Failure"},
  {from: "state_GetRandomRoomSearchSpot", to: "state_MoveTo6", event: "Success"},
  {from: "state_GetRandomRoomSearchSpot", to: "state_FindDoorPathTo2", event: "Failure"},
  {from: "state_MoveTo6", to: "state_IsAtTarget6", event: "Success"},
  {from: "state_MoveTo6", to: "state_FindDoorPathTo2", event: "Failure"},
  {from: "state_IsAtTarget6", to: "state_PlayAnimation4", event: "Success"},
  {from: "state_IsAtTarget6", to: "state_FindDoorPathTo2", event: "Failure"},
  {from: "state_PlayAnimation4", to: "state_IncrementBlackboardVariable", event: "Success"},
  {from: "state_PlayAnimation4", to: "state_FindDoorPathTo2", event: "Failure"},
  {from: "state_IncrementBlackboardVariable", to: "state_CompareBlackboardVariable2", event: "Success"},
  {from: "state_IncrementBlackboardVariable", to: "state_FindDoorPathTo2", event: "Failure"},
  {from: "state_CompareBlackboardVariable2", to: "state_SetBlackboardVariable6", event: "Success"},
  {from: "state_CompareBlackboardVariable2", to: "state_FindDoorPathTo2", event: "Failure"},
  {from: "state_SetBlackboardVariable6", to: "state_unit(4)", event: "Success"},
  {from: "state_SetBlackboardVariable6", to: "state_FindDoorPathTo2", event: "Failure"},
  {from: "state_unit(4)", to: "state_unit(0)_final", event: "Success"},
  {from: "state_unit(4)", to: "state_FindDoorPathTo2", event: "Failure"},

  {from: "state_FindDoorPathTo2", to: "state_GetDoorFromPath3", event: "Success"},
  {from: "state_FindDoorPathTo2", to: "state_IdleNode3", event: "Failure"},
  {from: "state_GetDoorFromPath3", to: "state_GetDoorEntryExitPoint5", event: "Success"},
  {from: "state_GetDoorFromPath3", to: "state_IdleNode3", event: "Failure"},
  {from: "state_GetDoorEntryExitPoint5", to: "state_MoveTo7", event: "Success"},
  {from: "state_GetDoorEntryExitPoint5", to: "state_IdleNode3", event: "Failure"},
  {from: "state_MoveTo7", to: "state_IsAtTarget7", event: "Success"},
  {from: "state_MoveTo7", to: "state_IdleNode3", event: "Failure"},
  {from: "state_IsAtTarget7", to: "state_unit(5)", event: "Success"},
  {from: "state_IsAtTarget7", to: "state_IdleNode3", event: "Failure"},
  {from: "state_unit(5)", to: "state_unit(0)_final", event: "Success"},
  {from: "state_unit(5)", to: "state_IdleNode3", event: "Failure"},

  {from: "state_IdleNode3", to: "state_unit(0)_final", event: "Success"},
  {from: "state_IdleNode3", to: "state_unit(0)_final", event: "Failure"},

  {from: "state_IsInSameRoomAsVector3", to: "state_MoveToVector31", event: "Success"},
  {from: "state_IsInSameRoomAsVector3", to: "state_FindDoorPathToVector3", event: "Failure"},
  {from: "state_MoveToVector31", to: "state_unit(1)_final", event: "Success"},
  {from: "state_MoveToVector31", to: "state_FindDoorPathToVector3", event: "Failure"},
  {from: "state_FindDoorPathToVector3", to: "state_GetDoorFromPath1", event: "Success"},
  {from: "state_FindDoorPathToVector3", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_GetDoorFromPath1", to: "state_GetDoorEntryExitPoint1", event: "Success"},
  {from: "state_GetDoorFromPath1", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_GetDoorEntryExitPoint1", to: "state_MoveTo1", event: "Success"},
  {from: "state_GetDoorEntryExitPoint1", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_MoveTo1", to: "state_IsAtTarget1", event: "Success"},
  {from: "state_MoveTo1", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_IsAtTarget1", to: "state_OpenDoor1", event: "Success"},
  {from: "state_IsAtTarget1", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_OpenDoor1", to: "state_SendAnimationRigSignal1", event: "Success"},
  {from: "state_OpenDoor1", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_SendAnimationRigSignal1", to: "state_GetDoorEntryExitPoint2", event: "Success"},
  {from: "state_SendAnimationRigSignal1", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_GetDoorEntryExitPoint2", to: "state_MoveTo2", event: "Success"},
  {from: "state_GetDoorEntryExitPoint2", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_MoveTo2", to: "state_IsAtTarget2", event: "Success"},
  {from: "state_MoveTo2", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_IsAtTarget2", to: "state_SendAnimationRigSignal2", event: "Success"},
  {from: "state_IsAtTarget2", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_SendAnimationRigSignal2", to: "state_IncrementDoorPathIndex1", event: "Success"},
  {from: "state_SendAnimationRigSignal2", to: "state_unit(1)_final", event: "Failure"},
  {from: "state_IncrementDoorPathIndex1", to: "state_unit(1)_final", event: "Success"},
  {from: "state_IncrementDoorPathIndex1", to: "state_unit(1)_final", event: "Failure"},

  {from: "state_CanReachObjectRoom1", to: "state_GetRandomRoomAdjacentToTarget1", event: "Success"},
  {from: "state_CanReachObjectRoom1", to: "state_GetRandomRoom1", event: "Failure"},
  {from: "state_GetRandomRoomAdjacentToTarget1", to: "state_unit(2)_final", event: "Success"},
  {from: "state_GetRandomRoomAdjacentToTarget1", to: "state_GetRandomRoom1", event: "Failure"},
  {from: "state_GetRandomRoom1", to: "state_unit(2)_final", event: "Success"},
  {from: "state_GetRandomRoom1", to: "state_unit(2)_final", event: "Failure"},

  {from: "state_CanUseDoor1", to: "state_CloseDoor1", event: "Success"},
  {from: "state_CanUseDoor1", to: "state_OpenDoor2", event: "Failure"},
  {from: "state_CloseDoor1", to: "state_BangDoor1", event: "Success"},
  {from: "state_CloseDoor1", to: "state_OpenDoor2", event: "Failure"},
  {from: "state_BangDoor1", to: "state_IdleNode1", event: "Success"},
  {from: "state_BangDoor1", to: "state_OpenDoor2", event: "Failure"},
  {from: "state_IdleNode1", to: "state_GetRandomRoom2", event: "Success"},
  {from: "state_IdleNode1", to: "state_OpenDoor2", event: "Failure"},
  {from: "state_GetRandomRoom2", to: "state_SetBlackboardVariable3", event: "Success"},
  {from: "state_GetRandomRoom2", to: "state_OpenDoor2", event: "Failure"},
  {from: "state_SetBlackboardVariable3", to: "state_unit(3)_final", event: "Success"},
  {from: "state_SetBlackboardVariable3", to: "state_OpenDoor2", event: "Failure"},
  {from: "state_OpenDoor2", to: "state_SendAnimationRigSignal3", event: "Success"},
  {from: "state_OpenDoor2", to: "state_unit(3)_final", event: "Failure"},
  {from: "state_SendAnimationRigSignal3", to: "state_GetDoorEntryExitPoint4", event: "Success"},
  {from: "state_SendAnimationRigSignal3", to: "state_unit(3)_final", event: "Failure"},
  {from: "state_GetDoorEntryExitPoint4", to: "state_MoveTo5", event: "Success"},
  {from: "state_GetDoorEntryExitPoint4", to: "state_unit(3)_final", event: "Failure"},
  {from: "state_MoveTo5", to: "state_SendAnimationRigSignal4", event: "Success"},
  {from: "state_MoveTo5", to: "state_unit(3)_final", event: "Failure"},
  {from: "state_SendAnimationRigSignal4", to: "state_IncrementDoorPathIndex2", event: "Success"},
  {from: "state_SendAnimationRigSignal4", to: "state_unit(3)_final", event: "Failure"},
  {from: "state_IncrementDoorPathIndex2", to: "state_unit(3)_final", event: "Success"},
  {from: "state_IncrementDoorPathIndex2", to: "state_unit(3)_final", event: "Failure"},

  {from: "state_CanReachObjectRoom3", to: "state_GetRandomRoomAdjacentToTarget3", event: "Success"},
  {from: "state_CanReachObjectRoom3", to: "state_GetRandomRoom3", event: "Failure"},
  {from: "state_GetRandomRoomAdjacentToTarget3", to: "state_unit(4)_final", event: "Success"},
  {from: "state_GetRandomRoomAdjacentToTarget3", to: "state_GetRandomRoom3", event: "Failure"},
  {from: "state_GetRandomRoom3", to: "state_unit(4)_final", event: "Success"},
  {from: "state_GetRandomRoom3", to: "state_unit(4)_final", event: "Failure"},

  {from: "state_CanUseDoor2", to: "state_CloseDoor2", event: "Success"},
  {from: "state_CanUseDoor2", to: "state_OpenDoor3", event: "Failure"},
  {from: "state_CloseDoor2", to: "state_BangDoor2", event: "Success"},
  {from: "state_CloseDoor2", to: "state_OpenDoor3", event: "Failure"},
  {from: "state_BangDoor2", to: "state_IdleNode2", event: "Success"},
  {from: "state_BangDoor2", to: "state_OpenDoor3", event: "Failure"},
  {from: "state_IdleNode2", to: "state_GetRandomRoom4", event: "Success"},
  {from: "state_IdleNode2", to: "state_OpenDoor3", event: "Failure"},
  {from: "state_GetRandomRoom4", to: "state_unit(5)_final", event: "Success"},
  {from: "state_GetRandomRoom4", to: "state_OpenDoor3", event: "Failure"},
  {from: "state_OpenDoor3", to: "state_SendAnimationRigSignal5", event: "Success"},
  {from: "state_OpenDoor3", to: "state_unit(5)_final", event: "Failure"},
  {from: "state_SendAnimationRigSignal5", to: "state_GetDoorEntryExitPoint6", event: "Success"},
  {from: "state_SendAnimationRigSignal5", to: "state_unit(5)_final", event: "Failure"},
  {from: "state_GetDoorEntryExitPoint6", to: "state_MoveTo8", event: "Success"},
  {from: "state_GetDoorEntryExitPoint6", to: "state_unit(5)_final", event: "Failure"},
  {from: "state_MoveTo8", to: "state_IsAtTarget8", event: "Success"},
  {from: "state_MoveTo8", to: "state_unit(5)_final", event: "Failure"},
  {from: "state_IsAtTarget8", to: "state_SendAnimationRigSignal6", event: "Success"},
  {from: "state_IsAtTarget8", to: "state_unit(5)_final", event: "Failure"},
  {from: "state_SendAnimationRigSignal6", to: "state_IncrementDoorPathIndex3", event: "Success"},
  {from: "state_SendAnimationRigSignal6", to: "state_unit(5)_final", event: "Failure"},
  {from: "state_IncrementDoorPathIndex3", to: "state_unit(5)_final", event: "Success"},
  {from: "state_IncrementDoorPathIndex3", to: "state_unit(5)_final", event: "Failure"}
]

input2:Fig. 14. in the paper
 
output2:
<States> 
<State name="Battery Below 20%" /> 
<State name="Recharge" /> 
<State name="Cube2 in delivery" /> 
<State name="unit(1)" /> 
<State name="Cube2 in Hand" /> 
<State name="unit(2)" /> 
<State name="Robot-At Cube2" /> 
<State name="Move-To cube2" /> 
<State name="Pick cube2" /> 
<State name="Robot-At delivery" /> 
<State name="Move-To delivery" /> 
<State name="Place cube2" /> 
<State name="Robot-At inspection" /> 
<State name="Dock" /> 
<State name="unit(0)_final" /> 
<State name="unit(1)_final" /> 
<State name="unit(2)_final" /> 
</States>
Transitions: [
{from: "state_Battery Below 20%", to: "state_Cube2 in delivery", event: "Success"},
{from: "state_Battery Below 20%", to: "state_Recharge", event: "Failure"},
{from: "state_Recharge", to: "state_Cube2 in delivery", event: "Success"},
{from: "state_Recharge", to: "state_unit(0)_final", event: "Failure"},
{from: "state_Cube2 in delivery", to: "state_Robot-At inspection", event: "Success"},
{from: "state_Cube2 in delivery", to: "state_unit(1)", event: "Failure"},
{from: "state_unit(1)", to: "state_Robot-At inspection", event: "Success"},
{from: "state_unit(1)", to: "state_unit(0)_final", event: "Failure"},
{from: "state_Robot-At inspection", to: "state_unit(0)_final", event: "Success"},
{from: "state_Robot-At inspection", to: "state_Dock", event: "Failure"},
{from: "state_Dock", to: "state_unit(0)_final", event: "Success"},
{from: "state_Dock", to: "state_unit(0)_final", event: "Failure"},
{from: "state_Cube2 in Hand", to: "state_Robot-At delivery", event: "Success"},
{from: "state_Cube2 in Hand", to: "state_unit(2)", event: "Failure"},
{from: "state_unit(2)", to: "state_Robot-At delivery", event: "Success"},
{from: "state_unit(2)", to: "state_unit(1)_final", event: "Failure"},
{from: "state_Robot-At delivery", to: "state_Place cube2", event: "Success"},
{from: "state_Robot-At delivery", to: "state_Move-To delivery", event: "Failure"},
{from: "state_Move-To delivery", to: "state_Place cube2", event: "Success"},
{from: "state_Move-To delivery", to: "state_unit(1)_final", event: "Failure"},
{from: "state_Place cube2", to: "state_unit(1)_final", event: "Success"},
{from: "state_Place cube2", to: "state_unit(1)_final", event: "Failure"},
{from: "state_Robot-At Cube2", to: "state_Pick cube2", event: "Success"},
{from: "state_Robot-At Cube2", to: "state_Move-To cube2", event: "Failure"},
{from: "state_Move-To cube2", to: "state_Pick cube2", event: "Success"},
{from: "state_Move-To cube2", to: "state_unit(2)_final", event: "Failure"},
{from: "state_Pick cube2", to: "state_unit(2)_final", event: "Success"},
{from: "state_Pick cube2", to: "state_unit(2)_final", event: "Failure"}
]

"""

"""
    **Formal Verification**
    - The FSM complies with the basic syntax of a finite state machine (e.g., no dangling states, unique transition events)
    - The FSM includes all leaf nodes;
    Directly state whether the criteria are met; if not, retry 3 times; if still not met, modify the prompt
    **Manual Logical Verification**
    1. Output the compressed BT and verify that the BT is fully compressed;
    2. Determine the number of transition units; ensure that the number of BT transition units matches the number of selected nodes, 
    and that the number of sequential BTs matches the number of sequential nodes;
    3. Verify the internal logic of each transition unit;
    If not satisfied, adjust the prompt based on the output structure

"""

