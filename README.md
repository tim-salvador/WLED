# WLED
WLED configs and presets

wled-serial-cmd.py< is ran by retropie during game loads to update the led matrix.  it uses the runcommand-onstart.sh file to exec.
- /opt/retropie/configs/all/runcommand-onstart.sh
```
#!/bin/bash
/usr/bin/python3 /home/pi/wled_matrix_updater/wled-serial-cmd.py $1 $2 $3
```
