# Python UI library for Servo Arm Controller project
Used for interfacing with the controller.
To start the program, run ```main.py```.
To exit, type "end" in the active terminal.
<br>
***Attention! do not exit the program via interruption (e.g Ctrl+C), the serial port might not be released and the threads can hang.***
If the previusly mentioned happens, the python runtime environment has to be halted manually.
<br>
Animation data is stored in ```animations.py```.
<br>
### Commands
All commands are enterd from the active command line / terminal as strings. The following are valid:
- "wave" - executes position initialisation animation, as specified in ```animations.py```.
- "wave" - executes waving animation, as specified in ```animations.py```.
- "h" or "high" - executes high value state animation, back and forth.
- "l" or "low" - executes low value state animation, back and forth.
- "debug on" and "debug off" - sets the amount of information to ask from the controller on next command.
- "end" - exits the program politely.
