#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors import LinkExtractor
import scrapy
from cartrade.items import CartradeItem
from scrapy.spider import BaseSpider

class CarDekhoSpider(BaseSpider):
    name="carDekho"
    #strr=''
    #def __init__(self,stra=''):
     #   self.strr=stra
    allowed_domains=['cardekho.com']
    start_urls=['http://www.cardekho.com/used-cars+in+delhi-ncr']
    #def start_requests(self):
     #   for i in range(2,62):
      #      yield self.make_requests_from_url("http://www.cardekho.com/used-cars+in+delhi-ncr/%d"%i)
   
    #rules=[Rule(LinkExtractor(restrict_xpaths=('//div[@class="cartitle"]/a')), callback='parse_item'),
     #      Rule(LinkExtractor(allow=("http://www.cardekho.com/used-car-details/",)), callback='parse_item'),
      #     ]
    def parse(self, response):
        for sel in response.xpath('//ul[@id="content"]/li'):
            item=CartradeItem()
            city=sel.xpath('div[1]/div[3]/div[2]/div[2]/span[1]/text()').extract()
            yom=sel.xpath('div[1]/div[2]/div[3]/ul/li[2]/div[2]/span/text()').extract()
            yom_str=''.join(yom)
            yom2=yom_str.split(' ')
            yomf=yom2[0]
            price=sel.xpath('div[1]/div[3]/div[1]/text()').extract()
            kms=sel.xpath('div[1]/div[2]/div[3]/ul/li[1]/div[2]/span/text()').extract()
            str_price=''.join(price)
            str_stripped_price=" ".join(str_price.split())
            transm=sel.xpath('div[1]/div[2]/div[3]/ul/li[4]/div[2]/text()').extract()
            fuel=sel.xpath('div[1]/div[2]/div[3]/ul/li[3]/div[2]/text()').extract()
            model=sel.xpath('div[1]/div[2]/div[1]/a/text()').extract()
            owner=sel.xpath('div[1]/div[2]/div[3]/ul/li[6]/div[2]/text()').extract()
            url=sel.xpath('div[1]/div[2]/div[1]/a/@href').extract()
            str_model=''.join(model)
            item['model']=str_model
            item['price']=str_stripped_price
            item['kms']=kms
            item['transm']=transm
            item['fuel']=fuel
            item['yom']=yomf
            item['city']=city
            item['owner']=owner
            item['url']=url
            url_str=''.join(sel.xpath("div[1]/div[2]/div[1]/a/@href").extract())
            request=scrapy.Request(url_str,callback=self.parse2)
            request.meta['item']=item
            yield request
            
    def parse2(self,response):
        item=response.meta['item']
        item['carid']=response.xpath('/html/body/main/div[1]/div[1]/div[4]/div[2]/div[5]/div[2]/text()').extract()
        yield item
