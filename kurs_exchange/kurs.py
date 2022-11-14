import scrapy 
import datetime
import items
from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler

class RateSpider(scrapy.Spider):
    name = 'exchangerate'

    def start_requests(self):
        urls = [
            'https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/default.aspx'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for i in range(1,26):
            df_rate = items.ExchangeRateItem()
            for rate in response.css('#ctl00_PlaceHolderMain_g_6c89d4ad_107f_437d_bd54_8fda17b556bf_ctl00_GridView1 > table > tbody'):
                df_rate['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                df_rate['mata_uang'] = rate.css('tr:nth-child(' + str(i) + ') > td:nth-child(1)::text').get(),
                df_rate['nilai'] = rate.css('tr:nth-child(' + str(i) + ') > td:nth-child(2)::text').get(),
                df_rate['kurs_jual'] = rate.css('tr:nth-child(' + str(i) + ') > td:nth-child(3)::text').get(),
                df_rate['kurs_beli'] = rate.css('tr:nth-child(' + str(i) + ') > td:nth-child(4)::text').get()
                
                yield df_rate

process = CrawlerProcess(settings={
    "FEEDS": {
        "data/exchange_data.csv": {
            "format": "csv",
            "overwrite": True,
        },
    },
})
scheduler = TwistedScheduler()
scheduler.add_job(process.crawl, 'interval', args=[RateSpider], hours=0, minutes=0, seconds=1)
scheduler.start()
process.start(False)