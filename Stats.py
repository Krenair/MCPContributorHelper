import ContributorTools

stats = {
  'client': {
    'methods': {'total': 0, 'renamed': 0, 'unnamed': 0},
    'fields': {'total': 0, 'renamed': 0, 'unnamed': 0},
    'both': {'total': 0, 'renamed': 0, 'unnamed': 0}
  },
  'server': {
    'methods': {'total': 0, 'renamed': 0, 'unnamed': 0},
    'fields': {'total': 0, 'renamed': 0, 'unnamed': 0},
    'both': {'total': 0, 'renamed': 0, 'unnamed': 0}
  },
  'both': {
    'methods': {'total': 0, 'renamed': 0, 'unnamed': 0},
    'fields': {'total': 0, 'renamed': 0, 'unnamed': 0},
    'both': {'total': 0, 'renamed': 0, 'unnamed': 0}
  }
}

def recordStat(side, memberType, stat):
    stats[side][memberType][stat] += 1
    stats[side]['both'][stat] += 1
    stats['both'][memberType][stat] += 1
    stats['both']['both'][stat] += 1

for side, sideMembers in ContributorTools.getAllMembers().items():
    sideName = {'0': 'client', '1': 'server'}[side]
    for name, info in sideMembers.items():
        memberType = {'func_': 'methods', 'field': 'fields'}[info['searge'][:5]]
        recordStat(sideName, memberType, 'total')

        if info['searge'] == info['name'] and info['desc'] == '':
            recordStat(sideName, memberType, 'unnamed')
        else:
            recordStat(sideName, memberType, 'renamed')

def output(d):
    p = str(round(float(d['renamed']) / float(d['total']) * 100, 2)).ljust(5, '0')
    return ' T ' + str(d['total']) + ' | R ' + str(d['renamed']) + ' | U ' + str(d['unnamed']) + ' | ' + p + '%'

def outputSmallUnnamed(d):
    p = str(round(float(d['renamed']) / float(d['total']) * 100, 2)).ljust(5, '0')
    return ' T ' + str(d['total']) + ' | R ' + str(d['renamed']) + ' | U  ' + str(d['unnamed']) + ' | ' + p + '%'

def outputBig(d):
    p = str(round(float(d['renamed']) / float(d['total']) * 100, 2)).ljust(5, '0')
    return ' T' + str(d['total']) + ' | R' + str(d['renamed']) + ' | U ' + str(d['unnamed']) + ' | ' + p + '%'

print '[C][METHODS] :' + outputSmallUnnamed(stats['client']['methods'])
print '[C][ FIELDS] :' + outputSmallUnnamed(stats['client']['fields'])
print '[C][   BOTH] :' + output(stats['client']['both'])
print '[S][METHODS] :' + outputSmallUnnamed(stats['server']['methods'])
print '[S][ FIELDS] :' + outputSmallUnnamed(stats['server']['fields'])
print '[S][   BOTH] :' + outputSmallUnnamed(stats['server']['both'])
print '[B][METHODS] :' + outputSmallUnnamed(stats['both']['methods'])
print '[B][ FIELDS] :' + output(stats['both']['fields'])
print '[B][   BOTH] :' + outputBig(stats['both']['both'])
