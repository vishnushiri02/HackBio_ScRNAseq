"""
Write a simple Python script for printing the names, slack username, country, 
1 hobby, affiliations of people on your team and the DNA sequence of the genes 
they love most.
"""
import pandas as pd
team_info=pd.read_csv("Team_details.csv")                  #Reading the input data
print(f"Dimensionality of my data{ team_info.shape}")      #Printing the dimensions


for rows in range(team_info.shape[0]):                     #looping through the dataframe
    print(f"My team member {team_info.at[rows,'Name']} who has the slack User name {team_info.at[rows,'Slack UserName']} \n \
    is from {team_info.at[rows,'Country']},\n \
    has {team_info.at[rows,'Hobby']} as hobby, \n \
        has {team_info.at[rows,'Affiliations']} as affiliation \n\
             and loves the gene sequence {team_info.at[rows,'DNA seq of the gene you love']}")
    print ("************************************************")