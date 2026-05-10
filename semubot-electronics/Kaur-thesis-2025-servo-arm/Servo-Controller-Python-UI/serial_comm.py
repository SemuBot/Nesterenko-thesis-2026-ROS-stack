import serial
import serial.tools.list_ports as lp
import time
import numpy as np
import animations
import threading

#Serial communication handler object

class SerCom():

    def __init__(self, baudrate=19200, automatic_con = True, target_device = "COM5"):
        self.baudrate = baudrate
        self.ser = None
        self.ports = (list(lp.comports()))
        self.connected = False
        self.auto_con = automatic_con
        self.device = target_device
        self.animation = "init"
        self.animation_data = []
        self.animation_active = False
        self.enabled = True

        self.thread1 = None
        self.thread2 = None
        self.thread3 = None

        for port in self.ports:
            print(f"{port.device} : {port.name}, [{port.description}]")
            if(self.auto_con):
                if str(port.device)[0:2] == "COM" and self.connected == False:
                    print(f"Trying to connnect to port {port.device}")
                    self.ser = serial.Serial(port.device, baudrate=19200)
                    self.ser.open()
                    print(f"Connected to port: {port.device}")
                    self.connected = True

                else:
                    print("Ignoring current port.")

            else:
                if str(port.device) == self.device and self.connected == False:
                    print(f"Trying to connnect to port {port.device}")
                    self.ser = serial.Serial(port.device, baudrate=19200)
                    print(f"Connected to port: {port.device}")
                    self.connected = True

                else:
                    print("Ignoring current port.")

        if not self.connected:
            print("Could not find suitable COM port. Check your device or port name")
        
        else:
            self.thread1 = threading.Thread(target=self.read_port)
            self.thread2 = threading.Thread(target=self.handle_input)
            self.thread3 = threading.Thread(target=self.handle_animation)

            print("Threads are up!")

    #meant to be threaded (thread1)
    def read_port(self):

        while(self.enabled):
            try:
                bytes_waiting = self.ser.in_waiting
                if(bytes_waiting):
                    #print("Incoming data: " + str(bytes_waiting) + " bytes.")
                    line = self.ser.read_until(b'\n')
                    #print("Bytes read: " + str(line))
                    print(str(line.decode("ascii")))
                    bytes_waiting = 0

                else:
                    time.sleep(200/1000)
                
                if(not self.enabled):
                    #release serial connection
                    self.ser.close()
                    print("Serial connection closed.")
                    break

            except KeyboardInterrupt:
                print("Shutting down serial comms")
                self.enabled = False

            

        
    
    #meant to be called within thread3
    def write_to_serial(self, data):
        #self.ser.flush()
        data_bytes = bytearray(data)
        print(data_bytes)
        code = self.ser.write(data_bytes)
        print("Write done. code: " + str(code))


    #meant to be threaded (thread2)
    def handle_input(self):
        while(self.enabled):

            try:
                self.animation = input("Specify animation by name: ")
                self.animation_active = True

                while(self.animation_active):
                    #wait until animation is finished
                    try:
                        time.sleep(10/1000)
                    except KeyboardInterrupt:
                        # Please don't use this. Probably won't work anyway
                        print("Cancelling animation progress")
                        self.animation = ""
                        self.animation_active = False

                self.animation = ""
                print("previous command done")

                if(not self.enabled):
                    break

            except KeyboardInterrupt:
                self.enabled = False
            except EOFError:
                print("Erroneous input. Did you mean 'end'?")

            

    #meant to be threaded (thread3)
    def handle_animation(self):
        debug = 0
        while(self.enabled):
            try:

                if self.animation_active:
                    if self.animation == "init":
                        #do animation here
                        self.animation_data = animations.animation_init(speedmult = 1, debug=debug)
                        #run the animation
                        self.run_animation()
                        #deactivate when done
                        self.animation_active = False

                    #continue with elifs
                    elif self.animation == "wave":
                        self.animation_data = animations.animation_wave(speedmult = 1, debug=debug)
                        self.run_animation()
                        self.animation_active = False

                    elif self.animation == "h" or self.animation == "high":
                        self.animation_data = animations.animation_highend(speedmult = 1, debug=debug)
                        self.run_animation()
                        self.animation_active = False
                        
                    elif self.animation == "l" or self.animation == "low":
                        self.animation_data = animations.animation_lowend(speedmult = 1, debug=debug)
                        self.run_animation()
                        self.animation_active = False

                    # DEBUG switching
                    elif(self.animation == "debug on"):
                        debug = 1
                        self.animation = ""
                        print("Debug is switched on.")
                        self.animation_active = False

                    elif(self.animation == "debug off"):
                        debug = 0
                        self.animation = ""
                        print("Debug is switched off.")
                        self.animation_active = False

                    #IMPORTANT! input to close the proram === "end" 
                    elif(self.animation == "end"):
                        self.enabled = False
                        self.animation_active = False

                    #else just sleep awhile and make sure not to get stuck
                    else:
                        print("Stupidity avoidance executed.")
                        time.sleep(0.01)
                        self.animation_active = False

            except KeyboardInterrupt:
                self.enabled = False

                if(not self.enabled):
                        break

            
        
    def run_animation(self):
        for i in range(len(self.animation_data)):
            # communicate over serial
            # conversions are done on the board
            sleeptime = self.animation_data[i, -1]/1000

            print("Sending bytes...")
            self.write_to_serial(self.animation_data[i, 0:-1])
            
            #wait for the previousmove to finish
            time.sleep(sleeptime)