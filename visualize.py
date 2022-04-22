#!/usr/bin/python
from flask import Flask, render_template
import Adafruit_DHT as dht
app = Flask(__name__)

h,t = dht.read_retry(dht.DHT22, 4)
print("Temp : {0:0.1f}*C Humidity : {1:0.1f}%".format(t,h))
@app.route("/")
def main():
   templateData = {
      'temperature' : t,
      'humidity': h
   }
   return render_template('main.html', **templateData)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
