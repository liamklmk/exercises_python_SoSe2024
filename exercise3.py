def steigung_function(liste):
    x1 = liste[0]
    y1 = liste[1]
    x2 = liste[2]
    y2 = liste[3]
    
    delta_x = x2 -x1
    delta_y = y2 - y1
    
    if delta_x == 0:
        print("die steigerung ist nicht definiert")
    else:
        steigung = delta_y / delta_x
        print(steigung)

steigung_function([4, 4, 8, 4])