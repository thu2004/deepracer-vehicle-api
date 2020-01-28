# Deepracer Vehicle API

deepracer-vehicle-api

# API

## High level methods
* show_vehicle_info
* move_forward
* move_backward
* turn_right
* turn_left

## General purpose methods
* get_is_usb_connected
* get_battery_level
* get_raw_video_stream

## Methods for running autonomous mode
* set_autonomous_mode
* set_throttle_percent

## methods for running manual mode
* set_manual_mode
* start_car
* stop_car
* move

## methods for models
* get_models
* get_uploaded_models
* load_model
* upload_model

## methods for calibration
* set_calibration_mode
* get_calibration_angle
* get_calibration_throttle
* set_calibration_throttle
* set_calibration_angle

# Installation
```
pip install deepracer-vehicle-api
```
# Getting Started

## Show vehicle info

```python
import deepracer_vehicle_api as dva

client = dva.Client(password="???", ip="111.222.333.444")
client.show_vehicle_info()
```

For more details, see addition examples here: https://github.com/thu2004/deepracer-vehicle-api/examples'

# Others

This repo has borrowed code and refactored them from :
* https://github.com/ARCC-RACE/deepracer-rc
* https://github.com/gidutz/DeepBullFighting



