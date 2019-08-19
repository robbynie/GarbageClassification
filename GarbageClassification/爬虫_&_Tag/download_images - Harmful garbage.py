# Downloading images form garbage classification training
# @Copyright, Huawei CBG, Cloud Services
# Initialied by Robby, niebuyang@huawei.com

from google_images_download import google_images_download   
response = google_images_download.googleimagesdownload()   

# Set the Dwonload meta data
listKey = ['Rechargeable Battery', 
            'Nickel chrome battery',
            'Aluminic acid battery',
            'Battery',
            'Button Battery',
            'Fluorescent lamp',
            'Energy saving lamp',
            'Halogen lamp',
            'Expired drug',
            'Pharmaceutical Packaging',
            'Pill',
            'Expired capsule drug',
            'Mercury blood pressure monitor',
            'Mercury thermometer',
            'Disinfectant',
            'Rat medicine',
            'Insecticide spray',
            'X-ray film',
            'Photo film']

#Start downloading
for item in listKey:
    print(item)
    #arguments = {"keywords":item,"limit":2,"px":"proxyhk.huawei.com:8080"}
    arguments = {"keywords":item,"limit":200,"chromedriver":"C:\Chromdriver\chromedriver.exe","output_directory":"./Harmful garbage"}
    response.download(arguments)

