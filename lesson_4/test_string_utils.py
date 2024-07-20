import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()
#capitalize
def test_capitalize(utils):
    assert utils.capitalize("dima") == "Dima"
    assert utils.capitalize("Dima") == "Dima"
    assert utils.capitalize("hello summer")== "Hello summer"
    """negativ test_capitaliz  """
    assert utils.capitalize("") == ""
    assert utils.capitalize("6789test")
#trim
def test_trim(utils):
    assert utils.trim(" summer") == "summer"
    assert utils.trim(" Hello summer ") == "Hello summer "
    """negativ test trim  """
    assert utils.trim("") == ""
    assert utils.trim("    ") == ""
    #test_to_list
def test_to_list(utils):
    assert utils.to_list("D,O,H") == ["D", "O", "H" ]
    assert utils.to_list("8:5:3", ":") == ["8", "5", "3"]
    """negativ test_to_list """
    assert utils.to_list("", ",") == []
    assert utils.to_list("DOH", ",") == ["DOH"]
    assert utils.to_list(":8:5:3:", ":") == ['', '8', '5', '3', '']
    #test_contains
def test_contains(utils):
     assert utils.contains("holidays", "h") == True
     assert utils.contains("holidays", "a") == True
     assert utils.contains("holidays","e") == False

#test_delete_symbol
def test_delete_symbol(utils):
    assert utils.delete_symbol("the sun", "t") == "he sun"
    assert utils.delete_symbol("the sun", "sun") == "the "
    assert utils.delete_symbol("the sun", "he ") == "tsun"
    assert utils.delete_symbol("the sun", "x") == "the sun"
    """negativ test_delete_symbol"""
    assert utils.delete_symbol("the sun", "moon") == "the sun" 
    # test_starts_with
def test_starts_with(utils):
     assert utils.starts_with("grass", "g") == True
     assert utils.starts_with("grass", "s") == False
     assert utils.starts_with("grass", "grass") == True
     """negativ test_starts_with"""
     assert utils.starts_with("grass", "green") == False
#test_ends_with
def test_ends_with(utils):
     assert utils.ends_with("собака", "а") == True
     assert utils.ends_with("собака", "ка") == True
     assert utils.ends_with("собака","собака") == True
     """negativ test_ends_with"""
     assert not utils.ends_with("", "a")
     #test_is_empty
def test_is_empty(utils):
    assert utils.is_empty("") == True
    assert utils.is_empty("skypro") == False
    """negativtest_is_empty  """
    assert utils.is_empty("//n") == False
    #test_list_to_string
def test_list_to_string(utils):
    assert utils.list_to_string([5, 6, 9, 48]) == "5, 6, 9, 48"
    assert utils.list_to_string(["sky", "pro"]) == "sky, pro"
    assert utils.list_to_string(["sky", "pro"], "-") == "sky-pro"
    assert utils.list_to_string([]) == ""
    assert utils.list_to_string(["single"]) == "single"



