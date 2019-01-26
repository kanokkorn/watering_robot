# Watering Bot(aka. SMART ROBOT v1)

Main objective:

* Watering by following GPS marker
* Palm tree analysis for find disease 
* Loadcell
* Measure soil & humidity

## Watering

The robot can navigate autonomously point-by-point by GPS receiver and data from the onboard computer.
The GPS point also can be edit in GUI and send to the robot via MQTT protocol

## Palm tree analysis

 Capture pictures of oil palm leaf and detect Oil palm fruits using computer vision and deep learning and collect data for further analysis \
 Example 1:
 > <img src="images/tf_palm.jpg" width="600">
 Example 2:
 > <img src="images/tf_palm_2.jpg" width="600">

## Loadcell

loadcell built-in with watering-robot

## Measure soil & humidity

Measure soil & humidity send it to Firebase to collect and analyze data
