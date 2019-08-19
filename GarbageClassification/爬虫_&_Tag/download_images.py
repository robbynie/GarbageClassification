# Downloading images form garbage classification training
# @Copyright, Huawei CBG, Cloud Services
# Initialied by Robby, niebuyang@huawei.com

from google_images_download import google_images_download   
response = google_images_download.googleimagesdownload()   

# Set the Dwonload meta data
listKey = ['newspaper', 
            'Carton',
            'book',
            'plastic aluminum mixed packaging box',
            'envelope',
            'Paper bag',
            'plastic bottle',
            'plastic toys',
            'Plastic oil drum',
            'Emulsion tank',
            'Crisper box',
            'Foam plastic',
            'Plastic hangers',
            'Wine bottle',
            'glass',
            'Glass magnifier',
            'Window glass',
            'shattered glass',
            'Cans',
            'pot',
            'screwdriver',
            'Knife',
            'Nail clipper',
            'blade',
            'leather shoes',
            'clothes',
            'Sheets',
            'pillows',
            'package',
            'Plush toy',
            'Circuit board',
            'wire',
            'socket',
            'Building Blocks',
            'Sticky board']

#Start downloading
for item in listKey:
    print(item)
    #arguments = {"keywords":item,"limit":2,"px":"proxyhk.huawei.com:8080"}
    arguments = {"keywords":item,"limit":200,"chromedriver":"C:\Chromdriver\chromedriver.exe"}
    response.download(arguments)

