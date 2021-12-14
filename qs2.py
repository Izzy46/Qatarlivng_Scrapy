import scrapy
import time

class Qs2Spider(scrapy.Spider):
    name = 'qs2'
    allowed_domains = ['www.qatarsale.com']
    start_urls = ['https://www.qatarsale.com/EnMain.aspx']

    def parse(self, response):
        posts = response.xpath("//tr[@style='height:88px;white-space:nowrap;']")
        for post in posts:
            make = post.xpath(".//span[contains(@id,'Label10')]/text()").get()
            model = post.xpath(".//span[contains(@id,'Label3')]/text()").get()
            version = post.xpath(".//span[contains(@id,'Label11')]/text()").get()
            firstreg = post.xpath(".//span[contains(@id, 'Label6')]/text()").get()
            price = post.xpath(".//span[contains(@id, 'Label4')]/text()").get()
            mileage = post.xpath(".//span[contains(@id, 'Label5')]/text()").get()
            url = post.xpath(".//input[contains(@name, 'ImageButton1')]/@onclick").get()
            seller_type = post.xpath(".//span['Label1' = substring(@id, string-length(@id) - string-length('Label1') +1)]/text()").get()
            website = 'QatarSale'
            scrape_time = time.time()
            
            yield{
                'make' : make,
                'model' : model, 
                'version' : version,  
                'firstreg' : firstreg,
                'price' : price,
                'mileage' : mileage,
                'url' : url,
                'seller_type' : seller_type,
                'website' : website,
                'scrape_time' : scrape_time
            }