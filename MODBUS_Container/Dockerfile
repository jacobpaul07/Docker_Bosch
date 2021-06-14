FROM python:3.9

ADD databaseconfig.py /
ADD MongoDB_Main.py /
ADD Modbus_MongoDB.py /


RUN pip install pymongo
RUN pip install pymodbus
RUN pip install dnspython

CMD [ "python", "./Modbus_MongoDB.py" ]
