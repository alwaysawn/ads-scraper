import re
import selenium
from selenium import webdriver
import time

class GetAdsList(object):

    def __init__(self):
        self.browser = None
        self.hotel_words = None
        self.target = None

    def getAds(self):
        print "Opening hotel words file"
        self.hotel_words = open('hotel_keywords.txt', 'r')
        self.target = open('scraped_ads.csv', 'w+')
        heading = "Query|Position|Rank|Title|Domain|Line 1|Line 2|Line 3|Content\n"
        self.target.write(heading)
        for line in self.hotel_words:
            print line
            query_term = line.replace(' ','+')
            query_term = query_term.replace('\n','')
            print query_term
            print "Opening the write file..."
            filename = query_term+'.html'
            page_target = open(filename, 'w+')
            print "working"
            self.browser = webdriver.Firefox()
            self.browser.get('https://www.google.com/#q='+query_term)
            time.sleep(5)
#page
            # get the page source
            page_target.write(self.browser.page_source.encode('ascii','ignore'))
            page_target.close()

            self.get_top_ads(query_term)
            self.get_rhs_ads(query_term)
            self.get_bottom_ads(query_term)
            self.browser.close()
            #if query_term == 'vegas+hotels':
            #    break
        self.target.close()


    def get_top_ads(self, query_term):
            all_top_titles = self.browser.find_elements_by_xpath("//*[contains(@id,'vs0p')]")
            num_top_ads = len(all_top_titles)
            print num_top_ads
            for title in list(enumerate(all_top_titles, start=1)):
              print title[0]
              print title[1].text
              top_rank = title[0]
              top_title = title[1].text.encode('ascii','ignore')
        # get top ads domains
              all_top_domains = self.browser.find_element_by_xpath("//*[@id='tads']/ol/li[@class='ads-ad']["+str(top_rank)+"]/div/cite")
              top_domain = all_top_domains.text
        # get top ads line 1
              all_top_line1 = self.browser.find_element_by_xpath("//*[@id='tads']/ol/li[@class='ads-ad']["+str(top_rank)+"]/div[@class='ads-creative']")
              print all_top_line1.text.encode('ascii','ignore')
              top_line1 = all_top_line1.text.encode('ascii','ignore')
        # get top ads line 2
              try:
                all_top_line2 = self.browser.find_element_by_xpath("//div[@id='tads']/ol/li[@class='ads-ad']["+str(top_rank)+"]/div[@class='_knd _Tv']")
                print all_top_line2.text
                top_line2 = all_top_line2.text.encode('ascii','ignore')
              except:
                print "no top_line 2"
                top_line2 = ''
        # get top ads line 3
              try:
                all_top_line3 = self.browser.find_element_by_xpath("//div[@id='tads']/ol/li[@class='ads-ad']["+str(top_rank)+"]/div[@class='_ond' or @class='_end']")
                print all_top_line3.text
                top_line3 = all_top_line3.text.encode('ascii','ignore')
              except:
                print "no top_line 3"
                top_line3 = ''

              print "Appending to file..."
              result = "{}|T|{}|{}|{}|{}|{}|{}|{} - {} {} {}\n".format(query_term, top_rank, top_title, top_domain, top_line1,
                                                                 top_line2, top_line3, top_title, top_line1, top_line2,
                                                                 top_line3)
              self.target.write(result)
              #self.target.write(query_term+'|T|'+str(top_rank)+'|'+top_title+'|'+top_domain+'|'+top_line1+'|'+top_line2+'|'+top_line3+'|'+top_title+' - '+top_line1+' '+top_line2+' '+top_line3+'\n')

    def get_rhs_ads(self, query_term):
            all_rhs_titles = self.browser.find_elements_by_xpath("//*[contains(@id,'vs1p')]")
            num_rhs_ads = len(all_rhs_titles)
            print num_rhs_ads
            for title in list(enumerate(all_rhs_titles, start=1)):
              print title[0]
              print title[1].text
              rhs_rank = title[0]
              rhs_title = title[1].text.encode('ascii','ignore')

       # get right hand side ads domains
              all_rhs_domains = self.browser.find_element_by_xpath("//div[@id='mbEnd']/ol/li[@class='ads-ad']["+str(rhs_rank)+"]/div[@class='ads-visurl']/cite")
              print all_rhs_domains.text
              rhs_domain = all_rhs_domains.text
       # get right hand side ads lines
              all_rhs_lines = self.browser.find_element_by_xpath("//div[@id='mbEnd']/ol/li[@class='ads-ad']["+str(rhs_rank)+"]/div[@class='ads-creative']")
              blah = str(all_rhs_lines.get_attribute('innerHTML').encode('ascii','ignore'))
              blah2 = blah.replace('<b>','')
              blah3 = blah2.replace('</b>','')
              print blah3.split('<br>')[0]
              print blah3.split('<br>')[1]
              rhs_line1 = blah3.split('<br>')[0]
              rhs_line2 = blah3.split('<br>')[1]
              content = blah3.replace('<br>',' ')
              try:
                print blah3.split('<br>')[2]
                rhs_line3 = blah3.split('<br>')[2]
              except IndexError:
                print 'IndexError'
                rhs_line3 = ''


              print "Appending to file..."
              #target.write('Houston+Hotels| R|'+str(rank)+'| '+rhs_title+'| '+rhs_domain+'| '+rhs_line1+'| '+rhs_line2+'| '+rhs_line3+'| '+rhs_title+' - '+content+'\n')
              result = "{}|R|{}|{}|{}|{}|{}|{}|{} - {}\n".format(query_term, rhs_rank, rhs_title, rhs_domain, rhs_line1,
                                                                 rhs_line2, rhs_line3, rhs_title, content)
              self.target.write(result)

#bottom
    def get_bottom_ads(self, query_term):
        # get bottom titles
            all_bottom_titles = self.browser.find_elements_by_xpath("//*[contains(@id,'vs3p')]")
            num_bottom_ads = len(all_bottom_titles)
            print num_bottom_ads
            for title in list(enumerate(all_bottom_titles, start=1)):
              print title[0]
              print title[1].text
              bottom_rank = title[0]
              bottom_title = title[1].text.encode('ascii','ignore')

        # get bottom ads domains
              all_bottom_domains = self.browser.find_element_by_xpath("//*[@id='tadsb']/ol/li[@class='ads-ad']["+str(bottom_rank)+"]/div[@class='ads-visurl']/cite")
              print all_bottom_domains.text
              bottom_domain = all_bottom_domains.text
        # get bottom ads line 1
              all_bottom_line1 = self.browser.find_element_by_xpath("//*[@id='tadsb']/ol/li[@class='ads-ad']["+str(bottom_rank)+"]/div[@class='ads-creative']")
              print all_bottom_line1.text.encode('ascii','ignore')
              bottom_line1 = all_bottom_line1.text.encode('ascii','ignore')

        # get bottom ads line 2
              try:
                all_bottom_line2 = self.browser.find_element_by_xpath("//div[@id='tadsb']/ol/li[@class='ads-ad']["+str(bottom_rank)+"]/div[@class='_knd _Tv']")
                print all_bottom_line2.text
                bottom_line2 = all_bottom_line2.text.encode('ascii','ignore')
              except:
                print "no bottom_line 2"
                bottom_line2 = ''

        # get bottom ads line 3
              try:
                all_bottom_line3 = self.browser.find_element_by_xpath("//div[@id='tadsb']/ol/li[@class='ads-ad']["+str(bottom_rank)+"]/div[@class='_ond' or @class='_end']")
                print all_bottom_line3.text
                bottom_line3 = all_bottom_line3.text.encode('ascii','ignore')
              except:
                print "no bottom_line 3"
                bottom_line3 = ''

              print "Appending to file..."
              #target.write('Houston+Hotels| B|'+str(bottom_rank)+'| '+bottom_title+'| '+bottom_domain+'| '+bottom_line1+'| '+bottom_line2+'| '+bottom_line3+'| '+bottom_title+' - '+bottom_line1+' '+bottom_line2+' '+bottom_line3+'\n')
              result = "{}|B|{}|{}|{}|{}|{}|{}|{} - {} {} {}\n".format(query_term, bottom_rank, bottom_title, bottom_domain, bottom_line1,
                                                                 bottom_line2, bottom_line3, bottom_title, bottom_line1, bottom_line2, bottom_line3)
              self.target.write(result)


myClassObject = GetAdsList()

myClassObject.getAds()
