#retrieve image using urllib and as continous sequence of bytes

import urllib.request

host='http://data.pr4e.org/cover3.jpg'
newHost='https://i2.wp.com/ramenswag.com/wp-content/uploads/2016/07/sasuke_wallpaper_4ce23.jpg?resize=300%2C188&ssl=1'

data=urllib.request.urlopen(newHost)

with open('stuff2.jpg','wb') as f:
    while True:
        image=data.read(100000)
        if len(image) < 1: break
        f.write(image)