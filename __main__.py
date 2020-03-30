import socket
import sense_hat

ip = socket.gethostname()
port = 420

server = socket.socket()

while True:
    sensors = sense_hat.SenseHat()
    server.bind((ip, port))

    print("Bound to " + ip + ":" + str(port))

    server.listen()

    client, clientaddress = server.accept()
    print("Just connected to " + clientaddress)

    while client.getpeername() is not None:
        orientation = sensors.get_orientation_degrees()

        pitch = str(round(orientation["pitch"], 1))
        yaw = str(round(orientation["yaw"], 1))
        roll = str(round(orientation["roll"], 1))

        xyz = "|" + pitch + "|" + yaw + "|" + roll + "|"

        client.send(xyz.encode("UTF8"))
