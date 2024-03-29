import sys

from roboflow import Roboflow

RoboFlowAPI = sys.argv[1]
rf = Roboflow(api_key=RoboFlowAPI)
project = rf.workspace("sign-recognintion").project("sign-recoginition")
dataset = project.version(1).download("yolov8-obb")
