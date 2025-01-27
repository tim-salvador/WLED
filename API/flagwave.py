import requests
import json
import time

def rgb_to_hex(rgb):
    return str('%02x%02x%02x' % rgb).upper()

def Animate():
    wled_device_ip = "192.168.86.57"
    api_endpoint = f"http://{wled_device_ip}/json/state"
    
    json_data = {"on":True,"bri":255,"transition":7,"mainseg":0,"seg":[{"id":0,"start":0,"stop":157,"grp":1,"spc":0,"of":0,"on":True,"frz":False,"bri":255,"cct":127,"col":[[128,128,128],[0,0,0],[255,0,0]],"fx":0,"sx":0,"ix":105,"pal":2,"sel":True,"rev":False,"mi":False},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0}]}
    
    headers ={'content-type':'application/json'}
    r = requests.post(api_endpoint, data=json.dumps(json_data),headers=headers)

    colors = { 'RED':[],
    'WHITE':[],
    'BLUE':[]}
    
    stripColors = ['RED','RED','RED','RED','RED','WHITE','WHITE','WHITE','WHITE','WHITE',
                'RED','RED','RED','RED','RED','WHITE','WHITE','WHITE','WHITE','WHITE',
                'RED','RED','RED','RED','RED','WHITE','WHITE','WHITE','WHITE','WHITE',
                'RED','RED','RED','RED','RED','WHITE','WHITE','WHITE','WHITE','WHITE',
                'RED','RED','RED','RED','RED','WHITE','WHITE','WHITE','WHITE','WHITE',
                'RED','RED','RED','RED','RED','WHITE','WHITE','WHITE','WHITE','WHITE',
                'RED','RED','RED','RED','RED',
                'BLUE','BLUE','BLUE','WHITE','BLUE','BLUE','BLUE','WHITE',
                'BLUE','BLUE','BLUE','WHITE','BLUE','BLUE','BLUE','WHITE',
                'BLUE','BLUE','BLUE','WHITE','BLUE','BLUE','BLUE','WHITE',
                'BLUE','BLUE','BLUE','WHITE','BLUE','BLUE','BLUE','WHITE','BLUE','BLUE','BLUE',
                'RED','RED','RED','WHITE','WHITE','WHITE',
                'RED','RED','RED','WHITE','WHITE','WHITE',
                'RED','RED','RED','WHITE','WHITE','WHITE',
                'RED','RED','RED','WHITE','WHITE','WHITE',
                'RED','RED','RED','WHITE','WHITE','WHITE',
                'RED','RED','RED','WHITE','WHITE','WHITE',
                'RED','RED','RED',
                'BLUE','BLUE','BLUE','WHITE',
                'BLUE','BLUE','BLUE','WHITE',
                'BLUE','BLUE','BLUE','WHITE',
                'BLUE','BLUE','BLUE','WHITE',
                'BLUE','BLUE'
                ]

    animMS = 0.05
    numLEDS = len(stripColors)
    levels = 11
    brightFactor = 256//(levels+2)
    brights = []
    for i in reversed(range(levels)):
        b = 255 - (i*brightFactor)
        brights.append(b)
    
    for i in brights:
        colors['RED'].append(rgb_to_hex((i, 0, 0)))
        colors['WHITE'].append(rgb_to_hex((i, i, i)))
        colors['BLUE'].append(rgb_to_hex((0, 0, i)))
    
    
    stripBrightness = []
    for i in range(levels):
        stripBrightness.append(i)
    for i in reversed(range(1, levels - 1)):
        stripBrightness.append(i)
            
    numBright = len(stripBrightness)
    strip=[""] * numLEDS
    counter = 0
    while True:
        for i in range(numLEDS):
            colorInd = stripBrightness[(i + counter) % numBright]
            strip[i]=colors[stripColors[i]][colorInd]
        json_data = {"seg":{"i":strip}}
        r = requests.post(api_endpoint,data=json.dumps(json_data),headers=headers)
        time.sleep(animMS)
        counter = (counter + 1) % numBright
    
def main():
    Animate()
    
if __name__ == "__main__":
    main()
