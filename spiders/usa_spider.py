import scrapy
from uni_scraper.items import UniversityItem
from uni_scraper.utils import find_emails, clean_emails, extract_domain

class USASpider(scrapy.Spider):
    name = "usa_universities"

    def start_requests(self):
        url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=DEMO_KEY&per_page=50"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        data = response.json()

        for school in data.get("results", []):
            item = UniversityItem()
            item["name"] = school.get("school.name")
            item["website"] = school.get("school.school_url")
            item["country"] = "USA"

            if item["website"]:
                url = "http://" + item["website"]
                yield scrapy.Request(
                    url,
                    callback=self.parse_website,
                    meta={"item": item}
                )
            else:
                yield item

    def parse_website(self, response):
        item = response.meta["item"]
        domain = extract_domain(response.url)

        emails = find_emails(response.text)
        emails = clean_emails(emails, domain)

        if emails:
            item["email"] = emails
            yield item
        else:
            # try contact pages
            links = response.css("a::attr(href)").getall()

            for link in links:
                if any(x in link.lower() for x in ["contact", "about"]):
                    yield response.follow(
                        link,
                        callback=self.parse_contact,
                        meta={"item": item}
                    )

    def parse_contact(self, response):
        item = response.meta["item"]
        domain = extract_domain(response.url)

        emails = find_emails(response.text)
        emails = clean_emails(emails, domain)

        item["email"] = emails if emails else None
        yield item
