import requests
import json
import os

class Redfin:
    def __init__(self, cookie_file_path):
        """
        Initializes the Redfin client.

        :param cookie_file_path: Path to the JSON file where cookies are stored.
        """
        self.base = 'https://www.redfin.com/stingray/'
        self.session = requests.Session()
        self.session.headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
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
        })
        self.cookie_file_path = cookie_file_path
        self.load_cookies()

    def load_cookies(self):
        """
        Loads cookies from the specified JSON file into the session.
        If the file does not exist or is invalid, refreshes cookies.
        """
        if os.path.exists(self.cookie_file_path):
            try:
                with open(self.cookie_file_path, 'r') as f:
                    cookies = json.load(f)
                self.session.cookies.update(cookies)
                print("Loaded cookies from storage.")
            except Exception as e:
                print(f"Failed to load cookies from {self.cookie_file_path}: {e}")
                self.refresh_cookies()
        else:
            print("Cookie file not found. Refreshing cookies...")
            self.refresh_cookies()

    def save_cookies(self):
        """
        Saves the current session's cookies to the specified JSON file.
        """
        try:
            with open(self.cookie_file_path, 'w') as f:
                json.dump(self.session.cookies.get_dict(), f)
            print(f"Cookies saved to {self.cookie_file_path}.")
        except Exception as e:
            print(f"Failed to save cookies to {self.cookie_file_path}: {e}")

    def refresh_cookies(self):
        """
        Performs an initial request to obtain fresh cookies and saves them.
        """
        print("Refreshing cookies...")
        try:
            response = self.session.get('https://www.redfin.com/')
            response.raise_for_status()
            self.save_cookies()
            print("Cookies refreshed successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to refresh cookies: {e}")
            raise

    def meta_property(self, url, kwargs, page=False):
        if page:
            kwargs['pageType'] = 3
        return self.meta_request('api/home/details/' + url, {
            'accessLevel': 1,
            **kwargs
        })

    def meta_request(self, url, kwargs):
        """
        Makes a GET request to the specified Redfin API endpoint with provided parameters.
        If a 401 Unauthorized error is encountered, refreshes cookies and retries once.

        :param url: API endpoint URL (relative to base).
        :param kwargs: Dictionary of query parameters.
        :return: Parsed JSON response.
        """
        try:
            response = self.session.get(self.base + url, params=kwargs)
            response.raise_for_status()
            return json.loads(response.text[4:])
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                print("Unauthorized access detected. Refreshing cookies and retrying...")
                self.refresh_cookies()
                try:
                    response = self.session.get(self.base + url, params=kwargs)
                    response.raise_for_status()
                    return json.loads(response.text[4:])
                except requests.exceptions.HTTPError as retry_e:
                    print(f"Retry failed: {retry_e}")
                    raise
            else:
                print(f"HTTP error occurred: {e}")
                raise
        except requests.exceptions.RequestException as req_e:
            print(f"Request exception: {req_e}")
            raise
        except json.JSONDecodeError as json_e:
            print(f"Failed to parse JSON response: {json_e}")
            raise

    # ... (rest of your methods remain unchanged)

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
