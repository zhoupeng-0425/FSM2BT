
"""
prompt

As a behavioral modeling expert
Task Objective: Implement a correct conversion from a finite state machine (FSM) to a behavior tree (BT),
ensuring that identical inputs always produce exactly the same outputs.

Domain Knowledge: Strictly adhere to the defined mappings between FSMs and looped behavior trees (LEBTs);
no additional assumptions are permitted.


Follow the Chain-of-Thought reasoning paradigm, with the following steps:
    1. **Identification of Typical FSM Structures**
    **FSM Examples**
<FSM>
  <States>
    <State name=" Start" type="initial"/>
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
</FSM>

    **Entry State**: A state with out-degrees only to the states it connects to, such as state A.
    **Loop State**: A state with in-degrees ≥ 2, such as states C and D.
    **Ordinary State**: A state with in-degrees = 1, such as states B, E, G, H, F, I, and J.
    **Branch Link**: State S has n outgoing edges (n > 0). **If there are i outgoing edges (1 < i ≤ n) connected to ordinary states**,
    then S forms a branch link with the i ordinary states pointed to by those edges, such as A → B/F.
    Links pointing to non-ordinary states do not constitute branch links, such as A → C and A → D.
    **Chain Linkage**: State S has n outgoing edges (n > 0). **If there are i outgoing edges (i == 1) connecting to ordinary states**,
    and the outgoing edges of the successor states also satisfy this condition (recursively),
    then it is a chain linkage, such as F->I->J and E->G->H. Links pointing to non-ordinary states do not constitute chain linkages, such as E->D.


    2. **Typical LEBT Structure (Strict Definition)**
    **Selection Subtree**: Root = selection node; left child = condition node (event); right child = action node/branch structure/sequence structure (if a state has branches or chained links, selection subtrees may be nested within one another).


    Structure 1 (right child = action node):
    <Fallback>
        <event/>
        <state/>
    </Fallback>

    Structure 2 (Right Child = Branch Structure):
    <Fallback>
        <event/>
        <Sequence>
            <state/>
            <Fallback--branch 1>
                <event/>
                <state/>
            </Fallback>
            <Fallback--branch 2>
                <event/>
                <state/>
            </Fallback>
            ...
            <Fallback--branch n>
                <event/>
                <state/>
            </Fallback>
        </Sequence>
    </Fallback>

    Structure 3 (Right Child = Sequence Structure):
    <Fallback>
        <event/>
        <Sequence>
            <state/>
            <Fallback--Sequence 1>
                <event/>
                <Sequence>
                    <state/>
                    <Fallback--Sequence 2>
                        <event/>
                        <state/>
                    </Fallback>
                </Sequence>
            </Fallback>
        </Sequence>
    </Fallback>

    **Entry Structure**: Root = sequential node; child nodes = **[subtrees consisting of entry states and loop states]**
    <Sequence>
        <Fallback--entry states 1>
            <event/>
            <state/>
        </Fallback>
        ...
        <Fallback--entry states n>
            <event/>
            <state/>
        </Fallback>
        <Fallback--loop state 1>
            <event/>
            <state/>
        </Fallback>
        ...
        <Fallback--loop state n>
            <event/>
            <state/>
        </Fallback>
    </Sequence>

    3. **Mapping Relationship Between FSM and LEBT (One-to-One Correspondence)**
    **States in the FSM map to unique action nodes in LEBT (named: action_state_name)**
    **Events in the FSM map to condition nodes in LEBT; events associated with the same action node can be merged into a single condition node (named: condition_event_name)**
    **Entry states and looping states → Selection subtrees in the entry structure**
    **Only ordinary states can form branch links and chained links; branch links map to branch structures; chained links map to sequential structures (recursive nesting)**

    4.**LEBT Construction Process (Fixed Order)**
    **Root Node**: The child nodes of the root node `root` form the entry structure
    For example, the entry structure in the sample can be converted to LEBT as follows:

    <root>
        < Entry Structure >
    </root>

    **Entry Structure Sub-nodes**: Add the entry state selection subtree and the loop state selection subtree in sequence.
    <root>
        <Sequence>
            <Fallback--entry state A>
                <eventStartA/>
                <A/>
            </Fallback>
            <Fallback--loop state C>
                <eventToC />
                <C/>
            </Fallback>
            <Fallback-- loop state D>
                <eventToD/>
                <D/>
        </Sequence>
    </root>

    **Handling the Right Child Node of the Subtree in Entry Structure Selection**:
    If the state contains branch links → the right child node is a branch structure;
    if it contains chain links → the right child node is a sequential structure;
    if neither is present → the right child node is an action node.
    <root>
        <Sequence>
            <Fallback--entry state A>
                <eventStartA/>
                <Sequence>
                    <A/>
                    <Fallback--branch B>
                        <eventToB/>
                        <B/>
                    </Fallback>
                    <Fallback--branch F>
                        <eventToF/>
                        <Sequence>
                            <F/>
                            <Fallback--sequence I>
                                <eventToI/>
                                <Sequence>
                                    <I/>
                                    <Fallback--sequence J>
                                        <eventToJ/>
                                        <J/>
                                    </Fallback>
                                </Sequence>
                            </Fallback>
                        </Sequence>
                    </Fallback>
                </Sequence>
            </Fallback>
            <Fallback--loop state C>
                <eventToC />
                <C/>
            </Fallback>
            <Fallback--loop state D>
                <eventToD/>
                <Sequence>
                    <D/>
                    <Fallback--sequence E>
                        <eventToE/>
                        <Sequence>
                            <E/>
                            <Fallback--sequence G>
                                <eventToG/>
                                <Sequence>
                                    <E/>
                                    <Fallback--sequence H>
                                        <eventToH/>
                                        <H/>
                                    </Fallback>
                                </Sequence>
                            </Fallback>
                        </Sequence>
                    </Fallback>
                </Sequence>
            </Fallback>
        </Sequence>
    </root>

    5. **Constraints (Mandatory Compliance)**
    - No additional logic is permitted; conversion must strictly follow the definitions provided above.
    - Node names must strictly adhere to the example format.
    - The output must be a complete BT file containing XML for all states of all FSMs, with no extraneous content other than comments.

"""
"""
input1:
<States> 
    <State name="StartChuckya" type="initial"/>  
    <State name="IDLE" /> 
    <State name="CHASE" /> 
    <State name="RETURN_HOME" /> 
    <State name="GRAB_MARIO" /> 
    <State name="THROW_MARIO" /> 
    <State name="COOLDOWN" /> 
    <State name="DEATH" /> 
</States> 
    <Transitions> 
    <Transition from="StartChuckya" to="REST" event="init_done"/>
    <Transition from="IDLE" to="CHASE" event="mario_near"/>
    <Transition from="CHASE" to="IDLE" event="mario_far"/>
    <Transition from="CHASE" to="RETURN_HOME" event="too_far_from_home"/>
    <Transition from="RETURN_HOME" to="IDLE" event="arrived_home"/>
    
    <Transition from="IDLE" to="GRAB_MARIO" event="catch_mario"/>
    <Transition from="CHASE" to="GRAB_MARIO" event="catch_mario"/>
    
    <Transition from="GRAB_MARIO" to="THROW_MARIO" event="throw_start"/>
    <Transition from="THROW_MARIO" to="COOLDOWN" event="throw_finish"/>
    <Transition from="COOLDOWN" to="IDLE" event="cooldown_finish"/>
    
    <Transition from="IDLE" to="DEATH" event="hit_wall"/>
    <Transition from="CHASE" to="DEATH" event="hit_wall"/>
    <Transition from="RETURN_HOME" to="DEATH" event="hit_wall"/>
    <Transition from="GRAB_MARIO" to="DEATH" event="hit_wall"/>
    <Transition from="THROW_MARIO" to="DEATH" event="hit_wall"/>
    <Transition from="COOLDOWN" to="DEATH" event="hit_wall"/>
</Transitions>

********************************************************
Error output：There are multiple nodes in the same state
********************************************************

<root>
    <Sequence> 
        <Fallback—entry state IDLE>
            <Condition_init_done/>
            <Sequence>
            
            ********************************************************
            Repeated structures lead to logical errors
            ********************************************************
                <Action_IDLE/>
                <Fallback—sequecne CHASE>
                    <Condition_mario_near/>
                    <Sequence>
                        <Action_CHASE/>
                        <Fallback—sequecne RETURN_HOME>
                            < Condition _too_far_from_home/>
                            < Action _RETURN_HOME/>
                        </Fallback-- sequecne RETURN_HOME>
                    </Sequence>
                </Fallback-- sequecne CHASE>
            </Sequence>
        </Fallback—entry state IDLE>
        
        ********************************************************
        Repeated structures lead to logical errors
        ********************************************************
        
        <Fallback—loop state IDLE>
            <Condition mario_far_arrived_home_cooldown_finish/>
            <Action_IDLE/>
        </Fallback-- loop state IDLE>
        
        <Fallback—loop state GRAB_MARIO>
            <Condition_catch_mario/>
            <Sequence>
              <Action_GRAB_MARIO/>
              <Fallback--sequecne THROW_MARIO>
                <Condition_throw_start/>
                <Sequence>
                    <Action_THROW_MARIO/>
                    <Fallback--sequecne COOLDOWN>
                        <Condition_throw_finish/>
                        <Action_COOLDOWN/>
                    </Fallback-- sequecne COOLDOWN>
                </Sequence>
            </Fallback--sequecne THROW_MARIO>
        </Sequence>
      </Fallback—loop state GRAB_MARIO>
      <Fallback—loop state DEATH>
        <Condition_hit_wall/>
        <Action_DEATH/>
      </Fallback—loop state DEATH>
    </Sequence>
</root>

Enter a prompt: Each state is mapped to a single node in the LEBT;
if identical nodes appear in the LEBT, they are merged and the LEBT is regenerated.

Correct output：
output1:
<root>
    <Sequence>
        <Fallback—entry state IDLE>
            <Condition_init_done_mario_far_arrived_home_cooldown_finish/>
            <Sequence>
                <Action_IDLE/>
                <Fallback--sequecne CHASE>
                    <Condition_mario_near/>
                    <Sequence>
                        <Action_CHASE/>
                        <Fallback--sequecne RETURN_HOME>
                            <Condition_too_far_from_home/>
                            <Action_RETURN_HOME/>
                        </Fallback--sequecne RETURN_HOME>
                    </Sequence>
                </Fallback--sequecne CHASE>
            </Sequence>
        </Fallback—entry state IDLE>
        <Fallback—loop state GRAB_MARIO>
            <Condition_catch_mario/>
            <Sequence>
                <Action_GRAB_MARIO/>
                <Fallback--sequecne THROW_MARIO>
                    <Condition_throw_start/>
                    <Sequence>
                        <Action_THROW_MARIO/>
                        <Fallback--sequecne COOLDOWN>
                            <Condition_throw_finish/>
                            <Action_COOLDOWN/>
                        </Fallback-- sequecne COOLDOWN>
                    </Sequence>
                </Fallback--sequecne THROW_MARIO>
            </Sequence>
        </Fallback—loop state GRAB_MARIO>
        <Fallback—loop state DEATH>
            <Condition_hit_wall/>
            <Action_DEATH/>
        </Fallback—loop state DEATH>
    </Sequence>
</root>

"""



