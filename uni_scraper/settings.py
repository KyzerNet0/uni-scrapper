BOT_NAME = "uni_scraper"

SPIDER_MODULES = ["uni_scraper.spiders"]
NEWSPIDER_MODULE = "uni_scraper.spiders"

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2
AUTOTHROTTLE_ENABLED = True

USER_AGENT = "Mozilla/5.0"

ITEM_PIPELINES = {
    "uni_scraper.pipelines.CleanPipeline": 300,
}

FEEDS = {
    "universities.csv": {
        "format": "csv",
        "encoding": "utf-8",
        "fields": ["name", "website", "email", "country"],
    }
}
