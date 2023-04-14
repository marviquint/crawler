from django.shortcuts import render
from django.http import HttpResponse
import scrapydo
from webcrawler.spider.pdfspider import MySpider
from scrapy.exceptions import CloseSpider

def download_pdf(request):
    scrapydo.setup()
    try:
        scrapydo.run_spider(MySpider)  # Pass the class name instead of the object
    except CloseSpider as e:
        return HttpResponse(f"An error occurred: {e}")
    return render(request, 'crawler/crawl_website.html')


# from django.http import FileResponse
# from django.shortcuts import get_object_or_404
# from django.views import View
# from crawler.models import PDFFile
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from subprocess import Popen, PIPE
# import os

# class PDFDetailView(View):
#     def get(self, request, pk):
#         pdf_file = get_object_or_404(PDFFile, pk=pk)
#         response = FileResponse(open(pdf_file.file.path, "rb"), content_type="application/pdf")
#         response['Content-Disposition'] = f'inline; filename="{pdf_file.filename}"'
#         return response
# @csrf_exempt
# def crawl_website(request):
#     if request.method == 'POST':
#         os.environ['SCRAPY_PROJECT'] = 'Users\InnoCSR\Documents\webcrawler\webcrawler'
#         process = Popen(['scrapy', 'crawl', 'pdf_spider'], stdout=PIPE, stderr=PIPE)
#         output, error = process.communicate()
#         return render(request, 'crawler/crawl_website.html', {'output': output, 'error': error})
#     else:
#         return render(request, 'crawler/crawl_website.html')



# from django.shortcuts import render
# from django.http import HttpResponse
# from multiprocessing import Process, Queue
# import scrapy.utils.project as proj
# from scrapy.crawler import CrawlerProcess
# from webcrawler.spider.myspider import MySpider

# def run_spider(queue):
#     spider_cls = MySpider
#     settings = proj.get_project_settings()
#     crawler = CrawlerProcess(settings)
#     crawler.crawl(spider_cls, queue=queue)
#     crawler.start()
#     crawler.stop()
    
# def crawl_books(request):
#     queue = Queue()
#     p = Process(target=run_spider, args=(queue,))
#     p.start()
#     p.join()

#     # Retrieve data from the queue
#     data = []
#     while not queue.empty():
#         data.append(queue.get())

#     # Create a dictionary to hold the data and pass it to the template
#     context = {'data': data}

#     # Render the template with the data
#     return render(request, 'crawler/crawl_books.html', context)
