# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['class-central.com']
    start_urls = ['http://class-central.com/subjects']

    def __init__(self,subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.css('a.text--blue[title*=' + self.subject + ']::attr(href)').extract_first()
            subject_url = response.urljoin(subject_url)
            yield Request(subject_url,callback=self.parse_subject)
        else:
            self.logger.info('Scraping All Subjects !!!')
            alldivs = response.css('li.width-100.medium-up-width-1-2.xlarge-up-width-1-3.col.margin-vert-medium.medium-up-margin-vert-xlarge.medium-up-padding-right-large.xlarge-up-padding-right-xlarge')
            subjects = alldivs.css('a.block::attr(href)').extract()
            for subject in subjects:
                yield Request(response.urljoin(subject),callback=self.parse_subject)

    def parse_subject(self,response):
        pass
    