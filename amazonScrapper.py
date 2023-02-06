from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for
import json
import requests


scrapper = Flask(__name__)

SearchThis = 'shirt'

@scrapper.route('/', methods = ['Post', 'Get'])
def getData():
    global SearchThis
    if request.method == 'POST':
        SearchThisPP = request.form['searchThisStuff']
         
        SearchThis = SearchThisPP

        print(SearchThis)
        headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'}

        AmazonSearchBarUrl = 'https://www.amazon.in/s?k='
        MintraSearchBarUrl = 'https://www.myntra.com/'
        FlipkartSearchBarUrl = 'https://www.flipkart.com/search?q='
        SnapdealSearchBarUrl = 'https://www.snapdeal.com/search?keyword='

        # SearchThis = input("What do want to search : ")
        # SearchThis = "shirt" 
        PageAmazon = requests.get(AmazonSearchBarUrl+SearchThis, headers=headers).text
        PageMintra = requests.get(MintraSearchBarUrl+SearchThis, headers= headers).text
        PageFlipkart = requests.get(FlipkartSearchBarUrl+SearchThis, headers=headers).text
        PageSnapdeal = requests.get(SnapdealSearchBarUrl+SearchThis, headers= headers).text


        soupAmazon = BeautifulSoup(PageAmazon, 'lxml')
        soupMintra = BeautifulSoup(PageMintra, 'lxml')
        soupFlipkart = BeautifulSoup(PageFlipkart, 'lxml')
        soupSnapdeal = BeautifulSoup(PageSnapdeal, 'lxml')

        # Getting Product from Amazon
        outputAmazonMainDiv = soupAmazon.find('div',class_='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1')
        outputAmazonProductInfo = outputAmazonMainDiv.find('div', class_="a-section")
        AmazonProduct = outputAmazonProductInfo.find('a', class_='a-link-normal s-no-outline')

        AmazonProductName = outputAmazonMainDiv.find('h2').text
        AmazonProductPrice = outputAmazonMainDiv.find('span', class_= 'a-price').find('span').text
        AmazonProductLink ='https://www.amazon.in/' + AmazonProduct['href']


        # Getting Product from Snapdeal
        outputSnapdealMainDiv = soupSnapdeal.find('div', class_= 'product-tuple-listing')
        SnapdealProductLink = outputSnapdealMainDiv.find('a')['href']
        SnapdealProductImg = outputSnapdealMainDiv.find('img')
        SnapdealProductName = outputSnapdealMainDiv.find('p').text
        SnapdealProductPrice = outputSnapdealMainDiv.find('div', class_= 'product-price-row').find('span').text


        # Getting Product from Flipkart
        outputFlipkartMainDiv = soupFlipkart.find('div',class_="_13oc-S")

        # FlipkartProductName = outputFlipkartMainDiv.find('div', class_= '_4rR01T')
        # FlipkartProductPrice = outputFlipkartMainDiv.find('span', class_= 'a-price').find('span').text
        # FlipkartProductLink ='https://www.flipkart.com/' + FlipkartProduct['href']
        # FilpkartImgLink = FlipkartProduct.find('img')

        return render_template("index.html", AproductPrice = AmazonProductPrice, AproductName = AmazonProductName, AproductLink = AmazonProductLink
                                            , SproductName = SnapdealProductName, SproductPrice = SnapdealProductPrice, SproductLink = SnapdealProductLink)

    else:
        headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'}

        AmazonSearchBarUrl = 'https://www.amazon.in/s?k='
        MintraSearchBarUrl = 'https://www.myntra.com/'
        FlipkartSearchBarUrl = 'https://www.flipkart.com/search?q='
        SnapdealSearchBarUrl = 'https://www.snapdeal.com/search?keyword='

        # SearchThis = input("What do want to search : ")
        # SearchThis = "shirt" 
        PageAmazon = requests.get(AmazonSearchBarUrl+SearchThis, headers=headers).text
        PageMintra = requests.get(MintraSearchBarUrl+SearchThis, headers= headers).text
        PageFlipkart = requests.get(FlipkartSearchBarUrl+SearchThis, headers=headers).text
        PageSnapdeal = requests.get(SnapdealSearchBarUrl+SearchThis, headers= headers).text


        soupAmazon = BeautifulSoup(PageAmazon, 'lxml')
        soupMintra = BeautifulSoup(PageMintra, 'lxml')
        soupFlipkart = BeautifulSoup(PageFlipkart, 'lxml')
        soupSnapdeal = BeautifulSoup(PageSnapdeal, 'lxml')

        # Getting Product from Amazon
        outputAmazonMainDiv = soupAmazon.find('div',class_='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1')
        outputAmazonProductInfo = outputAmazonMainDiv.find('div', class_="a-section")
        AmazonProduct = outputAmazonProductInfo.find('a', class_='a-link-normal s-no-outline')

        AmazonProductName = outputAmazonMainDiv.find('h2').text
        AmazonProductPrice = outputAmazonMainDiv.find('span', class_= 'a-price').find('span').text
        AmazonProductLink ='https://www.amazon.in/' + AmazonProduct['href']


        # Getting Product from Snapdeal
        outputSnapdealMainDiv = soupSnapdeal.find('div', class_= 'product-tuple-listing')
        SnapdealProductLink = outputSnapdealMainDiv.find('a')['href']
        SnapdealProductImg = outputSnapdealMainDiv.find('img')
        SnapdealProductName = outputSnapdealMainDiv.find('p').text
        SnapdealProductPrice = outputSnapdealMainDiv.find('div', class_= 'product-price-row').find('span').text


        # Getting Product from Flipkart
        outputFlipkartMainDiv = soupFlipkart.find('div',class_="_13oc-S")

        # FlipkartProductName = outputFlipkartMainDiv.find('div', class_= '_4rR01T')
        # FlipkartProductPrice = outputFlipkartMainDiv.find('span', class_= 'a-price').find('span').text
        # FlipkartProductLink ='https://www.flipkart.com/' + FlipkartProduct['href']
        # FilpkartImgLink = FlipkartProduct.find('img')

        return render_template("index.html", AproductPrice = AmazonProductPrice, AproductName = AmazonProductName, AproductLink = AmazonProductLink
                                            , SproductName = SnapdealProductName, SproductPrice = SnapdealProductPrice, SproductLink = SnapdealProductLink)

scrapper.run(host="0.0.0.0", port= 8080)