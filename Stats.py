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

def output(side, memberType):
    data = stats[side][memberType]
    total = ' ' * (5 - len(str(data['total']))) + str(data['total'])
    renamed = ' ' * (5 - len(str(data['renamed']))) + str(data['total'])
    unnamed = ' ' * (5 - len(str(data['unnamed']))) + str(data['unnamed'])
    percent = str(round(float(data['renamed']) / float(data['total']) * 100, 2)).ljust(5, '0')
    return '[' + side[0].upper() + '][' + memberType.upper().rjust(7) + '] : T' + total + ' | R' + renamed + ' | U' + unnamed + ' | ' + percent + '%'

print output('client', 'methods')
print output('client', 'fields')
print output('client', 'both')
print output('server', 'methods')
print output('server', 'fields')
print output('server', 'both')
print output('both', 'methods')
print output('both', 'fields')
print output('both', 'both')
