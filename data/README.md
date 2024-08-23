# Data Dictionary

AirBnB data from [Kaggle](https://www.kaggle.com/datasets/airbnb/seattle).


## Calendar

| field | type | description |
| ----- | ----------- | -------------- |
| listing_id | int | foerign key back to the listing file |
| date | date | format is YYYY-MM-DD |
| available | boolan | t = True or f = False |
| price | string | with "$" and a float with 2 decimal places |


## Reviews

| field | type | description |
| ----- | ----------- | -------------- |
| listing_id | int | foreign key to listings |
| id | int | unique idenfitier for reviews |
| date | date | date of the review |
| reviewer_id | int | foreign key to reviewers |
| reviewer_name | str | name of the person submitting the review |
| comments | str | comments submitted with the review |


## Listings

| field | type | description |
| ----- | ----------- | -------------- |
| id | int |  |
| listing_url | str |  |
| scrape_id | int |  |
| last_scraped | date |  |
| name | str | property name |
| summary | str | property summary |
| space | str | property space description |
| description | str | property description |
| experiences_offered | str | "none" for every record |
| neighborhood_overview | str | neighborhood description |
| notes | str | additional property notes |
| transit | str | description of transit options |
| thumbnail_url | str | image url |
| medium_url | str | image url |
| picture_url | str | image url |
| xl_picture_url | str | image url |
| host_id | int | unique identifier for host |
| host_url | str | airbnb user page for host |
| host_name | str | name of host |
| host_since | date | date host started |
| host_location | str | city / state |
| host_about | str | host description |
| host_response_time | str | "about an hour", "within a few hours", etc. |
| host_response_rate | str | percentage of messages responded to |
| host_acceptance_rate | str | percentage of bookings accepted |
| host_is_superhost | boolean | t = True, f = False |
| host_thumbnail_url | str | image url  |
| host_picture_url | str | image url |
| host_neighbourhood | str | neighborhood of the host |
| host_listings_count | int | number of listings |
| host_total_listings_count | int | number of listings |
| host_verifications | str | list of ways host has been verified. example: "['email', 'phone', 'facebook', 'linkedin', 'reviews', 'jumio']" |
| host_has_profile_pic | boolean | t = True, f = False |
| host_identity_verified | boolean | t = True, f = False |
| street | str | porperty street |
| neighbourhood | str | property neighborhood |
| neighbourhood_cleansed |str  | property neighborhood |
| neighbourhood_group_cleansed | str | property neighborhood |
| city |str  | property city |
| state |str  | propoerty state |
| zipcode | int | property zip |
| market | str | property market |
| smart_location | str | property location |
| country_code | str | property country |
| country | str | property country |
| latitude | float | property latitude |
| longitude | float | property longitude |
| is_location_exact | boolean | t = True, f = False |
| property_type | str | type of property. example: Apartment, Home, etc. |
| room_type | str | type of room. exmpale: Entire Home, Private Room, etc. |
| accommodates | int | number of guests allowed |
| bathrooms | float | number of bathrooms available |
| bedrooms | int | number of bedrooms available |
| beds | int | number of beds available |
| bed_type | str | type of bed. example: Real Bed, Futon, etc. |
| amenities | str | dictionary of amenities available. example: {TV,"Cable TV",Internet,"Wireless Internet","Air Conditioning",Kitchen,Heating,"Family/Kid Friendly",Washer,Dryer} |
| square_feet | int | square footage of property |
| price | str | nightly rate. format includes "$" and float with 2 decimal places. |
| weekly_price | str | weekly rate. format includes "$" and float with 2 decimal places. |
| monthly_price | str | monthly rate. format includes "$" and float with 2 decimal places. |
| security_deposit | str | deposit amount. format includes "$" and float with 2 decimal places. |
| cleaning_fee | str | cleaning fee. format includes "$" and float with 2 decimal places. |
| guests_included | int | number of guests allowed |
| extra_people | str | nightly rate for extra guests. format includes "$" and float with 2 decimal places. |
| minimum_nights | int | minimum number of nights required for a booking |
| maximum_nights | int | maximum number of nights allowed for a booking |
| calendar_updated | str | last time the calendar was updated. example: today, 4 weeks ago, etc. |
| has_availability | boolean | available nights in the next year |
| availability_30 | int | number of nights available in next 30 days |
| availability_60 | int | number of nights available in next 60 days |
| availability_90 | int | number of nights available in next 90 days |
| availability_365 | int | number of nights available in next 365 days |
| calendar_last_scraped | date | date the calendar was last updated |
| number_of_reviews | int | number of reviews |
| first_review | date | date of first review |
| last_review | date | date of last review |
| review_scores_rating | int | rating (0-100) |
| review_scores_accuracy | int | rating (0-10) |
| review_scores_cleanliness | int | rating (0-10) |
| review_scores_checkin | int | rating (0-10) |
| review_scores_communication | int | rating (0-10) |
| review_scores_location | int | rating (0-10) |
| review_scores_value | int | rating (0-10) |
| requires_license | boolean | t = True, f = False |
| license | str | all records blank |
| jurisdiction_names | str | all records "WASHINGTON" |
| instant_bookable | boolean | t = True, f = False |
| cancellation_policy | str | strictness of cancellation policy. example: moderate, strict, etc. |
| require_guest_profile_picture | boolean | t = True, f = False |
| require_guest_phone_verification | boolean | t = True, f = False |
| calculated_host_listings_count | int | number of listings for this host  |
| reviews_per_month | float | number of reivews per month |

