
Wed Jul  5 15:38:27 2023
F1 Unix: 1688593107
FFF Function: _ZN2ft24TxtDeliveryPickupStation6is_DINEv
arguments:  
arg_values: -1090522376
Wed Jul  5 15:38:27 2023
TB Unix: 1688593107
loaded values: 1
Wed Jul  5 15:38:20 2023
CF Unix: 1688593100
Called from: _ZN2ft32TxtDeliveryPickupStationObserver6UpdateEPNS_15SubjectObserverE _ZN2ft24TxtDeliveryPickupStation6is_DINEv callInst_values: -1
# This is delivery underflow

Wed Jul  5 15:38:32 2023
F1 Unix: 1688593112
Function: TxtMqttFactoryClient13publishVGR_Do
arguments:   , %"class.ft::TxtMqttFactoryClient"* %this , %"class.ft::TxtMqttFactoryClient"* %thisi32 %code , %"class.ft::TxtMqttFactoryClient"* %thisi32 %code%"class.ft::TxtWorkpiece"* %wp
arg_values: -1090521784 ,3 ,-1090522096 ,5000
TxtMqttFactoryClient::publishVGR_Do called.
# The publishVGR_Do is the function that is publishing the topic and the buffer function below is created by the IR, that's why ignoring this rewritting the function names.

Wed Jul  5 15:39:04 2023
F1 Unix: 1688593146
F: mqtt10buffer_ref
arguments:   , %"class.mqtt::buffer_ref"* %this
arg_values: -1289755496 ,-1289755352
publish get_topic value:  fl/vgr/do

Wed Jul  5 15:39:06 2023
F1 Unix: 1688593146
Function: message_arrived
arguments:   , %class.callback* %this
arg_values: -1090522788 ,-1279275668
# In the middle there are multiple conditions and function calls between message_arrived function till receiving the topic
Wed Jul  5 15:39:06 2023
CF Unix: 1688593146
Called from: message_arrived basic_string callInst_values: 2137177532
message_arrived get_topic value:  fl/hbw/ack



Wed Jul  5 15:38:32 2023
F1 Unix: 1688593112
Function: TxtMqttFactoryClient17publishStateOrder
arguments:   , %"class.ft::TxtMqttFactoryClient"* %this , %"class.ft::TxtMqttFactoryClient"* %this[2 x i32] %ord_state.coerce
arg_values: -1090521784 ,5000 ,-1289750256

Wed Jul  5 15:39:06 2023
F1 Unix: 1688593146
F: mqtt10buffer_ref
arguments:   , %"class.mqtt::buffer_ref"* %this
arg_values: -1289755376 ,-1289755400
publish get_topic value:  f/i/order

Wed Jul  5 15:37:03 2023
F1 Unix: 1688593146
Function: message_arrived
arguments:   , %class.callback* %this
arg_values: -1090522788 ,-1279275668
# In the middle there are multiple conditions and function calls between message_arrived function till receiving the topic
Wed Jul  5 15:37:06 2023
CF Unix: 1688593146
Called from: message_arrived basic_string callInst_values: 2137177532
message_arrived get_topic value:  f/o/order




Wed Jul  5 15:38:32 2023
F1 Unix: 1688593112
Function: TxtMqttFactoryClient13publishVGR_Do
arguments:   , %"class.ft::TxtMqttFactoryClient"* %this , %"class.ft::TxtMqttFactoryClient"* %thisi32 %code , %"class.ft::TxtMqttFactoryClient"* %thisi32 %code%"class.ft::TxtWorkpiece"* %wp
arg_values: -1090521784 ,3 ,-1090522096 ,5000
TxtMqttFactoryClient::publishVGR_Do called.
# The publishVGR_Do is the function that is publishing the topic and the buffer function below is created by the IR, that's why ignoring this rewritting the function names.

Wed Jul  5 15:39:06 2023
F1 Unix: 1688593146
F: mqtt10buffer_ref
arguments:   , %"class.mqtt::buffer_ref"* %this
arg_values: -1289755496 ,-1289755352
publish get_topic value:  fl/vgr/do

Wed Jul  5 15:39:06 2023
F1 Unix: 1688593146
Function: message_arrived
arguments:   , %class.callback* %this
arg_values: -1090522788 ,-1279275668
# In the middle there are multiple conditions and function calls between message_arrived function till receiving the topic
Wed Jul  5 15:39:06 2023
CF Unix: 1688593146
Called from: message_arrived basic_string callInst_values: 2137177532
message_arrived get_topic value:  fl/hbw/ack



#vgr file




#initially
Table: 0 0 0 0 0 0 0 0 0

# 676689
Wed Jul  5 15:39:00 2023
F1 Unix: 1688593140
Function: TxtHighBayWarehouse24requestVGRfetchContainer
arguments:   , %"class.ft::TxtHighBayWarehouse"* %this
arg_values: -1090522400 ,2137081336

# 676760
FETCH_CONTAINER

Wed Jul  5 15:38:06 2023
F1 Unix: 1688593086
Function: TxtHighBayWarehouse14fetchContainer
arguments:  
arg_values: -1090522400

# 677089
Wed Jul  5 15:38:30 2023
F1 Unix: 1688593110
Function: TxtHighBayWarehouseStorage14fetchContainer
Position: 0 0
Table: 1 0 0 0 0 0 0 0 0
arguments:  
arg_values: -1090522104
Wed Jul  5 15:38:30 2023
TB Unix: 1688593110
loaded values: 0
[i][j]: 02
Wed Jul  5 15:38:30 2023
FB Unix: 1688593110
loaded values: 0
Wed Jul  5 15:38:30 2023
FB Unix: 1688593110
loaded values: 2

Wed Jul  5 15:38:30 2023
F1 Unix: 1688593110
Function: TxtHighBayWarehouseStorage10isValidPos
arguments:   , %"class.ft::TxtHighBayWarehouseStorage"* %this
arg_values: -1090522104 ,-1289751472
Wed Jul  5 15:38:30 2023
CF Unix: 1688593110
Called from: TxtHighBayWarehouseStorage14fetchContainer TxtHighBayWarehouseStorage10isValidPos callInst_values: -1



Wed Jul  5 15:39:00 2023
F1 Unix: 1688593140
Function: message_arrived
arguments:   , %class.callback* %this
arg_values: -1090522412 ,-1279275668

Wed Jul  5 15:39:00 2023
CF Unix: 1688593140
Called from: message_arrived basic_string callInst_values: 2137080548
message_arrived get_topic value:  fl/vgr/do



Wed Jul  5 15:39:00 2023
F1 Unix: 1688593140
Function: mqtt10buffer_ref
arguments:   , %"class.mqtt::buffer_ref"* %this
arg_values: -1289753624 ,-1289753480
publish get_topic value:  fl/hbw/ack

# collision part - ordering from position 1,0
Wed Jul  5 15:39:00 2023
F1 Unix: 1688593140
Function: message_arrived
arguments:   , %class.callback* %this
arg_values: -1090522412 ,-1279275668

Wed Jul  5 15:39:00 2023
CF Unix: 1688593140
Called from: message_arrived basic_string callInst_values: 2137058156
message_arrived get_topic value:  fl/vgr/do
Wed Jul  5 15:39:00 2023
CF Unix: 1688593140
Called from: message_arrived char_traits callInst_values: -1

# FSM_TRANSITION global variable value changed and this function is called. This value is changed after the message_arrived function get the topic.
Wed Jul  5 15:39:00 2023
F1 Unix: 1688593140
Function: TxtHighBayWarehouse15requestVGRfetch
arguments:   , %"class.ft::TxtHighBayWarehouse"* %this
arg_values: -1090522400 ,2137080168

# fetch function called
Wed Jul  5 15:38:06 2023
F1 Unix: 1688593086
Function: TxtHighBayWarehouse5fetch
arguments:   , %"class.ft::TxtHighBayWarehouse"* %this
arg_values: -1090522400 ,1

#storage fetch function
Wed Jul  5 15:38:30 2023
F1 Unix: 1688593110
Function: TxtHighBayWarehouseStorage5fetch
Position: 1 0
Table: 1 0 0 0 0 0 0 0 0
arguments:   , %"class.ft::TxtHighBayWarehouseStorage"* %this
arg_values: -1090522104 ,1
Wed Jul  5 15:38:30 2023
TB Unix: 1688593110
loaded values: 2137079968
Wed Jul  5 15:38:30 2023
FB Unix: 1688593110
loaded values: 1
[i][j]: 02
wp[i][j]->type: Wed Jul  5 15:38:30 2023
TB Unix: 1688593110
loaded values: 2137079968
Wed Jul  5 15:38:30 2023
TB Unix: 1688593110
loaded values: 1
1
Wed Jul  5 15:38:30 2023
FB Unix: 1688593110
loaded values: 1
Wed Jul  5 15:38:30 2023
FB Unix: 1688593110
loaded values: 0

Wed Jul  5 15:38:30 2023
F1 Unix: 1688593110
Function: TxtHighBayWarehouseStorage10isValidPos 57241
arguments:   , %"class.ft::TxtHighBayWarehouseStorage"* %this
arg_values: -1090522104 ,-1289751472
Wed Jul  5 15:38:30 2023
CF Unix: 1688593110
Called from: TxtHighBayWarehouseStorage5fetch TxtHighBayWarehouseStorage10isValidPos callInst_values: -1

# The hbw will publish acychornization 779776
Wed Jul  5 15:38:32 2023
F1 Unix: 1688593112
Function: TxtMqttFactoryClient14publishHBW_Ack
arguments:   , %"class.ft::TxtMqttFactoryClient"* %this , %"class.ft::TxtMqttFactoryClient"* %thisi32 %code , %"class.ft::TxtMqttFactoryClient"* %thisi32 %code%"class.ft::TxtWorkpiece"* %wp
arg_values: -1090521784 ,1 ,2137081336 ,5000

Wed Jul  5 15:39:00 2023
F1 Unix: 1688593140
Function: mqtt10buffer_ref
arguments:   , %"class.mqtt::buffer_ref"* %this
arg_values: -1289753624 ,-1289753480
publish get_topic value:  fl/hbw/ack

#hbw file
