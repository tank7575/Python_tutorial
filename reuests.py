import requests

my_request = requests.get('http:')

menu = my_request()

print(menu)

print('Todays Menu;')
for item in menu:
    print(item['name'], ': ' item['desc'].title(), ', $',
                            item['price'], sep='')
