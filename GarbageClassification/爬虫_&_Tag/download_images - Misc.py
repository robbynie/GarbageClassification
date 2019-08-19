# Downloading images form garbage classification training
# @Copyright, Huawei CBG, Cloud Services
# Initialied by Robby, niebuyang@huawei.com

from google_images_download import google_images_download   
response = google_images_download.googleimagesdownload()   

# Set the Dwonload meta data
listKey = ['sofa', 
            'mattress',
            'bed',
            'table',
            'Broken toilet',
            'Gravel block',
            'Broken brick',
            'Waste mortar',
            'refrigerator',
            'washing machine',
            'air conditioning',
            'TV set',
            'Mobile phone',
            'Laptop',
            'Rice cooker']

#Start downloading
for item in listKey:
    print(item)
    #arguments = {"keywords":item,"limit":2,"px":"proxyhk.huawei.com:8080"}
    arguments = {"keywords":item,"limit":200,"chromedriver":"C:\Chromdriver\chromedriver.exe","output_directory":"./Misc garbage"}
    response.download(arguments)

