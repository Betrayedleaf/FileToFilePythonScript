import csv
from csv import reader
#for some reason i can't just import FtFC, it has to import Process from FtFC
from FtFC import Process

#opening the file
with open(input("Please enter a file path"), "r") as input_file:
    file_reader = reader(input_file)

    #the loop
    for i in file_reader:
        
        obj1 = Process(*i)
        obj1.PadCompName()
        obj1.PadLastName()
        obj1.PadFirstName()
        obj1.PadStreetAddress()
        obj1.PadCity()
        obj1.AbbreviateState()
        obj1.PadPhoneNumber()
        obj1.PadAltPhoneNumber()
        obj1.PadAlphaKey()
        obj1.PadBetaKey()
        obj1.PadRegion()
        obj1.PadCustomerID()
        obj1.PadZipCode()
        obj1.CustomerLimitReduction()
        with open(r"C:/Users/sam74/Desktop/Homework/Programming/OutputFile.csv", 'a') as output:
            writer = csv.writer(output)
            writer.writerow([obj1.CompanyName, obj1.LastName, obj1.FirstName, obj1.StreetAddress, obj1.City, obj1.StateAddress, obj1.StateZipCode, obj1.MainPhone, obj1.AltPhone, obj1.AlphaKey, obj1.BetaKey, obj1.StateRegion, obj1.CompanyCode, obj1.CustomerType, obj1.CustomerLimit, obj1.CustomerID])
            
            output.close()



        
