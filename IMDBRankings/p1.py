#Joseph Mucciaccio
#This program takes data from files and outputs them in a specific order
#Displaying the top collaborations shows which actor and director made the most movies together and how many
#Displaying the top directors add up the total gross of a directors movies and puts the top 7 

import pandas as pd #using this library because it makes it easier to select rows and columns by index and number (loc and iloc)

top_casts = pd.read_csv("imdb-top-casts.csv", header = None)
top_grossing = pd.read_csv("imdb-top-grossing.csv")
top_rated = pd.read_csv("imdb-top-rated.csv")
top_casts.columns = ["Title", "Year", "Director", "Actor1", "Actor2" ,"Actor3" ,"Actor4" ,"Actor5"]


def display_top_collaborations():
    Map = dict()
    
    for index, row in top_rated.iterrows():
        movieTitle = row["Title"]
        temp = top_casts.loc[top_casts["Title"] == movieTitle]
        if ((temp.iloc[0]["Director"],temp.iloc[0]['Actor1']) in Map):
            Map[(temp.iloc[0]["Director"],temp.iloc[0]["Actor1"])] = Map[(temp.iloc[0]['Director'],temp.iloc[0]['Actor1'])] + 1
        else:
            Map[(temp.iloc[0]["Director"],temp.iloc[0]["Actor1"])] = 1
    
    outputList = []   
    
    for key,val in Map.items():
        a,b = key
        outputList.append((a,b,val))
    outputList = sorted(outputList,key= lambda x: x[2],reverse=True)
    print("Top Collaborations:")
    for x in range(7):
        print(outputList[x])
    
    return outputList

def display_top_directors():
    Map = dict()
    for index, row in top_grossing.iterrows():
        movieTitle = row["Title"]
        totalAmount = row["USA Box Office"]
        temp = top_casts.loc[top_casts["Title"] == movieTitle]
        if (temp.iloc[0]["Director"] in Map):
            Map[temp.iloc[0]["Director"]] = Map[temp.iloc[0]["Director"]] + totalAmount
        else:
            Map[temp.iloc[0]["Director"]] = totalAmount
    outputList = []   
    for key,val in Map.items():
        outputList.append((key,val))
    outputList = sorted(outputList,key= lambda x: x[1],reverse=True)
    print("\nTop Directors:")
    for x in range(7):
        print(outputList[x])
  
    return outputList


def main():
    display_top_collaborations()
    display_top_directors()
  
main()
