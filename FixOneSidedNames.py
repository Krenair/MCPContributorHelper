import ContributorTools
def checkNames (clientinfo, serverinfo):
    if not ContributorTools.isSeargeName(clientinfo['name']) and ContributorTools.isSeargeName(serverinfo['name']):
        safeOutput('0', serverinfo['name'], 'pc' + serverinfo['searge'][1].replace('u', 'm').replace('i', 'f') + ' ' + clientinfo['searge'] + ' ' + serverinfo['searge'])
    elif ContributorTools.isSeargeName(clientinfo['name']) and not ContributorTools.isSeargeName(serverinfo['name']):
        print clientinfo['name'], serverinfo['name']
        safeOutput('1', clientinfo['name'], 'ps' + clientinfo['searge'][1].replace('u', 'm').replace('i', 'f') + ' ' + serverinfo['searge'] + ' ' + clientinfo['searge'])

def safeOutput(side, name, out):
    for member in ContributorTools.members[side].values():
        if member['name'] == name:
             print 'POSSIBLY BROKEN:', out

    print out

ContributorTools.forEachMember(checkNames)
