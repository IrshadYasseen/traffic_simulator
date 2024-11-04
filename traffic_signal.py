import numpy as np
from detection import points

def update(img1, img2, img3, img4, red, yellow, green):
    signal_points = [points(img1), points(img2), points(img3), points(img4)]
    
    mean_points = np.mean(signal_points)
    std_points = np.std(signal_points)
    
    traffic_levels = []
    for point in signal_points:
        deviation_from_mean = point - mean_points
        if deviation_from_mean > std_points:
            traffic_levels.append(3)  
        elif deviation_from_mean > 0:
            traffic_levels.append(2)  
        elif deviation_from_mean < -std_points:
            traffic_levels.append(0)  
        else:
            traffic_levels.append(1)  
    
    for i in range(4):
        if traffic_levels[i] == 3:
            green[i] = min(green[i] + 10, 60) 
        elif traffic_levels[i] == 2:
            green[i] = min(green[i] + 5, 60)  
        elif traffic_levels[i] == 0:
            green[i] = max(green[i] - 5, 10)  
    red = []
    for i in range(len(green)):
        green_sum = sum(green) - green[i]
        yellow_sum = sum(yellow) - yellow[i]
        red_value = green_sum + yellow_sum
        red.append(red_value)

    return red, yellow, green
