from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import datetime

from MongoDB_Main import SensorDocument, ControllerDocument

# MongoDB
db_sensordoc = SensorDocument()
db_controllerdoc = ControllerDocument()


def do_things():
    count = 0
    # MongoDB Controller Document
    controller = db_controllerdoc.controller_config()[0]
    client = ModbusClient(method=controller["Method"], port=controller["COMPort"],
                          timeout=controller["timeout"], stopbits=controller["stopbit"],
                          bytesize=controller["bytesize"], parity=controller["Parity"],
                          baudrate=controller["BaudRate"])
    client.connect()
    # MongoDB Sensor Document
    sensor = db_sensordoc.sensor_config()

    # Sensor values in list
    Sensor_Data = []
    for i in range(0, len(sensor)):
        # Reading Analog Inputs
        Register_Data = client.read_input_registers(address=sensor[i]["Address"], count=1, unit=2)
        Data = Register_Data.registers[0]/10
        Sensor_Data.append(Data)

    # Push MongoDB
    db_sensordoc.field_config(Sensor_Data)
    count += 1
    print("Number of Iteration: {0}".format(count))
    # Live Sensor Values
    print("Controller Type: {0} \nError message: {1}".format(controller["ControllerType"],controller["ErrorMsg"]))
    print("Sensor Values: {0} \nTotal No. of Sensors: {1}".format(Sensor_Data, len(Sensor_Data)))
    print("________________________________________________________________________________________")
    Sensor_Data.clear()
    client.close()
    time.sleep(1)


while True:
    try:
        do_things()
    except Exception as ex:
        print("\nCaught exception {}".format(ex))
        print("Retrying...")
        print("!! Check the Modbus Connection !!")
        print("Auto-Restart in", end=" ")
        for i in range(10, -1, -1):
            print(i, end=" ")
            time.sleep(1)
    finally:
        ts = datetime.datetime.now()
        timestamp = ts.astimezone().isoformat(timespec='milliseconds').replace('+05:30', 'Z')
        print("\nTimeStamp: ", timestamp)