# Parser for Logic Port CSV Export
Parses the csv export file from [logic port](http://www.pctestinstruments.com/index.htm) measurement of [UAVCAN](http://uavcan.org/) data and extracts [meta data](http://uavcan.org/Specification/4._CAN_bus_transport_layer/) .

## Input
Input csv file should look like this (important is the `CAN` coloumn):
```
"SampleNumber","CAN","CAN Raw Data","CAN Bit Sequence","CANH"
"0","","","","0"
"51","","","","1"
"300","","","","0"
"351","","","","1"
"600","","","","0"
"651","","","","1"
"900","","","","0"
...
"4450","","","","0"
"5800","D:268522852","0","1","1"
"5850","","1","2","0"
...
```

## Output
Output will look like:
```
new message found:
  identifier raw = 10000000000010101010101100100
  priority = 16
  message type ID = 341
  service = 0
  source node ID = 100
  data length = 8
  tailbyte raw = 11000000
  start of transfer = 1
  end of transfer = 1
  toogle byte = 0
  transfer ID = 0
  checksum = 23302
  ```
## Interpreter Settings
There should at least be one interpreter with the Name `CAN` and displayed as `Interpreted Data`:
![Image of Interpreter Settings](https://raw.githubusercontent.com/tum-phoenix/drive_helper_uavcan_from_logic_port/master/can_interpeter.png)
