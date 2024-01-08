## 1 Data

3 retrievals:

- F1: `1retrieval.txt`
- F2: `2retrieval.txt`
- F3: `3retrieval.txt`

## 2 Unique functions

### 2.1 Unique functions in F1

1. Unique functions in F1, neither in F2 nor F3:

```txt
# Header files
_GLOBAL__sub_I_TxtHighBayWarehouse.cpp
_GLOBAL__sub_I_TxtHighBayWarehouseRun.cpp
_GLOBAL__sub_I_TxtHighBayWarehouseStorage.cpp
_GLOBAL__sub_I_TxtConveyorBelt.cpp
_GLOBAL__sub_I_TxtAxisNSwitch.cpp
_GLOBAL__sub_I_TxtHighBayWarehouseCalibData.cpp

# File loading stage
_ZN2ft19TxtHighBayWarehouseC2EPNS_11TxtTransferEPNS_20TxtMqttFactoryClientE - TxtHighBayWarehouse_TxtTransfer_TxtMqttFactoryClient 
_ZN2ft14TxtAxisNSwitchC2ENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEPNS_11TxtTransferEhhh - TxtAxisNSwitch_basic_string_char_traits_TxtTransfer
_ZN2ft7TxtAxis12configInputsEh - TxtAxis_configInputs 
_ZN2ft28TxtConveyorBeltLightBarriersC2EPNS_11TxtTransferEhii - TxtConveyorBeltLightBarriers_TxtTransfer 
_ZN2ft15TxtConveyorBeltC2EPNS_11TxtTransferEh - TxtConveyorBelt_TxtTransfer 
_ZN2ft26TxtHighBayWarehouseStorageC2Ev - TxtHighBayWarehouseStorage
_ZN2ft26TxtHighBayWarehouseStorage16loadStorageStateEv - TxtHighBayWarehouseStorage_loadStorageState 
# These functions were called from `loadStorageState` to get the workpiece state in string format - https://github.com/fischertechnik/txt_training_factory/blob/27526cc803ebfcecd1163de31f0e3c6d25f65ca8/TxtSmartFactoryLib/src/TxtHighBayWarehouseStorage.cpp#L82-L85
_ZN2ft12TxtWorkpieceC2ENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_11TxtWPType_tENS_12TxtWPState_tE - TxtWorkpiece_basic_string_char_traits_TxtWPType_TxtWPState
_ZN2ft12TxtWorkpieceC2ENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_11TxtWPType_tENS_12TxtWPState_tE - TxtWorkpiece_basic_string_char_traits_TxtWPType_TxtWPState
_ZN2ft28TxtHighBayWarehouseCalibDataC2Ev - TxtHighBayWarehouseCalibData 
_ZN2ft28TxtHighBayWarehouseCalibData4loadEv - TxtHighBayWarehouseCalibData_load 
_ZN8callbackC1ERN2ft20TxtMqttFactoryClientERNS0_19TxtHighBayWarehouseE - callback_TxtMqttFactoryClient_TxtHighBayWarehouse 

# This function TxtHighBayWarehouse_run will start after the hbw is started and it will keep running
_ZN2ft19TxtHighBayWarehouse3runEv - TxtHighBayWarehouse_run 
_ZN2ft27TxtHighBayWarehouseObserverC2EPNS_19TxtHighBayWarehouseEPNS_20TxtMqttFactoryClientE - TxtHighBayWarehouseObserver_TxtHighBayWarehouse_TxtMqttFactoryClient 
_ZN2ft19TxtHighBayWarehouse10getStorageEv - TxtHighBayWarehouse_getStorage 
_ZN2ft34TxtHighBayWarehouseStorageObserverC2EPNS_26TxtHighBayWarehouseStorageEPNS_20TxtMqttFactoryClientE - TxtHighBayWarehouseStorageObserver_TxtHighBayWarehouseStorage_TxtMqttFactoryClient 
```

### 2.2 Unique functions in F2

1. Unique functions in F2, neither in F1 nor F3: **None**
2. Functions in F2, **NOT** in F1, but **IN** F3:

```txt
# PUT BACK PHASE: After giving the workpiece to the vgr, it will store the empty container back to the storage. Then this function `TxtAxis1RefSwitch_moveRefThread` will be executed if a switch is pressed.
# Storing empty container back to the storage.
_ZN2ft17TxtAxis1RefSwitch13moveRefThreadEv - TxtAxis1RefSwitch_moveRefThread
_ZN2ft17TxtAxis1RefSwitch13moveRefThreadEv - TxtAxis1RefSwitch_moveRefThread
_ZN2ft17TxtAxis1RefSwitch7moveRefEv - TxtAxis1RefSwitch_moveRef
_ZN2ft17TxtAxis1RefSwitch7moveRefEv - TxtAxis1RefSwitch_moveRef
_ZN2ft7TxtAxis8setSpeedEs - TxtAxis_setSpeed
_ZN2ft7TxtAxis8setSpeedEs - TxtAxis_setSpeed
_ZN2ft7TxtAxis8setSpeedEs - TxtAxis8setSpeed
_ZN2ft17TxtAxis1RefSwitch13moveRefThreadEv - TxtAxis1RefSwitch_moveRefThread
_ZN2ft17TxtAxis1RefSwitch13moveRefThreadEv - TxtAxis1RefSwitch_moveRefThread
_ZN2ft17TxtAxis1RefSwitch7moveRefEv - TxtAxis1RefSwitch_moveRef
_ZN2ft17TxtAxis1RefSwitch7moveRefEv - TxtAxis1RefSwitch_moveRef

# Dependencies: functions from header files like `will_options.h`, `message.h`
_ZNK4mqtt7message15get_payload_strB5cxx11Ev - mqtt_message_get_payload_str
_ZN2ft20trycheckTimestampTTLERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEd - ft_trycheckTimestamp_basic_string_char_traits - 
_ZN2ft15trygettimepointERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE - ft_trygettimepoint_basic_string_char_traits - 
_ZN2ft11time_offsetEv - ft_time_offset
_ZN2ft12TxtWorkpieceD0Ev - ft_TxtWorkpiece
_ZN2ft12TxtWorkpieceD2Ev - ft_TxtWorkpiece
_ZNK4mqtt7message15get_payload_strB5cxx11Ev - mqtt_message_get_payload_str
_ZN2ft20trycheckTimestampTTLERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEd - trycheckTimestamp_basic_string_char_traits - 
_ZN2ft15trygettimepointERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE - trycheckTimestamp_basic_string_char_traits - 
_ZN2ft11time_offsetEv - time_offset
_ZNK4mqtt7message15get_payload_strB5cxx11Ev - mqtt_message_get_payload_str - 
_ZN2ft20trycheckTimestampTTLERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEd - trycheckTimestamp_basic_string_char_traits - 
_ZN2ft15trygettimepointERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE - trygettimepoint_basic_string_char_traits
_ZN2ft11time_offsetEv - time_offset
```

### 2.3 Unique functions in F3

1. Unique functions in F3, neither in F1 nor F2: **None**
2. Functions in F3, **NOT** in F1, but **IN** F2:

```txt
# Put back phase: Same functions in F2
_ZN2ft17TxtAxis1RefSwitch13moveRefThreadEv
_ZN2ft17TxtAxis1RefSwitch13moveRefThreadEv
_ZN2ft17TxtAxis1RefSwitch7moveRefEv
_ZN2ft17TxtAxis1RefSwitch7moveRefEv
_ZN2ft7TxtAxis8setSpeedEs
_ZN2ft7TxtAxis8setSpeedEs
_ZN2ft7TxtAxis8setSpeedEs
_ZN2ft17TxtAxis1RefSwitch13moveRefThreadEv
_ZN2ft17TxtAxis1RefSwitch13moveRefThreadEv
_ZN2ft17TxtAxis1RefSwitch7moveRefEv
_ZN2ft17TxtAxis1RefSwitch7moveRefEv

# Dependencies: same as F2
_ZNK4mqtt7message15get_payload_strB5cxx11Ev
_ZN2ft20trycheckTimestampTTLERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEd
_ZN2ft15trygettimepointERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
_ZN2ft11time_offsetEv
_ZN2ft12TxtWorkpieceD0Ev
_ZN2ft12TxtWorkpieceD2Ev
_ZNK4mqtt7message15get_payload_strB5cxx11Ev
_ZN2ft20trycheckTimestampTTLERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEd
_ZN2ft15trygettimepointERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
_ZN2ft11time_offsetEv
_ZNK4mqtt7message15get_payload_strB5cxx11Ev
_ZN2ft20trycheckTimestampTTLERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEd
_ZN2ft15trygettimepointERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
_ZN2ft11time_offsetEv
```

which are the same as the result in 2.2.2.

## 3 Common Patterns in Different Orders

Use F1 and F2 as samples.

There are 3 main types of patterns which contain a large number of repeated functions:

- T1: repeated 1 function: `_ZN2ft19TxtHighBayWarehouse7fsmStepEv`
- T2: repeated 1 function: `_ZN2ft7TxtAxis15isSwitchPressedEh`

- T3: repeated 

  ```txt
# fsmStep: Finite State Machine - Its a loop that keeps running until the txt controller is stopped.
  _ZN2ft19TxtHighBayWarehouse7fsmStepEv - TxtHighBayWarehouse_fsmStep
# Prints the state of the machine
  _ZN2ft19TxtHighBayWarehouse10printStateENS0_7State_tE - TxtHighBayWarehouse_printState
# Converts the state into string, it is called from printState
  _ZN2ft19TxtHighBayWarehouse8toStringENS0_7State_tE - TxtHighBayWarehouse_toString_State
  ```

### 3.1 Common Patterns in Different Orders

In F1, the order of these 3 main pattern types is: T1, T2, T3, T2

In F2, the order of these 3 main pattern types is: T2, T1, T2, T3, T2

(ignoring some small patterns).

# `_ZN2ft7TxtAxis15isSwitchPressedEh` function checks if the switch is pressed for the PUT BACK PHASE
The order of T1 and T2, i.e. repeated `_ZN2ft19TxtHighBayWarehouse7fsmStepEv` and repeated `_ZN2ft7TxtAxis15isSwitchPressedEh`, may vary.

### 3.2 Common Prefix

Function sequences commonly shown in both F1 and F2, before the different patterns.

```txt
# Checks the status of the subject e.g., hbw, vgr, sorting line
_ZN2ft18TxtSimulationModel9getStatusEv
# checks if the subject is active 
_ZN2ft18TxtSimulationModel8isActiveEv
# publishes the state so that other subjects or controllers can know the current status of the subject
_ZN2ft20TxtMqttFactoryClient15publishStateHBWENS_13TxtLEDSCode_tENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEliS7_
_ZN2ft20TxtMqttFactoryClient19publishStateStationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_13TxtLEDSCode_tES6_liS6_
_ZN2ft9getnowstrEPc
_ZN2ft10gettimestrEliPc
_ZN4mqtt10buffer_refIcEC2ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
_ZN4mqtt10buffer_refIcEC2EONSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
_ZN4mqtt12make_messageENS_10buffer_refIcEES1_

# Other subjects/controllers e.g., vgr, hbw will listen to the published state
_ZN2ft23action_listener_publish10on_successERKN4mqtt5tokenE
_ZNK4mqtt17string_collection5emptyEv
_ZNK4mqtt17string_collection4sizeEv
_ZNK4mqtt17string_collectionixB5cxx11Ej
_ZNK4mqtt17string_collection4sizeEv
_ZN8callback17delivery_completeESt10shared_ptrIN4mqtt14delivery_tokenEE
_ZN4mqtt7messageD2Ev
_ZN4mqtt10buffer_refIcED2Ev
_ZN4mqtt10buffer_refIcED2Ev
```

### 3.3 Common Suffix

According to 3.1, the pattern types T3, T2 shown in both F1 and F2, i.e. the common suffix of F1 and F2 is repeated: 

```txt
# Same as T3: repeated 
_ZN2ft19TxtHighBayWarehouse7fsmStepEv
_ZN2ft19TxtHighBayWarehouse10printStateENS0_7State_tE
_ZN2ft19TxtHighBayWarehouse8toStringENS0_7State_tE
```

and then repeated `_ZN2ft7TxtAxis15isSwitchPressedEh`

(Including but not limited to).
