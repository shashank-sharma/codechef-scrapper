import scrapy

class LoginSpider(scrapy.Spider):

    def __init__(self):
        self.name = []
        self.code = []
        self.successful_submission = []
        self.accuracy = []
        self.answer = []
        self.count = -1

    name = 'codespider'
    start_urls = ['https://www.codechef.com/problems/school']

    def getAnswer(self, response):
        answer = []
        a = response.css('tbody')
        for i in a.css('tr'):
            answer.append(i.css('td::text').extract()[0])
        self.count += 1
        return {
            'name': self.name[self.count],
            'code': self.code[self.count],
            'successful_submission': self.successful_submission[self.count],
            'accuracy': self.accuracy[self.count],
            'answer': answer,
        }
        '''
        self.result = []
        a = response.css('tbody')
        for i in a.css('tr'):
            self.result.append(i.css('td::text').extract()[0])
        yield self.result
        '''


    def parse(self, response):
        ll = []
        #response.css('div.problemname a::attr(href)').re(r'problems.*')
        for link in response.css('tr.problemrow'):
            self.name.append(link.css('div.problemname b::text').extract()[0])
            self.code.append(link.css('td a::text').extract()[2])
            self.successful_submission.append(link.css('td div::text').extract()[2])
            self.accuracy.append(link.css('td a::text').extract()[3])

            ans = 'https://www.codechef.com/status/' + link.css('td a::text').extract()[2]
            yield scrapy.Request(url = ans, callback = self.getAnswer)




'''


import scrapy

class LoginSpider(scrapy.Spider):
    result = []

    name = 'codespider'
    start_urls = ['https://www.codechef.com/problems/school']

    def getAnswer(self, response):
        item = response.meta['item']
        return item

    def parse(self, response):
        #response.css('div.problemname a::attr(href)').re(r'problems.*')
        for link in response.css('tr.problemrow'):
            ans = 'https://www.codechef.com/status/' + link.css('td a::text').extract()[2]
            #answer = getAnswer(ans, self.)
            #answer = scrapy.Request(ans, callback=self.getAnswer, dont_filter=True)
            answer = scrapy.Request(ans, callback=self.getAnswer, dont_filter=True)
            print('\n\n\n')
            print(answer)
            yield {
                'name': link.css('div.problemname b::text').extract()[0],
                'code': link.css('td a::text').extract()[2],
                'successful_submission': link.css('td div::text').extract()[2],
                'accuracy': link.css('td a::text').extract()[3],
                'answer': self.result,
            }


'''