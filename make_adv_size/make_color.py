def make_color(size_ratio,name,size_epsilon):
	if size_ratio[name] < 1.0: #small
		red = 0.5 + ((1-size_ratio[name])/size_epsilon)*0.5
		other1 = 0.5 - ((1-size_ratio[name])/size_epsilon)*0.5
		geom.set("rgba",str(red)+str(" ")+str(other1)+str(" ")+str(other1)+str(" 1")) 
	else: # big
		blue = 0.5 + ((size_ratio[name]-1)/size_epsilon)*0.5
		other2  = 0.5 - ((size_ratio[name]-1)/size_epsilon)*0.5
		geom.set("rgba",str(other2)+str(" ")+str(other2)+str(" ")+str(blue)+str(" 1"))
