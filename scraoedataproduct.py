from bs4 import BeautifulSoup 
import requests 
import numpy as np
import pandas as pd

links=[
"https://disty.ma/can-acc-ap/10145-ef-50mm-f-1-8-stm.html",
"https://disty.ma/can-acc-ap/10146-ef-24-105mm-f-4l-is-ii-usm.html",
"https://disty.ma/can-acc-ap/10149-ef-24-70mm-f-28-l-ii-usm.html",
"https://disty.ma/can-acc-ap/10150-ef-16-35mm-f-28l-iii-usm.html",
"https://disty.ma/can-acc-ap/10152-speedlite-430-ex-iii-rt.html",
"https://disty.ma/can-acc-ap/10154-canon-kp-108in-kit-encre-et-papier-photo.html",
"https://disty.ma/can-acc-ap/10155-lc-e6.html",
"https://disty.ma/can-acc-ap/10157-ef70-200mm-f-28l-is-iii-usm.html",
"https://disty.ma/can-acc-ap/10158-canon-objectif-rf24-70mm-f28-l-is-usm.html",
"https://disty.ma/can-acc-ap/10159-canon-objectif-rf50mm-f-12l-usm.html",
"https://disty.ma/can-acc-ap/10160-canon-objectif-rf15-35mm-f28-l-is-usm.html",
"https://disty.ma/objectif/10692-canon-lens-ew-63ii-lens-hood.html",
"https://disty.ma/selphy/10685-cp-1300-black.html",
"https://disty.ma/objectif/12466-canon-objectif-rf24-105mm-f-4l-is-usm.html",
"https://disty.ma/accessoire/12898-canon-binoculars-10x20-is.html",
"https://disty.ma/jumelle/12899-canon-binoculars-12x36-is-iii.html",
"https://disty.ma/adaptateur/13020-canon-mount-adapter-ef-eos-r.html",
"https://disty.ma/objectif/13021-canon-objectif-rf-100-f-28l-is-macro-usm.html",
"https://disty.ma/batterie/13022-canon-battery-pack-lp-e17.html",
"https://disty.ma/chargeur/13023-canon-chargeur-lc-e17e.html",
"https://disty.ma/objectif/13024-canon-rf-50mm-f18-stm.html",
"https://disty.ma/sacoche/13102-canon-backpack-bp100-blue.html",
]




titles=[]
prices=[]
images=[]
descs=[]




for link in links:
    
        try:

            response = requests.get(link)  
            soup = BeautifulSoup(response.text, "html.parser") 

            try:
                title = soup.find("h2")
                titles.append(title.text)
            except:
                title = "Not Available"
                titles.append(title)
            try:
                price = soup.find("p", class_="our_price_display")
                prices.append(price.text)
            except:
                price = "Not Available"
                prices.append(price)
            try:
                image = soup.find("img", id="bigpic")
                images.append(image.get('src'))
            except:
                image = "Not Available"
                images.append(image)
            try:
                desc = soup.find("p", id = "short_description_content")
                descs.append(desc.text)
            except:
                desc = "Not Available"
                descs.append(desc)
            print('gfrfgdrfgerr')
        except:
            pass

df_marks = pd.DataFrame({
            'Type': 'simple',
            'Name': titles,
            'Regular price': prices,
            'Images': images,
            'Short description': descs,
            'Published': 1,
            'Is featured?':1,
            'Visibility in catalog':'visible',
            'Categories': 'Ordinateurs > Tout en un (AIO)'


        })
writer = pd.ExcelWriter('output.xlsx')
df_marks.to_excel(writer, 'products')
writer.save()






