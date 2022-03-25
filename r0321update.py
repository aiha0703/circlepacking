#############################################
#update
##############################################
for rectangle in rectangles:
    rectangle.update(rectangles)


##############################################
#draw
##############################################
guids_rectangles = []
for rectangle in rectangles:
    guids = rectangle.draw()
    guids_rectangles.extend(guids)

