import re
import selenium
from selenium import webdriver
import time

class GetAdsList(object):
    def getAds(self):
        print "Opening hotel words file"
        hotel_words = open('hotel_keywords.txt', 'r')
        for line in hotel_words:
            print line
            query_term = line.replace(' ','+')
            query_term = query_term.replace('\n','')
            print query_term
            print "Opening the write file..."
            filename = query_term+'.html'
            page_target = open(filename, 'w+')
            print "working"
            browser = webdriver.Firefox()
            browser.get('https://www.google.com/#q='+query_term)
            time.sleep(5)
#page
            # get the page source
            page_target.write(browser.page_source.encode('ascii','ignore'))
            page_target.close()
            #target.close()

# #rhs
        # get right hand side ads titles
        all_rhs_titles = browser.find_elements_by_xpath("//*[contains(@id,'vs1p')]")
        num_rhs_ads = len(all_rhs_titles)
        print num_rhs_ads
        for title in list(enumerate(all_rhs_titles, start=1)):
            print title[0]
            print title[1].text
            rank = title[0]
            rhs_title = title[1].text.encode('ascii','ignore')

        # get right hand side ads domains
            all_rhs_domains = browser.find_element_by_xpath("//div[@id='mbEnd']/ol/li[@class='ads-ad']["+str(rank)+"]/div[@class='ads-visurl']/cite")
            #for domain in all_rhs_domains:
            print all_rhs_domains.text
            rhs_domain = all_rhs_domains.text
        # get right hand side ads lines
            all_rhs_lines = browser.find_element_by_xpath("//div[@id='mbEnd']/ol/li[@class='ads-ad']["+str(rank)+"]/div[@class='ads-creative']")
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
            target.write('Houston+Hotels| R|'+str(rank)+'| '+rhs_title+'| '+rhs_domain+'| '+rhs_line1+'| '+rhs_line2+'| '+rhs_line3+'| '+rhs_title+' - '+content+'\n')

#top

        # get top ads titles
        all_top_titles = browser.find_elements_by_xpath("//*[contains(@id,'vs0p')]")
        num_top_ads = len(all_top_titles)
        print num_top_ads
        for title in all_top_titles:
            print title.text
        # get top ads domains
        all_top_domains = browser.find_elements_by_xpath("//*[@id='tads']/ol/li/div/cite")
        for domain in all_top_domains:
            print domain.text
        # get top ads line 1
        all_top_line1 = browser.find_elements_by_xpath("//*[@id='tads']/ol/li/div[@class='ads-creative']")
        for line in all_top_line1:
            print line.text
        # get top ads line 2
        all_top_line2 = browser.find_elements_by_xpath("//*[@id='tads']/ol/li/div[@class='_knd _Tv']")
        for line in all_top_line2:
            print line.text

#bottom
        # get bottom titles
        # all_bottom_titles = browser.find_elements_by_xpath("//*[contains(@id,'vs3p')]")
        # num_bottom_ads = len(all_bottom_titles)
        # print num_bottom_ads
        # for title in list(enumerate(all_bottom_titles, start=1)):
        #     print title[0]
        #     print title[1].text
        #     bottom_rank = title[0]
        #     bottom_title = title[1].text.encode('ascii','ignore')
        #
        # # get bottom ads domains
        #     all_bottom_domains = browser.find_element_by_xpath("//*[@id='tadsb']/ol/li[@class='ads-ad']["+str(bottom_rank)+"]/div[@class='ads-visurl']/cite")
        #     print all_bottom_domains.text
        #     bottom_domain = all_bottom_domains.text
        # # get bottom ads line 1
        #     all_bottom_line1 = browser.find_element_by_xpath("//*[@id='tadsb']/ol/li[@class='ads-ad']["+str(bottom_rank)+"]/div[@class='ads-creative']")
        #     print all_bottom_line1.text.encode('ascii','ignore')
        #     bottom_line1 = all_bottom_line1.text.encode('ascii','ignore')
        #
        # # get bottom ads line 2
        #     try:
        #       all_bottom_line2 = browser.find_element_by_xpath("//div[@id='tadsb']/ol/li[@class='ads-ad']["+str(bottom_rank)+"]/div[@class='_knd _Tv']")
        #       print all_bottom_line2.text
        #       bottom_line2 = all_bottom_line2.text.encode('ascii','ignore')
        #     except:
        #       print "no bottom_line 2"
        #       bottom_line2 = ''
        #
        # # get bottom ads line 3
        #     try:
        #       all_bottom_line3 = browser.find_element_by_xpath("//div[@id='tadsb']/ol/li[@class='ads-ad']["+str(bottom_rank)+"]/div[@class='_ond' or @class='_end']")
        #       print all_bottom_line3.text
        #       bottom_line3 = all_bottom_line3.text.encode('ascii','ignore')
        #     except:
        #       print "no bottom_line 3"
        #       bottom_line3 = ''
        #
        #     print "Appending to file..."
        #     target.write('Houston+Hotels| B|'+str(bottom_rank)+'| '+bottom_title+'| '+bottom_domain+'| '+bottom_line1+'| '+bottom_line2+'| '+bottom_line3+'| '+bottom_title+' - '+bottom_line1+' '+bottom_line2+' '+bottom_line3+'\n')
              browser.close()
            if query_term == 'cheapest+hotel+rates':
                break

myClassObject = GetAdsList()

myClassObject.getAds()
