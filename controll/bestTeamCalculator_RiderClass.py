QtdAllRounders = 2
QtdClimbers = 2
QtdSprinters = 1
QtdUnclassed = 3
AllRounder = "All Rounder"
Climber = "Climber"
Sprinter = "Sprinter"
Unclassed = "Unclassed"

def cannotAddClassInTeam(class_, listBestTeam, isWildCard):
    if (isWildCard):
        return False
    if (class_ == AllRounder):
        return len(list(filter(getOnlyAllRonders, listBestTeam))) >= QtdAllRounders
    elif (class_ == Climber):
        return len(list(filter(getOnlyClimbers, listBestTeam))) >= QtdClimbers
    elif (class_ == Sprinter):
        return len(list(filter(getOnlyClimbers, listBestTeam))) >= QtdSprinters
    elif (class_ == Unclassed):
        return len(list(filter(getOnlyUnclassed, listBestTeam))) >= QtdUnclassed

def removeRidersToFitCategorys(listBestTeam):
    listAux = []
    listBestTeamUssingClasses = []

    listAux = list(filter(getOnlyAllRonders, listBestTeam))
    if (len(listAux) > QtdAllRounders):
        for i in range(QtdAllRounders):
            listBestTeamUssingClasses.append(listAux[i])
    else:
        listBestTeamUssingClasses.extend(listAux)            

    listAux = list(filter(getOnlyClimbers, listBestTeam))
    if (len(listAux) > QtdClimbers):
        for i in range(QtdClimbers):
            listBestTeamUssingClasses.append(listAux[i])
    else:
        listBestTeamUssingClasses.extend(listAux)            

    listAux = list(filter(getOnlySpriters, listBestTeam))
    if (len(listAux) > QtdSprinters):
        for i in range(QtdSprinters):
            listBestTeamUssingClasses.append(listAux[i])
    else:
        listBestTeamUssingClasses.extend(listAux)            

    listAux = list(filter(getOnlyUnclassed, listBestTeam))
    if (len(listAux) > QtdUnclassed):
        for i in range(QtdUnclassed):
            listBestTeamUssingClasses.append(listAux[i])     
    else:
        listBestTeamUssingClasses.extend(listAux)            

    return listBestTeamUssingClasses

def getOnlyAllRonders(rider):
    return rider.class_ == AllRounder

def getOnlyClimbers(rider):
    return rider.class_ == Climber

def getOnlySpriters(rider):
    return rider.class_ == Sprinter

def getOnlyUnclassed(rider):
    return rider.class_ == Unclassed        

gameUsesRidersClass = listAllRiders[0].class_ != ""

# if (gameUsesRidersClass):
#     listBestTeam = removeRidersToFitCategorys(listBestTeam)