import ContributorTools, os

pipe = os.popen('wget http://mcp.ocean-labs.de/files/mcptest/methods.csv -O ' + ContributorTools.mcpPath + 'conf/' + ContributorTools.csvPrefix + 'methods.csv')
print pipe.readline().strip()
pipe.close()

pipe = os.popen('wget http://mcp.ocean-labs.de/files/mcptest/fields.csv -O ' + ContributorTools.mcpPath + 'conf/' + ContributorTools.csvPrefix + 'fields.csv')
print pipe.readline().strip()
pipe.close()
