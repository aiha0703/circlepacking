#############################################
#update
##############################################
for circle in circles:
    circle.update(circles)


##############################################
#draw
##############################################
guids_circles = []
for circle in circles:
    guids = circle.draw()
    guids_circles.extend(guids)

