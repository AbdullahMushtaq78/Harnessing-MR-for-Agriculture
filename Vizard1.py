#libraries
import vizfx
import oculus
import vizconnect
import vizshape
import vizmat
import math
hmd = oculus.Rift()
import vizinfo
import cv2 
import numpy as np
#Video Connection
url = 'https://172.20.10.2:8080/video'
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
    
        

#Sphere(Drone dummy) head-movement
def GetMatrix(e):
	move_speed = 0.03
	#Sphere movement
	euler = vizconnect.getTracker("head_tracker").getEuler()
	sphere.setEuler(euler)
	sphere.translate(hmd.getRightTouchController().getStick()[0] * move_speed, 0, hmd.getRightTouchController().getStick()[1] * move_speed, viz.REL_LOCAL)
	
	
	# Displaying the Video (frame by frame) as a Texture of the screen box
	ret, frame = cap.read()
	frame = cv2.resize(frame, (int(frame.shape[0]*1.5),int(frame.shape[1]*1.5)), interpolation=cv2.INTER_LINEAR)
	cv2.imwrite("./Assets/Camera/frame.png", frame)
	frame_t = viz.addTexture("./Assets/Camera/frame.png")
	screen.texture(frame_t)
	
#Loading and adding the scene in the environment
vizfx.addChild("scene1.osgb")

#Creating a Box for Screen
screen = vizshape.addBox(size= [6,4,0.01])
s_pos = screen.getPosition()
screen.setPosition([s_pos[0], 2, 3])

#Creating a Sphere (Drone Dummy)
sphere = vizshape.addSphere(radius=0.3, color=viz.RED)
sphere.setPosition([0.5,2,0])
dot = viz.addTexture("./Assets/Texture_images/drone.png")
sphere.texture(dot)


#Loading the configuration and starting the Vizard Environment
vizconnect.go("viz_connect_config.py")
#Hooking the GetMatrix function with Update Event
viz.callback(viz.UPDATE_EVENT, GetMatrix)


#Y Button Event for increasing the height of the Drone
def MoverY(e):
	move_speed =0.03
	sphere.translate(hmd.getLeftTouchController().getStick()[0] * move_speed, move_speed, hmd.getLeftTouchController().getStick()[1] * move_speed, viz.REL_LOCAL)
	
#X  Button Event for decreasing the height of the Drone
def MoverX(e):
	move_speed = 0.03
	sphere.translate(hmd.getLeftTouchController().getStick()[0] * move_speed, -move_speed, hmd.getLeftTouchController().getStick()[1] * move_speed, viz.REL_LOCAL)

#Adding callback to keep checking the press of buttons
viz.callback(viz.getEventID('ButtonY'), MoverY)
viz.callback(viz.getEventID('ButtonX'), MoverX)


