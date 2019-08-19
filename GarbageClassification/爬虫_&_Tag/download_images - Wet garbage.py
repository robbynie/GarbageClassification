# Downloading images form garbage classification training
# @Copyright, Huawei CBG, Cloud Services
# Initialied by Robby, niebuyang@huawei.com

from google_images_download import google_images_download   
response = google_images_download.googleimagesdownload()   

# Set the Dwonload meta data
listKey = ['Meals', 
            'bread',
            'Cake biscuit',
            'animal organs',
            'Apple core',
            'chicken',
            'Dried nuts',
            'Fish and shrimp',
            'vegetables',
            'Rice',
            'Beans',
            'medicine dregs',
            'Pet feed',
            'flowers']

#Start downloading
for item in listKey:
    print(item)
    #arguments = {"keywords":item,"limit":2,"px":"proxyhk.huawei.com:8080"}
    arguments = {"keywords":item,"limit":200,"chromedriver":"C:\Chromdriver\chromedriver.exe","output_directory":"./Wet garbage"}
    response.download(arguments)

