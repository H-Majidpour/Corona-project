import scrapy 
import pickle


class mySpider(scrapy.Spider):
    name = 'coronaCrawler'

    def start_requests(self):
        page_url = ["https://www.worldometers.info/coronavirus/"]

        for url in page_url:
            yield scrapy.Request(url = url, callback = self.parse)


    def parse(self, response):
        tmp_list = response.xpath("//div[@class = 'maincounter-number' ]/span/text()").extract()
        Coronavirus_Cases = tmp_list[0]
        Deaths = tmp_list[1]
        Recovered = tmp_list[2]

        Table_info = []

        Country = []
        number_of_country = len(response.xpath("//tbody/tr/td[1]/text()").extract())
        for i in range(0, number_of_country):
            # Statistics of 100 countries involved in Corona
            this_country = response.xpath("//tbody/tr["+ str(i) +"]/td[2]/span/text()").extract()
            this_country += (response.xpath("//tbody/tr["+ str(i) +"]/td[2]/a/text()").extract()[:108])
            self.delete_key(this_country, " ")
            
            if this_country == []:
                this_country.append("")

            Country.append(this_country[0])
            self.delete_key(Country, "")

        Total_Cases = response.xpath('//tbody/tr/td[3]/text()').extract()[8:108]
        New_cases = response.xpath('//tbody/tr/td[4]/text()').extract()[8:]
        New_Deaths = response.xpath('//tbody/tr/td[5]/text()').extract()[8:108]
        Total_Recovered = response.xpath('//tbody/tr/td[6]/text()').extract()[8:108]
        New_Recovered = response.xpath('//tbody/tr/td[7]/text()').extract()[8:108]
        Active_cases = response.xpath('//tbody/tr/td[8]/text()').extract()[8:108]
        

        Table_info.append(Country)
        Table_info.append(Total_Cases)
        Table_info.append(New_cases)
        Table_info.append(New_Deaths)
        Table_info.append(Total_Recovered)
        Table_info.append(New_Recovered)
        Table_info.append(Active_cases)



        with open("statics/DB/data.dat", 'wb') as Fin:
            pickle.dump(Coronavirus_Cases, Fin)
            pickle.dump(Deaths, Fin)
            pickle.dump(Recovered, Fin)
            pickle.dump(Table_info, Fin)

            Fin.close()
            
                






    def delete_key(self, mylist, key):
        if key in mylist:
            mylist.remove(key)

        return (mylist)
