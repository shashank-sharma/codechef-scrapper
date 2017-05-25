'''
Codechef spider

Scrapy spider for ScrapingHub project.
Enter start_urls with the given url and rest it will do it for you.

1. Grab all the name, coden submission and accuracy.
2. Join URL and code then check the solution of each problem
3. Solutions are divided into 4 parts with max 50 answers each.
  - C
  - C++
  - Java
  - Python
4. After getting answer it will append to the list and yield it.

'''

import scrapy

class LoginSpider(scrapy.Spider):

    def __init__(self):

        # To first append all the given details and use it later
        # We could have passed the argument through callback
        self.name = []
        self.code = []
        self.successful_submission = []
        self.accuracy = []
        #self.lang = {'114': ' GO', '20': ' D'}
        self.lang = {'11': ' C', '44': ' C++14', '10': ' JAVA', '4': ' PYTH'}
        self.answer = []
        self.count = -1
        self.count1 = 0
        self.ll = ''
        self.kk = ''

    name = 'codespider'

    # URL to start scrapping
    start_urls = ['https://www.codechef.com/problems/school']

    def getAnswer(self, response):
        count1 = 0
        data = response.meta['data']
        a = response.css('tbody')
        if self.lang[self.ll] in response.css('select.field-style1 option::text').extract():
            for i in a.css('tr'):
                try:
                    data['answer'][self.ll].append(i.css('td::text').extract()[0])
                except:
                    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
                    print(i.css('td::text').extract())
                    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')

            if ('/sites/all/themes/abessive/images/page-next-active.gif' in response.text):
                count1 += 1
                ans = 'https://www.codechef.com' + response.css('a::attr(href)').re(r'/status/.*')[0]
                print('-=-=-=-=')
                print(ans)
                yield scrapy.Request(url = ans, callback = self.getAnswer, meta = {'data': data})
        yield data

    def parse(self, response):
        for link in response.css('tr.problemrow'):
            data = {}
            data['name'] = link.css('div.problemname b::text').extract()[0]
            data['code'] = link.css('td a::text').extract()[2]
            data['successfully_submission'] = link.css('td div::text').extract()[2]
            data['accuracy'] = link.css('td a::text').extract()[3]
            data['answer'] = {}

            '''
            Join URL with the given CODE

            Parameters used in URL:

            ?sort_by=Time&sorting_order=asc&language=4&status=15&Submit=GO

            sort_by = Sort the given data
            sorting_order = Ascending or Descending
            language = [4: Python], [116: Python3.4], [44: C++14], [11: C], [10: Java]
            status = [15: Accepted]
            submit = GO (default)

            '''
            for i in self.lang.keys():
                ans = 'https://www.codechef.com/status/' + data['code'] + '?sort_by=Time&sorting_order=asc&language='+str(i)+'&status=15&Submit=GO'
                data['answer'][str(i)] = []
                self.ll = str(i)
                yield scrapy.Request(url = ans, callback = self.getAnswer, meta = {'data': data})