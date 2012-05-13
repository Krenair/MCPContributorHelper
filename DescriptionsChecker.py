import ContributorTools
latin_lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def outputMember (member):
    #print member['searge'] + ' (' + {'0':'client', '1':'server'}[member['side']] + '):', member['desc']
    commandName = 'fs' + {'0':'c', '1':'s'}[member['side']] + {'i':'f', 'u':'m'}[member['searge'][1]]
    print commandName, member['searge'], member['name'], member['desc']

for member in ContributorTools.getMemberListFromCsvs():
    if member['desc'] == '':
        continue
    #elif member['desc'][0] == '\'':
        #outputMember(member)
    elif "@" in member['desc']:
        outputMember(member)
    #elif member['desc'][0].lower() == member['desc'][0] and member['desc'][0] in latin_lowercase_letters:
        #if member['desc'][0] in ['x', 'y', 'z'] and member['desc'][1] == ' ':
            #continue
        #outputMember(member)
    #elif 'j,' in member['desc'] or 'i,' in member['desc'] or 'k, ' in member['desc']:
        #outputMember(member)
