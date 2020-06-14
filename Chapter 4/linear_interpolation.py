import numpy as np

def interpolate(yi, Δt, t):
	#Measurement finds the time t such that, t[i] < t < t[i+1]
	measurement = Δt
	i = 0
	while measurement < t:
		measurement = measurement + Δt
		i += 1
	#It returns the formula of the linear interpolation in the time t
	return ((yi[i]-yi[i-1])/Δt)*(t - (measurement - Δt)) + yi[i-1]

def find_y(yi, Δt, t):
	print(interpolate(yi, Δt, t))
	h = float(input('Type the time: '))
	if h > 0:
		find_y(yi, Δt, h)
	return 0


Δt = 1
measurements = [4.4, 2.0, 11.0, 21.5, 7.5]
h = float(input('Type the first interpolation time: '))
print("If you don't need other interpolations you may type a negative number or ctrl + c")

find_y(measurements,Δt, h)
