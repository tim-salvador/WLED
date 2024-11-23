`add picture here`

# Why
- Customizable
- Cost effective

# Parts
## Hardware
- 2ct 10' x 1" PVC pipe (prob could use smaller diameter but wanted to see if mounting xconnectors is possible)
- 8ct 1" 45º connector
- 3ct = 1" T connector

## Electronics
- 1 ESP8266 (I used a 8266 NodeMCU but any ESP will work)
- 4ct 50ct ws2815 ext rated LED strips (12V)
- 4ct male 3 pin xconnect extension
- 4ct female 3 pin xconnect extension
- 1ct 12V 3A power supply
- 1ct 18G Fuse
- 1ct Shift Leveler

# Diagram
```
BASE
            5
       A -- T -- A
 6   /      |      \   4
    A       |       A
7   |       T       |   3
    A       |       A
 8   \      |      /   2
       A -- T -- A
            1
```
A = angled connector
T = T connector
| and -- = 1" pipe

# Build
1. Each strip will cover opposite ends of the tree.
   Data In | Data Out
   - 1 and 5 
   - 4 and 8
   - 7 and 3
   - 2 and 5
