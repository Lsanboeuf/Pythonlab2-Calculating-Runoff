#Laurence SanBoeuf
#Python IDCE302
#Lab #3
#Sep 6, 2019

'''When agricultural land is paved over, rainwater cannot be absorbed as easily,
resulting in runoff of rainwater. In some cases, this runoff can lead to increases
in flooding or landslides. The runoff also presents an opportunity to capture and/or
recycle it. We’re going to write a short script to calculate the amount of rain run
off of a single plot of land (50 feet by 20 feet) in Kenya during a very small rain
storm. You may be as astonished as we were to learn how much it is. Take a guess:
what is the volume of water that runs off a 1,000 square foot plot of paved land
during a 1 inch rain storm? 20 gallons? 50 gallons? 100 gallons? 1000 gallons?

To calculate the runoff from any given rainfall:

Start by writing your script to include variables and values for the length, width,
and area of the plot of land. You may want to put a comment tag to show what this
section of script is for. Take the dimensions of the footprint of the land and convert
them to inches, because the rainwater is measured in inches and we will need to convert
to gallons. Then create descriptive variables with these values and use them to calculate
the area. Note: you only need to calculate to the second decimal place, or hundredths.
Next create include variables and values for the amount of rainfall, which equals:
length times width times the number of inches of rainfall to get the cubic inches of water.
Once you’ve done that, you’ll need to convert the number of cubic inches to gallons. 
Finally, make sure that the script will print out the following text, along with the
values you used. It should look something like this:
o    plot_length is:  ____________ (whatever values you used)
o    plot_width is:  ____________ (whatever values you used)
o    rainfall_inches is:  ____________ (whatever values you used)
o    runoff_gallons is:  ____________ (whatever values you used)'''


plot_length = 50  #Length of plot area in ft
plot_width = 20  #Width of plot area in ft
area = plot_length*plot_width  #Area in ft
areain = (plot_length*12)* (plot_width*12)  #Area in inches
rainfall=1  #Amount of recorded rainfall in inches
rainfall_inches = areain*rainfall  #Volume of rainfall in certain area (inches cubed)
runoff_gallons = rainfall_inches*0.004329 #Volume of rainfall in area (gallons)

print "Plot_length is:", (plot_length), "ft"
print "Plot_width is:", (plot_width), "ft"
print "Rainfall_inches is:",(rainfall_inches), "in^2"
print "Runoff_gallons is:", (runoff_gallons), "gal"





