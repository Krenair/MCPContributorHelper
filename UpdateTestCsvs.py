import ContributorTools, os

pipe = os.popen('wget http://mcp.ocean-labs.de/files/mcptest/methods.csv -O - > ' + ContributorTools.mcpPath + 'conf/test_methods.csv')
print pipe.readline().strip()
pipe.close()

pipe = os.popen('wget http://mcp.ocean-labs.de/files/mcptest/fields.csv -O - > ' + ContributorTools.mcpPath + 'conf/test_fields.csv')
print pipe.readline().strip()
pipe.close()
