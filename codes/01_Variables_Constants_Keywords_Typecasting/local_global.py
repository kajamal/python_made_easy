# Global vs. local variables in functions

# Declare a variable and initialize it
temp_threshold = 30 # Global variable
def monitor_temperature():
	# Local Variable
    temp_threshold = 44
    print("Threshold set inside the function", temp_threshold)

monitor_temperature()
print("Threshold set globally", temp_threshold)


# Declare a variable and initialize it
temp_threshold = 30 # Global variable
def monitor_temperature():
	global temp_threshold
	temp_threshold = 44
	print("Threshold set inside the function", temp_threshold)

monitor_temperature()
print("Threshold set globally", temp_threshold)

