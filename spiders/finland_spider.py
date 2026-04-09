import scrapy
from uni_scraper.items import UniversityItem
from uni_scraper.utils import find_emails, clean_emails, extract_domain

class FinlandSpider(scrapy.Spider):
    name = "finland_universities"
    start_urls = ["https://www.studyinfinland.fi/universities"]

    def parse(self, response):
        for link in response.css("a::attr(href)").getall():
            if "http" in link:
                yield response.follow(link, self.parse_uni)

    def parse_uni(self, response):
        item = UniversityItem()
        item["name"] = response.css("h1::text").get()
        item["website"] = response.url
        item["country"] = "Finland"

        yield self.extract_email(response, item)

    def extract_email(self, response, item):
        domain = extract_domain(response.url)

        emails = find_emails(response.text)
        emails = clean_emails(emails, domain)

        item["email"] = emails if emails else None
        yield item
