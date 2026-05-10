#python 3
#encoding utf-8


import time
import serial_comm


def main():
    Ser = serial_comm.SerCom(baudrate=19200, automatic_con=False, target_device="COM5")

    if(Ser.connected):
        Ser.thread1.start()
        Ser.thread2.start()
        Ser.thread3.start()

    while(Ser.enabled):
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            Ser.enabled = False

    if(Ser.thread1 is not None):
        Ser.thread1.join()
        print("Reading thread done.")

    if(Ser.thread2 is not None):
        Ser.thread2.join()
        print("Input thread done.")

    if(Ser.thread3 is not None):
        Ser.thread3.join()
        print("Animation thread done.")

    print("Programm closed successfully.")

    
if __name__ == "__main__":
    main()
    
    

