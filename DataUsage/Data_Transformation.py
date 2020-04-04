# This file averages patient-specific files or group-specific files and temporarily stores them into Data_Storage
import DataUsage.Data_Storage as db

def toDatabase():
    db.database()

# Gets content from each determined file to be average (along with other statistics
def dataTransformation():
    print("")
    toDatabase()