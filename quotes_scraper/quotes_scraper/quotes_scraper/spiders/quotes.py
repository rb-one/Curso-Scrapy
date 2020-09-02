import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top Ten Tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()
# Next page button = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()


class QoutesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    # uso custom settings para archivo
    custom_settings = {
        #guardado de archivos
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
        # numero maximo peticiones asincronas 
        'CONCURRENT_REQUEST': 24,
        # maximo de ram
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['rb@rb.com'],
        # No violar pautas de robots.txt
        'ROBOTSTXT_OBEY': True,
        # custom User Agent
        'USER_AGENT': 'ElmerHomero',
        # Cambiar el encoding del archivo
        'FEED_EXPORT_ENCODING': ' utf-8'
    }

    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
        quotes.extend(response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall())

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link,
                                  callback=self.parse_only_quotes,
                                  cb_kwargs={'quotes': quotes})
        else:
            yield {
                'quotes': quotes,
            }

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()
        top_tags = response.xpath(
            '//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()

        top = getattr(self, 'top', None)
        
        if top:
            top = int(top)
            top_tags

        yield {
            'title': title,
            'top_tags': top_tags[:top]
        }

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link,
                                  callback=self.parse_only_quotes,
                                  cb_kwargs={'quotes': quotes})
