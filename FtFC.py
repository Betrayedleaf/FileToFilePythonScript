class Process:
    #this initializes the class
    def __init__(self, ID, Company, Contact, Address, City, State, ZipCode, Phone, AltPhone, Key, CompanyKey, Region, CustomerLimit, CustomerType):
        self.CompanyName = Company
        self.FirstName, self.LastName = Contact.split(' ')
        self.StreetAddress = Address
        self.City = City
        self.StateAddress = State
        self.StateZipCode = ZipCode
        self.MainPhone = Phone
        self.AltPhone = AltPhone
        self.AlphaKey = Key[0:10]
        self.BetaKey = Key[11:36]
        self.StateRegion = Region
        self.CompanyCode = CompanyKey
        self.CustomerType = CustomerType
        self.CustomerLimit = CustomerLimit
        self.CustomerID = ID

    #this pads the company name to 20
    def PadCompName(self):
        self.CompanyName = self.CompanyName.rjust(20, " ")

    #pads the last name to 20
    def PadLastName(self):
        self.LastName = self.LastName.rjust(20, " ")
        
    #this pads first name
    def PadFirstName(self):
        self.FirstName = self.FirstName.rjust(15, " ")

    #this pads street address
    def PadStreetAddress(self):
        self.StreetAddress = self.StreetAddress.rjust(30," ")

    #this pads city
    def PadCity(self):
        self.City = self.City.rjust(20, " ")

    #this uses a dictionary of state abberviations to abbreviate the state
    def AbbreviateState(self):
        StateAbbreviations = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
       "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "District of Columbia": "DC",
        "American Samoa": "AS",
        "Guam": "GU",
        "Northern Mariana Islands": "MP",
        "Puerto Rico": "PR",
        "United States Minor Outlying Islands": "UM",
        "U.S. Virgin Islands": "VI",
        }
        if self.StateAddress in StateAbbreviations:
            self.StateAddress = StateAbbreviations[self.StateAddress]
        else:
            self.StateAddress = "xx"

    #changes the zip code to ##### if the length is below 5
    def PadZipCode(self):
        if len(self.StateZipCode) < 5:
            self.StateZipCode = "#####"

    #replaces hyphens in phone number with emptiness
    def PadPhoneNumber(self):
        self.MainPhone = self.MainPhone.replace("-", "")

    #replaces hyphens in phone number with emptiness
    def PadAltPhoneNumber(self):
        self.AltPhone = self.AltPhone.replace("-", "")

    #pads alpha key with 0
    def PadAlphaKey(self):
        self.AlphaKey = self.AlphaKey.ljust(10, "0")

    #pads beta key with x
    def PadBetaKey(self):
        self.BetaKey = self.BetaKey.ljust(28, "x")

    #pads the region with spaces
    def PadRegion(self):
        self.StateRegion = self.StateRegion.ljust(5, " ")

    #reduces the customer limit by 1000
    def CustomerLimitReduction(self):
        self.CustomerLimit = int(self.CustomerLimit) / 1000
        self.CustomerLimit = int(self.CustomerLimit)

    #pads customer ID with an x
    def PadCustomerID(self):
        self.CustomerID = self.CustomerID.rjust(10, "x")

    #this is mostly debugging for developers. allows all properties of current object to be printed
    def PrintAll(self):
        print(self.CompanyName, self.LastName, self.FirstName, self.StreetAddress, self.StateZipCode, self.MainPhone, self.AltPhone, self.AlphaKey, self.BetaKey, self.StateRegion, self.CompanyCode, self.CustomerLimit, self.CustomerType)
    
                                                

    
        
        
      
        
    
    
