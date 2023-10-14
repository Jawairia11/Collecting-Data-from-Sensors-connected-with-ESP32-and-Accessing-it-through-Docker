# Collecting-Data-from-Sensors-connected-with-ESP32-and-Accessing-it-through-Docker
The objective is to setup IOT system using ESP32  for collecting temperature , humidity and distance data from sensors and push it to Grafana Dashboard through MQTT and employ Docker for managing containers. 
The data transmission occurs to a server using a local hotspot for connectivity.

We have one microcontroller and 3 sensors
1.	Temperature  
2.	Humidity 
3.	Sonar

Requirements:
•	ESP32 microcontroller
•	Temperature and humidity sensor (e.g., DHT22)
•	Ultrasonic sensor (e.g., HC-SR04)
•	MQTT broker (e.g., Mosquitto)
•	Grafana installation
•	Docker installed on the Linux server
•	Linux operating system
•	Local hotspot for data transmission
