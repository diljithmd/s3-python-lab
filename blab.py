std={'name':'athul ','age':'11','marks':'50'}
print(std)
print(std['name'])
std['age']='22'
print(std)
std.update({'course':'cs'})
print(std)
std.pop('marks')
print(std)
print(std.keys())
print(std.values())
print(std.items())
new=std.copy()
print(new)
dl={}
dl.update(std)
print(dl)
