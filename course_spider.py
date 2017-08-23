import scrapy
import sys
import os
import re
import json


class CourseSpider(scrapy.Spider):
    name = 'course'

    # From https://sac.epfl.ch/page-128071.html
    # through https://sac.epfl.ch/page-128085.html
    start_urls = ['https://sac.epfl.ch/page-1280{}.html'.format(x)
                      for x in range(71, 86)]

    def parse(self, response):
        for href in response.css('div.htmlBox div.relative a::attr("href")') \
                        .extract():
            if href.endswith('fr'):
                href = href[:-2] + 'en'
            next_page = href
            yield response.follow(next_page, callback=self.parse_course_page)

    def parse_course_page(self, response):
        content = response.text[:response.text.find('infocode')]
        content = re.sub(r'\n', '', content)

        def get_var_value(var):
            match_list = re.findall(r'{}.*?>([\S\s]*?)</'.format(var),
                                    content)
            if len(match_list) == 0:
                sys.exit("No match.\nPattern: {}\nText:\n{}\n"
                             .format(pattern, content))
            elif len(match_list) > 1:
                sys.exit("Too many matches.\nPattern: {}\nText:\n{}\n"
                             .format(pattern, content))
            else:
                return match_list[0].strip()

        name = get_var_value('MATIERE_EN')
        code = get_var_value('ITEMPLAN_CODE')
        credits = get_var_value('ITEMPLAN_ECTS_OU_COEFF')
        period = get_var_value('ITEMPLAN_PERIODE_SEMESTRE')

        yield {
            'name': name,
            'code': code,
            'credits': credits,
            'period': period,
        }

    def closed(self, reason):
        print('Scraping finished, removing duplicates.')
        if os.path.isfile('scraped_course_data.json'):
            infile = open('scraped_course_data.json', 'r')
            data = json.load(infile)
            infile.close()
            courses = {item['code'] : item for item in data}.values()
            outfile = open('scraped_course_data.json', 'w')
            json.dump(list(courses), outfile)
            outfile.close()
            print('Done.')
        else:
            sys.exit("'scraped_course_data.json' not found")
