mcpPath = '/home/alex/MCP/7.2/'
csvPrefix = '' #Leave this blank unless you know what you're doing. This is the prefix to the csv filenames in the conf folder. Used because I have test_methods.csv and test_fields.csv for MCPBot's testcsv command.
sidesFile = 'MCP7.2ClientToServerMappings.csv' #

import csv, re, sys
sidesFileReader = csv.DictReader(open(sidesFile))

seargeNameCheck = re.compile(r"f(unc|ield)_[0-9]+_[a-zA-Z]+(_|)$")

def isSeargeName(name):
    return seargeNameCheck.match(name)

def getAllMembers ():
    members = {'0':{}, '1':{}}

    for line in open(mcpPath + 'conf/client.srg').read().splitlines():
        searge = getSeargenameFromSrgLine(line)
        if searge != None:
            members['0'][searge] = {'searge':searge, 'name':searge, 'desc':''}

    for line in open(mcpPath + 'conf/server.srg').read().splitlines():
        searge = getSeargenameFromSrgLine(line)
        if searge != None:
            members['1'][searge] = {'searge':searge, 'name':searge, 'desc':''}

    for member in csv.DictReader(open(mcpPath + 'conf/' + csvPrefix + 'methods.csv')):
        members[member['side']][member['searge']] = member

    for member in csv.DictReader(open(mcpPath + 'conf/' + csvPrefix + 'fields.csv')):
        members[member['side']][member['searge']] = member

    return members

def getSeargenameFromSrgLine (line):
    parts = line.split(' ')

    if parts[0] == 'FD:':
        qualifiedName = parts[2]
    elif parts[0] == 'MD:':
        qualifiedName = parts[3]
    else:
        return None

    searge = qualifiedName[qualifiedName.rfind('/') + 1:]

    if not isSeargeName(searge):
        return None

    return searge

def forEachMember (f):
    for row in sidesFileReader:
        try:
            clientinfo = members['0'][row['client']]
        except KeyError as keyError:
            print 'Missing client', keyError.message
            continue

        try:
            serverinfo = members['1'][row['server']]
        except KeyError as keyError:
            print 'Missing server', keyError.message
            continue

        f(clientinfo, serverinfo)

def getMemberListFromCsvs ():
    memberList = []

    for member in csv.DictReader(open(mcpPath + 'conf/' + csvPrefix + 'methods.csv')):
        memberList.append(member)

    for member in csv.DictReader(open(mcpPath + 'conf/' + csvPrefix + 'fields.csv')):
        memberList.append(member)

    return memberList

def outputCommands ():
    try:
        return sys.argv[1] == 'commands'
    except IndexError:
        return False

members = getAllMembers()
