import universe_api
country_list = []
total_universities_from_db = universe_api.get_university_from_db()

def test_count_matching_univiersities_by_country():
    country_list = ['Israel', 'United States']
    for country in country_list:
        total_universities_from_api = len(universe_api.get_universities_by_country(country)[0])
        db_count_filtered_univiersities = len(list(filter(lambda item: item['country'] == country ,total_universities_from_db)))
        assert total_universities_from_api == db_count_filtered_univiersities, f"Exepcted {db_count_filtered_univiersities} matching univiersites for country - {country}"
               
def test_validate_status_code():
    country_list = ['Israel', 'United States', 'Thailand']
    for country in country_list:
        status_code = universe_api.get_universities_by_country(country)[1]
        assert status_code == 200, f"Exepcted status code to be 200 for country {country}"
        
def test_verify_no_missing_fields():
    fields = ['country', 'id', 'name']
    for field in fields:
        expected_missing_fields_count = len(list(filter(lambda item: field not in item ,total_universities_from_db)))
        assert expected_missing_fields_count == 0, f"Found missing field - {field}"