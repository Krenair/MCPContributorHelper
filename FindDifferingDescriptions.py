import ContributorTools, Levenshtein, sys

ContributorTools.haveOutputted = False

def checkDifferentDescriptions (clientinfo, serverinfo):
    try:
        maxDistance = sys.argv[1]
    except:
        maxDistance = 5

    if clientinfo['desc'] != serverinfo['desc'] and Levenshtein.distance(clientinfo['desc'], serverinfo['desc']) <= maxDistance:
        output(clientinfo, serverinfo)
    elif clientinfo['desc'] != serverinfo['desc'] and clientinfo['desc'].lower() == serverinfo['desc'].lower():
        output(clientinfo, serverinfo)

def output(clientinfo, serverinfo):
    if ContributorTools.haveOutputted:
        print '----'

    ContributorTools.haveOutputted = True

    print 'Client name:', clientinfo['name'], '(' + clientinfo['searge'] + ')'
    print 'Client description:', clientinfo['desc']
    print 'Server name:', serverinfo['name'], '(' + serverinfo['searge'] + ')'
    print 'Server description:', serverinfo['desc']

ContributorTools.forEachMember(checkDifferentDescriptions)
