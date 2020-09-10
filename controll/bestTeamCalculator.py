from itertools import cycle

#TODO: I really need to import like this? Fells like a workaround
import sys
sys.path.insert(1, "./model")
import webSrapper

# Constants
QtdRidersInTeam = 9
MaxTeamCost = 100
MinRiderCost = 4

def sortByPoints(rider):
    return rider.points  

#TODO: Is there a better way do to this? Something like Java strem()?    
def removeLowestRatioRider(listBestTeam):
    lowestRatio = listBestTeam[0].ratio
    indexLowestRatio = 0
    for i in range(len(listBestTeam)):
        if (listBestTeam[i].ratio < lowestRatio):
            lowestRatio = listBestTeam[i].ratio
            indexLowestRatio = i
    
    listBestTeam.pop(indexLowestRatio)    

def getTeamCost(team):
    teamCost = 0
    for i in range(len(team)):
        teamCost += team[i].cost

    return teamCost

# Rider cannot be in the best team 
# The rider cost can add more than 100 to the team
# Need do consider the qtd of riders stil to fill
def canAddRiderInTeam(rider, listBestTeam):
    if (not rider in listBestTeam):
        teamCost = getTeamCost(listBestTeam)
        ridersToFillCost = (QtdRidersInTeam - len(listBestTeam) - 1) * MinRiderCost

        if ((teamCost + ridersToFillCost + rider.cost) <= MaxTeamCost):
            return True
        else:
            return False
    else: 
        return False

# Team cost must be lower then 100
# Need to consider the qtd of riders (Ex: Can not have 96 total cost and only 7 riders)
def isNecessaryToRemoverAnRider(listBestTeam):
    teamCost = getTeamCost(listBestTeam) 

    if (teamCost > MaxTeamCost):       
        return True
    else:
        # Each rider cost minumum 4 points
        pointsToFill = (QtdRidersInTeam - len(listBestTeam)) * MinRiderCost
        if (teamCost + pointsToFill <= MaxTeamCost):
            return False
        else:
            return True         

listBestTeam = []
listAllRiders = []

# Get de riders list and do the sorting by points
listAllRiders = webSrapper.getListOfRiders()
listAllRiders.sort(reverse=True, key=sortByPoints)

# Get the 9 best point riders
for i in range(QtdRidersInTeam):
    listBestTeam.append(listAllRiders[i])

# Remove the riders by ratio until the points fits the 100 maximum 
while (isNecessaryToRemoverAnRider(listBestTeam)):
    removeLowestRatioRider(listBestTeam)

# Use the cycle to get the best next rider
listAllRidersCycle = cycle(listAllRiders)

# Fill the rooster to fit the rider
while (len(listBestTeam) < QtdRidersInTeam): 
    rider = next(listAllRidersCycle)

    if (canAddRiderInTeam(rider, listBestTeam)):
        listBestTeam.append(rider)


print("\nBest team: ")
totalPoints = 0
for i in range(len(listBestTeam)):
    print("Name: ", listBestTeam[i].name, ", Points: ", listBestTeam[i].points, "Cost: ", listBestTeam[i].cost) 
    totalPoints += listBestTeam[i].points

print("Team points: ", totalPoints)    
print("Team cost: ", getTeamCost(listBestTeam))    
print("Unused Credits: ", MaxTeamCost - getTeamCost(listBestTeam))    
