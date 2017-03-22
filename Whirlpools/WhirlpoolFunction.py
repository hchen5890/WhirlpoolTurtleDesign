def Whirlpool (t, size, times, width):
    #Repeats the following code "times" which is defined when using the command
    for times in range(times):
        #Sets the width (how wide the turtle draws)
        t.width(width)
        #Draws a circle that is "size" divided by 2 (To limit the size)
        t.circle(size/2)
        #Makes the turtle go forward "Size" but doubled
        t.forward(size*2)
        #Makes the turtle turn right 180 (Same as left 180)
        t.right(180)
        #Draws another circle that is also "size" divided by 2
        t.circle(size/2)
