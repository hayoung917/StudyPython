import paho.mqtt.client as mqtt
import Adafruit_DHT as dht
import json
import time
import datetime as dt
import uuid

from collections import OrderedDict

sensor = dht.DHT11
pin = 16
count = 0

try:
    dev_id = "LHY"
    #mqtt publisher
    broker_address = "210.119.12.52" #pc ip
    client2 = mqtt.Client(dev_id)
    client2.connect(broker_address)

    while True:
        count+=1
        currtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        #sensor value
        h,t = dht.read_retry(sensor,pin)

        #make groupdata
        raw_data = OrderedDict()
        raw_data["dev_id"] = dev_id
        raw_data["time"] = currtime
        raw_data["temp"] = "{0:0.1f}".format(t)
        raw_data["humid"] = "{0:0.1f}".format(h)

        pub_data = json.dumps(raw_data, ensure_ascii=False, indent = "\t")

        #mqtt published
        print(dev_id, pub_data)
        client2.publish("home/device/data/",pub_data)

        time.sleep(5)

except Exception as ex:
    print('Error raised ', ex)
