from device_locator import *
from routes import Route
from data_processing import *
from nref_floor2_graph import NREFFloor2Graph

''' TO BUILD HEAT MAP
STEP 1: Obtain devices detected by a sensor from the database at a certain time frame
'''

# for sensor in all_sensors.keys():
    # TODO: SQL command: for each 'sensor' in database, GET detected devices and STORE it in sensor_data dictionary
    # For each device, append device name and RSSIs to devices array
sensor_data = {'A5:3E:6R:G0':[-50, -48, -46, -47, -43, -44, -44, -42, -40, -42],
                'D5:6T:Y7:U8':[-50, -48, -46, -47, -43, -44, -44, -42, -40, -42]}
    # APPEND HERE
    # Below is an example
    # for key, value in sensor_data.items():
    #     all_sensors[sensor].add_device(key, value)
for key, value in sensor_data.items():
    all_sensors['sensor0'].add_device(key, value)

sensor_data = {'A5:3E:6R:G0':[-30, -28, -36, -40, -31, -32, -36, -30, -32, -28],
                'D5:6T:Y7:U8':[-30, -28, -36, -40, -31, -32, -36, -30, -32, -28]}

for key, value in sensor_data.items():
    all_sensors['sensor1'].add_device(key, value)

sensor_data = {'A5:3E:6R:G0':[-60, -48, -61, -62, -64, -67, -60, -61, -62, -63],
                'D5:6T:Y7:U8':[-60, -48, -61, -62, -64, -67, -60, -61, -62, -63]}

for key, value in sensor_data.items():
    all_sensors['sensor2'].add_device(key, value)


'''
STEP 2: Process data per sensor group
# DataProcessing class gather RSSI data, convert them to distances, pinpoint the exact vertex where the device is located, 
    and increase the heat of vertices
# Since we are only working with three sensors, we will only process one sensor group
# TODO: There should be a for loop to process data for all sensor groups in sensor_groups dictionary
'''
data_processing = DataProcessing(['sensor0','sensor1','sensor2'], sensor_groups[tuple(['sensor0','sensor1','sensor2'])])



'''
STEP 3: Send the graph instance NREFFloor2Graph to the front end to obtain the heat of the vertices

TODO: Send graph to FastAPI endpoint for the web app front end
'''
print(f"HEAT: {NREFFloor2Graph.vertices['2-118'].heat_level}")



    
''' PROCESS ROUTE REQUEST'''

''' STEP 1: Get start and destination request from the front end'''
start = '2-118'
destination = '2-090'

''' STEP 2: instantiate Route class '''
route = Route()


''' STEP 3: Calculate route '''
print(route.bfs_route(start, destination))

''' STEP 4: Send to front end '''