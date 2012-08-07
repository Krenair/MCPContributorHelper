import ContributorTools
print 'client,server'
for member in ContributorTools.members['0'].keys():
    if member in ContributorTools.members['1'].keys():
        print member + ',' + member
