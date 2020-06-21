# A dictionary-of-lists database that holds data unique to raw time points
class DataStorage():
    #Initial variables
    rawtime     = 0
    time        = 0
    oxy_a_perc  = 0
    thc_a       = 0
    hbo_a       = 0
    hb_a        = 0
    oxy_b_perc  = 0
    thc_b       = 0
    hbo_b       = 0
    hb_b        = 0
    marker      = 0
    # The entire NIRS database (ordered based on timepoints)
    nirs_database = {}
    # Individual (time) point database
    timepoint_nirs_database = []
    # Initialize the time point database
    def __init__(self):
        self.timepoint_nirs_database = [ self.rawtime,
                                         self.time,
                                         self.oxy_a_perc,
                                         self.thc_a,
                                         self.hbo_a,
                                         self.hb_a ,
                                         self.oxy_b_perc,
                                         self.thc_b,
                                         self.hbo_b,
                                         self.hb_b,
                                         self.marker ]
    # Store data
    def storeData(self, rawtime_key, data_content):
        print("Storing data...")

        # Copy over data associated (found) at raw NIRS timepoint
        for iterations in range(0,len(data_content)-1):
            self.timepoint_nirs_database[iterations] = data_content[iterations]

        # Add the associated data to the rawtime key into the nirs database
        self.nirs_database[rawtime_key] = self.timepoint_nirs_database

    # Get data using binary search
    def readData(self, rawtime_key):
        print("Reading data..")
        return self.nirs_database[rawtime_key]

# Send an object, list, or file with the NIRS data
def database(nirs_rawtime_row, nirs_datacontent_row, option):
    db = DataStorage()
    # Store data
    if option == "store":
        db.storeData(nirs_rawtime_row, nirs_datacontent_row)
    # Get data
    elif option == "read":
        return db.readData(nirs_rawtime_row)