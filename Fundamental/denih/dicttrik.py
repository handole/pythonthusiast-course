ages = {
    'Mung' : 32,
    'Jong' : 31,
    'Fan'  : 29
}

# bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknown'
print('Dick is %s years old' % age)