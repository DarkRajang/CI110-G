from Conversions import footToMeter
from Conversions import meterToFoot

#Main function
def heading():
    #Heading
    print(format('Feet', "<10s") + format('Meters',"<10s") + format('|', "<5s") + format('Meters',"<12") + "Feet")
    print()
    
def table():
    #Defining Meters
    m = float(20)
    
    #Making the Conversion table
    for i in range(1,11,1):
        
        #Displaying the table
        print(format(float(i), "<10.1f") + format(footToMeter(i),"<10.3f") + format('|', "<5s") 
              + format(m,"<12.1f") + format(meterToFoot(m),".3f") )
        #Increasing Meters value
        m += 6

def ConTa():
    heading()
    table()
    
ConTa()