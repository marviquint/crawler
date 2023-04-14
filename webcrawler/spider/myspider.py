import scrapy

class MySpider(scrapy.Spider):
    name = "books"
    start_urls = [
        "http://books.toscrape.com/"
    ]

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('div p.price_color::text').get(),
                'availability': book.css('div p.availability::text').get().strip()
            }

        next_page_url = response.css('li.next a::attr(href)').get()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
