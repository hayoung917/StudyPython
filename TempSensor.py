import Adafruit_DHT as dht
import datetime
import time
import urllib.request
import pymysql

sensor = dht.DHT11
pin = 4
print('Reading Temperature&Humidity')

#DB저장
conn = pymysql.connect(host = '210.119.12.52', user = 'test_usr', password = 'mysql_p@ssw0rd', db = 'shopdb', charset = 'utf8')

try:
    while True:
        wtime = datetime.datetime.now()
        h, t = dht.read_retry(sensor, pin)

        if h is not None and t is not None:
            print(wtime, "Temp = {0:0.1f}C Humidity = {1:0.1f}%".format(t, h))
            curs = conn.cursor()
            query = """INSERT INTO shopdb.iotmachine (currents_time, machine_id, temperature, humidity)""" \
                    """VALUE (%s, %s, %s, %s)"""
            date = (wtime.strftime("%Y-%m-%d %H:%M:%S"),'LHY',t,h)
            curs.execute(query, date)
            conn.commit()

            time.sleep(10)

        else:
            print("Failed to get readming. Try again!")

finally:
    curs.close()
    conn.close()