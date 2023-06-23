import serial
import time

class ArduinoCommunication:
    def __init__(self, port, baud_rate=9600):
        self.port = port
        self.baud_rate = baud_rate
        self.connection = None

    def connect(self):
        try:
            self.connection = serial.Serial(self.port, self.baud_rate)
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error connecting to Arduino: {e}")
            return False

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def send_data(self, data):
        if not self.connection:
            raise Exception("Arduino not connected")

        try:
            self.connection.write(data.encode())
        except Exception as e:
            print(f"Error sending data to Arduino: {e}")

    def read_data(self):
        if not self.connection:
            raise Exception("Arduino not connected")

        try:
            data = self.connection.readline().decode()
            return data.strip()
        except Exception as e:
            print(f"Error reading data from Arduino: {e}")
            return None

if __name__ == "__main__":
    arduino = ArduinoCommunication(port="COM3")
    if arduino.connect():
        print("Connected to Arduino")
        while True:
            try:
                data = input("Enter data to send: ")
                arduino.send_data(data)
                response = arduino.read_data()
                print("Received from Arduino:", response)
            except KeyboardInterrupt:
                break
        arduino.disconnect()
