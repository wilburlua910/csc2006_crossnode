import json
from data import data

# Global variables
currentIteration = 0
emptyCount = 0
currentSection = 0

straightGreenLight = [False, False, False, False]
# rightGreenLight: [False, False, False, False]


# If it's at 60 seconds, next section will turn green
if currentIteration == 6:
    if currentSection == 1:
        currentSection = 0
    else:
        currentSection += 1
    straightGreenLight[currentSection] = True
    straightGreenLight[currentSection + 2] = True
    #return straightGreenLight

traffic = [
    {
        "section": 0,
        "straight": 0,
        "right": 0
    },
    {
        "section": 1,
        "straight": 0,
        "right": 0
    },
    {
        "section": 2,
        "straight": 0,
        "right": 0
    },
    {
        "section": 3,
        "straight": 0,
        "right": 0
    }
]

for iSec, sec in enumerate(data):
    lanes = sec["lanes"]
    for lane in lanes:
        if lane["lane"] == 1:
            traffic[iSec]["right"] += lane["cars"]
        else:
            traffic[iSec]["straight"] += lane["cars"]

# parsed = json
print(json.dumps(traffic, indent=4, sort_keys=True))
print(max(traffic["straight"] for traffic in traffic))

if emptyCount == 3:
    if currentSection == 3:
        currentSection = 0
    else:
        currentSection += 1
    straightGreenLight[currentSection] = True
    # return straightGreenLight[currentSection]
    # section = next((x for x in traffic if x["section"] == currentSection), None)


allStraightEqual = all(obj["straight"] == traffic[0]["straight"] for obj in traffic)
if allStraightEqual != True:
    maxStraightVal = max(traffic["straight"] for traffic in traffic)
    highestObj = next((x for x in traffic if x["straight"] == maxStraightVal), None)
    print(highestObj)

allRightEqual = all(obj["right"] == traffic[0]["right"] for obj in traffic)
if allRightEqual != True:
    maxRightVal = max(traffic["right"] for traffic in traffic)
    highestObj = next((x for x in traffic if x["right"] == maxRightVal), None)
    print(highestObj)