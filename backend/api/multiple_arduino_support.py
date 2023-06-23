import serial
from time import sleep

class MultipleArduinoSupport:
    def __init__(self, port_list):
        self.port_list = port_list
        self.arduinos = [serial.Serial(port, 9600) for port in port_list]

    def send_data_to_all(self, data):
        for arduino in self.arduinos:
            arduino.write(data.encode())
            sleep(0.1)

    def read_data_from_all(self):
        data_list = []
        for arduino in self.arduinos:
            data = arduino.readline().decode().strip()
            data_list.append(data)
        return data_list

if __name__ == "__main__":
    port_list = ["COM3", "COM4", "COM5"]
    arduino_manager = MultipleArduinoSupport(port_list)
    arduino_manager.send_data_to_all("Hello, Arduino!")
    data_list = arduino_manager.read_data_from_all()
    print(data_list)
