#Data we need to retrieve.
#1. The total number of vates cast 
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won 
#4. The total number of votes each candidate won 
#5. The winner of the election based on popular vote.
#Add dependencies 
import os
import csv
#Assign variable to load a file from a path 
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis","election_analysis.txt")
#Open the election results and read the file.
with  open(file_to_load) as election_data:
#To Do Read and Analyze the file  
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read and Print the header row 
    headers = next(file_reader) 
    print(headers)
    
#close the file 
