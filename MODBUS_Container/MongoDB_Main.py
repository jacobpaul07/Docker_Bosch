from databaseconfig import Databaseconfig
import databaseconfig as dbc


class SensorDocument:

    def __init__(self):
        connection = Databaseconfig()
        connection.connect()
        db = dbc.client["Bosch"]
        self.collection = db["Sensor_Data"]

    def sensor_config(self):
        v = self.collection.find()
        list = []
        for i in v:
            value = i
            list.append(value)
        return list

    def field_config(self, parameter):
        v = self.collection.find()
        list = []
        for i in v:
            value = i
            list.append(value)
        length = len(list)

        for i in range(0, length):
            self.collection.find_one_and_update(
                {"_id": list[i]["_id"]},
                {"$set":
                    {"TagValue": parameter[i]}
                 }, upsert=True
            )


class ControllerDocument:

    def __init__(self):
        connection = Databaseconfig()
        connection.connect()
        db = dbc.client["Bosch"]
        self.collection = db["Controller"]

    def controller_config(self):
        v = self.collection.find()
        list = []
        for i in v:
            value = i
            list.append(value)
        return list




