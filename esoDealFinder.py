#Import requests (to download the page)
import requests

#Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

#Import Time (to add a delay between the times the scape runs)
import time

#Import Reg Expressions for parsing strings whitespace
import re

import random

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.


filename = "testScrape"
filename2 = "testScrape2"
filename3 = "testScrape3"
filename4 = "testScrape4"
filename5 = "testScrape5"
filename6 = "testScrape6"

urlArr = []
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=8182&ItemNamePattern=Scrib+Jelly&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=250")   #Scrib Jelly
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=11979&ItemNamePattern=Decorative+Wax&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=250")   #Decorative Wax
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=2069&ItemNamePattern=Dwemer+Frame&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=600")   #Dwemer Frame
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=6132&ItemNamePattern=Perfect+Roe&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=21200")   #Perfect Roe
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=1114&ItemNamePattern=Kuta&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=2000")   #Kuta
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=2677&ItemNamePattern=Rosin&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=3300")   #Rosin
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=5687&ItemNamePattern=Tempering+Alloy&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=9500")   #Tempering Alloy
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=211&ItemNamePattern=Dreugh+Wax&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=10000")   #Dreugh Wax
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=3790&ItemNamePattern=Potent+Nirncrux&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=25000")   #Potent Nirncrux
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=11971&ItemNamePattern=&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=5&AmountMax=&PriceMin=&PriceMax=400")   #Heartwood
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=4794&ItemNamePattern=Hakeijo&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=27000")   #Hakeijo
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=10368&ItemNamePattern=Ring+of+a+Mother%27s+Sorrow&ItemCategory1ID=&ItemTraitID=&ItemQualityID=3&IsChampionPoint=true&IsChampionPoint=false&LevelMin=160&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=31000")   #Ring of Mother's Sorrow
urlArr.append("https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=10367&ItemNamePattern=Necklace+of+a+Mother%27s+Sorrow&ItemCategory1ID=&ItemTraitID=&ItemQualityID=3&IsChampionPoint=true&IsChampionPoint=false&LevelMin=160&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=40000")   #Necklace of Mother's Sorrow

# set the headers like we are a browser,
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'referer': 'https://us.tamrieltradecentre.com/pc/Trade',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'us.tamrieltradecentre.com',
    'TE': 'Trailers',
    'Upgrade-Insecure-Requests': '1'}
maxEntriesPerPage = 5
maxMinsElapsed = 4

# open a session
session = requests.Session()

# while this is true (it is true by default),
while True:

    """
    #Testing to purposely scrape a reCAPTCHA
    # download the homepage
    response = requests.get(urlArr[0], headers=headers)
    # parse the downloaded homepage and grab all text
    soup = BeautifulSoup(response.text, "lxml")
    captchaFinder = soup.find_all('h5', {'class': 'text-danger'})
    if (len(captchaFinder) > 0):
        print("Captcha solution required")
    """
    
    for url in urlArr:
        
        # download the homepage
        response = session.get(url, headers=headers)
        # parse the downloaded homepage and grab all text
        soup = BeautifulSoup(response.text, "lxml")
        
        captchaFinder = soup.find_all('h5', {'class': 'text-danger'})
        dataArr = soup.find_all('tr', {'class': 'cursor-pointer'})
        minsElapsedArr = soup.find_all('td', {'class': 'bold hidden-xs'})
        validEntries = 0

        if (len(captchaFinder) > 0):
            print("Captcha solution required")
            input("Press Enter to continue when captcha has been solved...")
            #time.sleep(10)
        else:
            #Doing the below min() check ensures that we don't try to access the array out of bounds
            for i in range(min(maxEntriesPerPage, len(minsElapsedArr))):    
                tmpMinsElapsedSplit = str(minsElapsedArr[i]).split("\"")
                tmpMinsElapsed = int(tmpMinsElapsedSplit[3])
                if (tmpMinsElapsed <= maxMinsElapsed):
                    validEntries += 1
                    minsElapsedArr[i] = tmpMinsElapsed
                else:
                    break
            
            dataArrParsed = []
            if (validEntries > 0):
                print("========================")
                for i in range(validEntries):
                    tmpData = str(dataArr[i].get_text()).strip()
                    tmpData = tmpData.replace("    ", "")
                    tmpData = "\n".join([ll.rstrip() for ll in tmpData.splitlines() if ll.strip()])
                    tmpDataSplit = tmpData.split("\n")
                    tmpData = tmpDataSplit[0] + "\t |  " + str(minsElapsedArr[i]) + " mins ago" + "\n" + tmpDataSplit[4] + "\n" + tmpDataSplit[5] + "\n" + tmpDataSplit[6] + "g " + tmpDataSplit[7] + " " + tmpDataSplit[8] + " units " + tmpDataSplit[9] + " " + tmpDataSplit[10] + "g"
                    dataArrParsed.append(tmpData)    

                for entry in dataArrParsed:
                    print(entry)
                    print()
                print("========================")
            time.sleep(random.uniform(3.0, 4.25))    
    
