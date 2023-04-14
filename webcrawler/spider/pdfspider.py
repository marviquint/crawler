import scrapy


class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.dccourts.gov/court-of-appeals/dccarules']

    custom_settings = {
        'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
        'FILES_STORE': '/path/to/your/files/folder',
    }

    def parse(self, response):
        # Extract the links to the PDF files and yield requests to download them
        pdf_links = response.css('a[href$=".pdf"]::attr(href)').getall()
        for pdf_link in pdf_links:
            yield scrapy.Request(pdf_link, callback=self.save_pdf)

    def save_pdf(self, response):
        # Extract the filename from the response and return a dict with file_urls and filename
        filename = response.headers.get('Content-Disposition').decode('utf-8').split('filename=')[-1]
        return {'file_urls': [response.url], 'filename': filename}
