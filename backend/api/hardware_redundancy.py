import serial
from time import sleep

class HardwareRedundancy:
    def __init__(self, primary_port, backup_port):
        self.primary_port = primary_port
        self.backup_port = backup_port
        self.primary_arduino = serial.Serial(primary_port, 9600)
        self.backup_arduino = serial.Serial(backup_port, 9600)

    def send_data(self, data):
        try:
            self.primary_arduino.write(data.encode())
            sleep(0.1)
        except serial.SerialException:
            self.backup_arduino.write(data.encode())
            sleep(0.1)

    def read_data(self):
        try:
            data = self.primary_arduino.readline().decode().strip()
        except serial.SerialException:
            data = self.backup_arduino.readline().decode().strip()
        return data

if __name__ == "__main__":
    primary_port = "COM3"
    backup_port = "COM4"
    hardware_manager = Hardware
