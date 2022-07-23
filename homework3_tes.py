import HW3
import pytest
import logging


@pytest.fixture
def data_set():
    data_set = {
        1: {"name": "adham", "height": 1.58, "sex": "male", "age": 22},
        2: {"sex": "female", "age": 57, "height": 1.58, "name": "amal"},
        3: {"sex": "male", "age": 64, "height": 1.80, "name": "emad"},
        4: {"sex": "female", "age": 29, "height": 1.55, "name": "tamar"},
        5: {"sex": "female", "age": 20, "height": 1.65, "name": "rima"}
    }
    print("********")
    yield data_set
    print("\n--------")


@pytest.mark.smoke
def test_split_male_female(data_set):
    logging.info("Accepts data_set as a parameter and returns 2 dictionaries")
    dict_female, dict_male = HW3.split_male_female(data_set)
    for x, y in data_set.items():
        if y.get("sex") == "female":
            assert x in dict_female
        if y.get("sex") == "male":
            assert x in dict_male


@pytest.mark.regression
def test_find_median_average(data_set):
    logging.info("average age and median age of the resulting dictionary")
    average_age, median_age = HW3.find_median_average(data_set)
    assert average_age == 38.4
    assert median_age == 29


