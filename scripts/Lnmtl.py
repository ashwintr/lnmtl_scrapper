import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'ww_spider'
    start_urls = ['https://lnmtl.com/chapter/transcending-the-nine-heavens-chapter-1140']

    def parse(self, response):
        SET_SELECTOR = '#chapter-container'
        for brickset in response.css(SET_SELECTOR):

            title_SELECTOR = 'h3 span ::text'
            CONTENT_SELECTOR = '.translated ::text'
        #     MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
        #     IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'title': brickset.css(title_SELECTOR).extract_first(),
                'content': brickset.css(CONTENT_SELECTOR).extract(),
        #         'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
        #         'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }
        #
        # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #     )
