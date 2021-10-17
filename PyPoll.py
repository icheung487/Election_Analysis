
import datetime
from typing import ClassVar
now = datetime.datetime.now()
print("the time right now is", now)

#Direct Parth to the file 
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file: 
election_data = open(file_to_load, 'r')
#close the file 
election_data.close()
# Open the election results and read the file using "with"
with open(file_to_load) as election_data:
    print(election_data)
import os
dir(os)

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #READ AND PRINT THE HEADER ROW
    headers = next(file_reader)
    print(headers)

        

