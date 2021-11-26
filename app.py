text = 'EXAMPLE TEXT'

data = {}
sorted_dict = {}
keysDict = {}
done = {}
routes = {}
encodedText = ""

for i in text.upper():
    if i in data:
        data[i]['val'] += 1
    else:
        data[i] = {'val': 1}

sorted_keys = sorted(data, key=lambda x : data[x]["val"], reverse=True)

while len(sorted_keys) > 1:
    ak = sorted_keys.pop()
    bk = sorted_keys.pop()
    akval = data[ak]['val']
    bkval = data[bk]['val']
    totalval = akval + bkval
    done[ak], done[bk] = data[ak], data[bk]
    del data[ak], data[bk]
    data[str(ak + bk)] = {'val': totalval, 'left': ak, 'right': bk}
    sorted_keys = sorted(data, key=lambda x : data[x]["val"], reverse=True)
done[list(data.keys())[0]] = list(data.values())[0]
#print('done:', done, '\n\ndata:', data)

def trace(currentNode, char, route):
    if 'left' in done[currentNode]:
        if char in done[currentNode]['left']:
            newRoute = route + '0'
            trace(done[currentNode]['left'], char, newRoute)
    if 'right' in done[currentNode]:
        if char in done[currentNode]['right']:
            newRoute = route + '1'
            trace(done[currentNode]['right'], char, newRoute)
    if 'left' not in done[currentNode]:
        if 'right' not in done[currentNode]:
            routes[char] = route

rootNode = list(data.keys())[0]
for i in rootNode:
    trace(rootNode, i, '')
for i in text.upper():
    encodedText += routes[i]

print('\n\nRoutes:', routes)
print(encodedText)
