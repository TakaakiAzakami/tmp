import xml.etree.ElementTree as ET 
import time
import random
import make_color

tree = ET.parse('/home/takaaki/.local/lib/python3.8/site-packages/gym/envs/mujoco/assets/ant_adv.xml')

root = tree.getroot()

size_ratio = {}

size_list = {"torso_geom":0.25,"aux_1_geom":0.08,"aux_2_geom":0.08,"aux_3_geom":0.08,"aux_4_geom":0.08
			,"front_left_leg_geom":0.08,"front_right_leg_geom":0.08,"back_left_leg_geom":0.08,"back_right_leg_geom":0.08
			,"front_left_ankle_geom":0.08,"front_right_ankle_geom":0.08,"back_left_ankle_geom":0.08,"back_right_ankle_geom":0.08}

size_epsilon = 0.05

def set_size(epsilon):
	random.seed(time.time())
	r = random.random()	
	ratio = 1.0 - epsilon + r*(epsilon*2)
	ratio = 1.0
	return ratio

for geom in root.iter("geom"):
	for name in size_list:
		if name in str(geom.attrib):
			if name in size_list.keys():	
				size_ratio[name] = set_size(size_epsilon)
				geom.set("size",str(size_ratio[name]*size_list[name]))

				if size_ratio[name] < 1.0:
					red = 0.5 + ((1-size_ratio[name])/size_epsilon)*0.5
					other1 = 0.5 - ((1-size_ratio[name])/size_epsilon)*0.5
					geom.set("rgba",str(red)+str(" ")+str(other1)+str(" ")+str(other1)+str(" 1")) 
				else: # big
					blue = 0.5 + ((size_ratio[name]-1)/size_epsilon)*0.5
					other2  = 0.5 - ((size_ratio[name]-1)/size_epsilon)*0.5
					geom.set("rgba",str(other2)+str(" ")+str(other2)+str(" ")+str(blue)+str(" 1"))

tree.write('/home/takaaki/.local/lib/python3.8/site-packages/gym/envs/mujoco/assets/ant_adv.xml',encoding='UTF-8')
