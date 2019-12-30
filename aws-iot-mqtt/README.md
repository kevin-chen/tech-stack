http://mqtt.kev-chen.me/

Steps to setup Paho MQTT on AWS IoT:

* Setup IoT
  * AWS CLI : https://www.hackster.io/mariocannistra/python-and-paho-for-mqtt-with-aws-iot-921e41
  * Create a new Thing using web interface

* Create a new certificate and apply it to Thing
  * Download certificate, public and private key
  * Download pem file https://www.amazontrust.com/repository/AmazonRootCA1.pem

* Use Python code and replace 
  * Install paho-mqtt
  * Code: https://github.com/mariocannistra/python-paho-mqtt-for-aws-iot/blob/master/awsiotpub.py
  * Host Data
    * CLI: aws iot describe-endpoint --endpoint-type iot:Data-ATS
    * AWS -> Thing -> Interact -> HTTPS
  * Credentials
    * awshost = "a26q0nqbn8czyn-ats.iot.us-east-1.amazonaws.com"
    * awsport = 8883
    * clientId = "myThingName"
    * thingName = "myThingName"
    * caPath = "AmazonRootCA1.pem"
    * certPath = "3bbc724062-certificate.pem.crt" #certificate
    * keyPath = "3bbc724062-private.pem.key" # private key

Tips:
* subscribes to all
* MQTT Broker: https://console.aws.amazon.com/iot/home?region=us-east-1#/test?topic=$aws~2Fthings~2FmyThingName~2Fshadow~2Fupdate~2Faccepted

Material:

Tutorial: https://www.hackster.io/mariocannistra/python-and-paho-for-mqtt-with-aws-iot-921e41

Code: https://github.com/mariocannistra/python-paho-mqtt-for-aws-iot/blob/master/awsiotpub.py

caPath: https://www.amazontrust.com/repository/AmazonRootCA1.pem
