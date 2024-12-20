
capitales = {'USA':'WashingtonDC',
             'Argentina' : 'Buenos Aires'
}

capitales.update({'Japon':'Tokio'})
capitales.pop('Argentina')
print(capitales['USA'])
print(capitales.get('Rusia'))
print(capitales.keys())
print(capitales.values())
print(capitales.items())