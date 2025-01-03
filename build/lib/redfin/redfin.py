import requests
import json

class Redfin:
    def __init__(self):
        self.base = 'https://www.redfin.com/stingray/'
        self.user_agent_header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'RF_BROWSER_ID=uzwwbkwfSheVvmPLwRE93A; RF_BROWSER_ID_GREAT_FIRST_VISIT_TIMESTAMP=2025-01-02T10%3A22%3A21.832022; RF_BID_UPDATED=1; __pdst=18411f2e4cf141328e35d0536694d40f; _scor_uid=355606d5ddc64225b3e1831818c7e0dc; _fbp=fb.1.1735842180221.964833610527593196; _tt_enable_cookie=1; _ttp=plsXtnNpNgv6xz9yWSN219Ed8I_.tt.1; _gcl_au=1.1.1321230548.1735842181; _gid=GA1.2.218242723.1735842181; RF_LAST_NAV=1; unifiedLastSearch=name%3D5955%2520Pauley%2520Swamp%2520Rd%26subName%3DConway%252C%2520SC%252C%2520USA%26url%3D%252FSC%252FConway%252F5955-Pauley-Swamp-Rd-29527%252Fhome%252F170807295%26id%3D1_170807295%26type%3D1%26unifiedSearchType%3D1%26isSavedSearch%3D%26countryCode%3DUS; RF_VISITED=true; RF_MARKET=south-carolina; RF_BUSINESS_MARKET=39; ki_t=1735842374630%3B1735842374630%3B1735842374630%3B1%3B1; ki_r=; cw-test-20241121-intersection-observer=test; _sharedid=8d048da1-ddf5-4f44-b24a-ec8c6a53b719; pbjs_fabrickId=%7B%22fabrickId%22%3A%22E1%3AXCK9ZifIJ3AD0afqDAnPXqLp0Vx-o0Mvd7yitescsCYl50aRiC09DSGvI-QQdguyTAcy7Ry4VWqtv62TPIp9TVCTiAfYGT5AOwWhbRvBy_A%22%7D; RF_LISTING_VIEWS=167042323; RF_LAST_DP_SERVICE_REGION=3093; __gads=ID=8be215e276d6d833:T=1735842378:RT=1735846452:S=ALNI_MY95bwnKdkEK83Sd-fKR26MDdcxtg; __gpi=UID=00000fb41145f99d:T=1735842378:RT=1735846452:S=ALNI_MaDQZXOZw1xNdDuk00RJOcx7B-dgg; __eoi=ID=fe2da4b77afadcfe:T=1735842378:RT=1735846452:S=AA-AfjZn2SiQWm68MC3px00nBpNt; _sharedid_cst=zix7LPQsHA%3D%3D; pbjs_fabrickId_cst=zix7LPQsHA%3D%3D; cto_bundle=KY7oiV9tbVlYVklDQTVNQUE3MWFKYmlIV0tjbyUyQmFlekdaNktNYTdRdEo3UTJ1bVNUeFBIYzR1dUtqVk1RMmRlTXElMkZITlZvS1o3WkplaTZpT2xRVWdiRCUyQllzTHV1TlZHNmNjcnVVc2w2Vlg2QUt2Unh5elFhYzZxUGd6UjdMV01VMnMlMkZUQ010QVJoT2d1QXN2MVJZdWJJYzZLWnJsTU9VbWVYSU5QWDFTb2MyenEwQmpTUWcyT1NnYlJwcGJJUFdSMjZlbA; cto_bidid=V7Pq-V8yaCUyQklURkJNUFIwM3VQJTJCS0pZJTJCdzJjeXZYJTJGYnNOMTVJa2gwRkhrOFJld0pNQW44dXI2elN3VmRubnVVJTJGSEFBJTJCQ2QwTmd4b0UyZmxXUUJPZXdLSjVZa3ZwVW1zYW4xSiUyQml5amRTRXFaTEclMkZHVHNwQThQTE9XaFdzSiUyRng3UHpwTEJwemdCYiUyQlpuYnRheDFuT3JUWUE4dyUzRCUzRA; AMP_TOKEN=%24NOT_FOUND; RF_TRAFFIC_SEGMENT=non-organic; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jan+03+2025+16%3A03%3A35+GMT-0300+(Brasilia+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=e8de32d0-4cdb-4d52-95a6-9983f962efc2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=BR%3BSP; OptanonAlertBoxClosed=2025-01-03T19:03:35.149Z; _dc_gtm_UA-294985-1=1; _ga_928P0PZ00X=GS1.1.1735931015.5.0.1735931015.60.0.0; _uetsid=98edac60c93611efa1a08ba4333c111a; _uetvid=98edaf80c93611ef87c3df012f13fc48; FEED_COUNT=%5B%22%22%2C%22f%22%5D; audS=t; RF_CORVAIR_LAST_VERSION=556.2.0; aws-waf-token=262801bb-5485-47de-9565-d6f2297b44ad:EAoAsnuFJ+ZGAAAA:ffpFvHRhrw3ikqOZnHZzWW/YaBJs/4AdAD12Vcqedbo9zAzI9W2+TfeDo+9w/qXwqdQlFKy9rFmd1PQKr+pkSRQ5tgmJRIE0o5BTsDXZtDTTnmrd0EWDDapdF/83xjyIFi9neyDEQUOgCWykWnR4+SfXWiAptr78JOGJhmkqkkyhFzkywes/HW1utTDnG+y8CmDuml33oLxAWIKfDgJWr5biPsJG+4hyuxGu+PkIA52NnBrw8cctA3hNLOGJZiSGzQ==; _ga=GA1.2.2042146238.1735842181; RF_BROWSER_CAPABILITIES=%7B%22screen-size%22%3A2%2C%22events-touch%22%3Afalse%2C%22ios-app-store%22%3Afalse%2C%22google-play-store%22%3Afalse%2C%22ios-web-view%22%3Afalse%2C%22android-web-view%22%3Afalse%7D; _dd_s=rum=0&expire=1735931932200',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }

    def meta_property(self, url, kwargs, page=False):
        if page:
            kwargs['pageType'] = 3
        return self.meta_request('api/home/details/' + url, {
            'accessLevel': 1,
            **kwargs
        })

    def meta_request(self, url, kwargs):
        response = requests.get(self.base + url, params=kwargs, headers=self.user_agent_header)
        response.raise_for_status()
        return json.loads(response.text[4:])

    def initial_info(self, url, **kwargs):
        return self.meta_request('api/home/details/initialInfo', {'path': url, **kwargs})

    def page_tags(self, url, **kwargs):
        return self.meta_request('api/home/details/v1/pagetagsinfo', {'path': url, **kwargs})

    def primary_region(self, url, **kwargs):
        return self.meta_request('api/home/details/primaryRegionInfo', {'path': url, **kwargs})

    def search(self, query, **kwargs):
        return self.meta_request('do/location-autocomplete', {'location': query, 'v': 2, **kwargs})

    def below_the_fold(self, property_id, **kwargs):
        return self.meta_property('belowTheFold', {'propertyId': property_id, **kwargs}, page=True)

    def hood_photos(self, property_id, **kwargs):
        return self.meta_request('api/home/details/hood-photos', {'propertyId': property_id, **kwargs})

    def more_resources(self, property_id, **kwargs):
        return self.meta_request('api/home/details/moreResourcesInfo', {'propertyId': property_id, **kwargs})

    def page_header(self, property_id, **kwargs):
        return self.meta_request('api/home/details/homeDetailsPageHeaderInfo', {'propertyId': property_id, **kwargs})

    def property_comments(self, property_id, **kwargs):
        return self.meta_request('api/v1/home/details/propertyCommentsInfo', {'propertyId': property_id, **kwargs})

    def building_details_page(self, property_id, **kwargs):
        return self.meta_request('api/building/details-page/v1', {'propertyId': property_id, **kwargs})

    def owner_estimate(self, property_id, **kwargs):
        return self.meta_request('api/home/details/owner-estimate', {'propertyId': property_id, **kwargs})

    def claimed_home_seller_data(self, property_id, **kwargs):
        return self.meta_request('api/home/details/claimedHomeSellerData', {'propertyId': property_id, **kwargs})

    def cost_of_home_ownership(self, property_id, **kwargs):
        return self.meta_request('do/api/costOfHomeOwnershipDetails', {'propertyId': property_id, **kwargs})

    def floor_plans(self, listing_id, **kwargs):
        return self.meta_request('api/home/details/listing/floorplans', {'listingId': listing_id, **kwargs})

    def tour_list_date_picker(self, listing_id, **kwargs):
        return self.meta_request('do/tourlist/getDatePickerData', {'listingId': listing_id, **kwargs})

    def shared_region(self, table_id, **kwargs):
        return self.meta_request('api/region/shared-region-info', {'tableId': table_id, 'regionTypeId': 2, 'mapPageTypeId': 1, **kwargs})

    def similar_listings(self, property_id, listing_id, **kwargs):
        return self.meta_property('similars/listings', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def similar_sold(self, property_id, listing_id, **kwargs):
        return self.meta_property('similars/solds', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def nearby_homes(self, property_id, listing_id, **kwargs):
        return self.meta_property('nearbyhomes', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def above_the_fold(self, property_id, listing_id, **kwargs):
        return self.meta_property('aboveTheFold', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def property_parcel(self, property_id, listing_id, **kwargs):
        return self.meta_property('propertyParcelInfo', {'propertyId': property_id, 'listingId': listing_id, **kwargs}, page=True)

    def activity(self, property_id, listing_id, **kwargs):
        return self.meta_property('activityInfo', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def customer_conversion_info_off_market(self, property_id, listing_id, **kwargs):
        return self.meta_property('customerConversionInfo/offMarket', {'propertyId': property_id, 'listingId': listing_id, **kwargs}, page=True)

    def rental_estimate(self, property_id, listing_id, **kwargs):
        return self.meta_property('rental-estimate', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def avm_historical(self, property_id, listing_id, **kwargs):
        return self.meta_property('avmHistoricalData', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def info_panel(self, property_id, listing_id, **kwargs):
        return self.meta_property('mainHouseInfoPanelInfo', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def descriptive_paragraph(self, property_id, listing_id, **kwargs):
        return self.meta_property('descriptiveParagraph', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def avm_details(self, property_id, listing_id, **kwargs):
        return self.meta_property('avm', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def tour_insights(self, property_id, listing_id, **kwargs):
        return self.meta_property('tourInsights', {'propertyId': property_id, 'listingId': listing_id, **kwargs}, page=True)

    def stats(self, property_id, listing_id, region_id, **kwargs):
        return self.meta_property('stats', {'regionId': region_id, 'propertyId': property_id, 'listingId': listing_id, 'regionTypeId': 2, **kwargs})
