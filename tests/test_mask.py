from copy import deepcopy

from mask.helper import (
    DATA_TO_MASK,
    MASKED_DATA_WITH_INNER_DICT,
    MASKED_DATA_WITH_INNER_LIST,
    MASKED_TEST_DICT,
    TEST_DATA_WITH_INNER_DICT,
    TEST_DATA_WITH_INNER_LIST,
    TEST_DICT,
)
from mask.mask import mask


def test_mask_dict_not_inplace():
    out = mask(TEST_DICT, DATA_TO_MASK)
    assert out
    assert out["name"] == MASKED_TEST_DICT["name"]
    assert out["DOB"] == MASKED_TEST_DICT["DOB"]
    assert out["email"] == MASKED_TEST_DICT["email"]
    assert out["id"] != MASKED_TEST_DICT["id"]


def test_mask_dict_inplace():
    tmp = deepcopy(TEST_DICT)
    out = mask(tmp, DATA_TO_MASK, inplace=True)
    assert out is None
    assert tmp["name"] == MASKED_TEST_DICT["name"]
    assert tmp["DOB"] == MASKED_TEST_DICT["DOB"]
    assert tmp["email"] == MASKED_TEST_DICT["email"]
    assert tmp["id"] != MASKED_TEST_DICT["id"]


def test_mask_list_of_dict_not_inplace():
    tmp_list = [TEST_DICT]
    out = mask(tmp_list, DATA_TO_MASK)
    assert out
    assert out[0]["name"] == MASKED_TEST_DICT["name"]
    assert out[0]["DOB"] == MASKED_TEST_DICT["DOB"]
    assert out[0]["email"] == MASKED_TEST_DICT["email"]


def test_mask_list_of_dict_inplace():
    tmp_list = deepcopy([TEST_DICT])
    out = mask(tmp_list, DATA_TO_MASK, inplace=True)
    assert out is None
    assert tmp_list[0]["name"] == MASKED_TEST_DICT["name"]
    assert tmp_list[0]["DOB"] == MASKED_TEST_DICT["DOB"]
    assert tmp_list[0]["email"] == MASKED_TEST_DICT["email"]


def test_mask_dict_with_inner_dict_not_inplace():
    out = mask(TEST_DATA_WITH_INNER_DICT, DATA_TO_MASK)
    assert out
    assert out["name"] == MASKED_DATA_WITH_INNER_DICT["name"]
    assert out["DOB"] == MASKED_DATA_WITH_INNER_DICT["DOB"]
    assert out["email"] == MASKED_DATA_WITH_INNER_DICT["email"]
    assert (
        out["address"]["door_no"] == MASKED_DATA_WITH_INNER_DICT["address"]["door_no"]
    )
    assert out["address"]["street"] == MASKED_DATA_WITH_INNER_DICT["address"]["street"]
    assert out["address"]["city"] == MASKED_DATA_WITH_INNER_DICT["address"]["city"]
    assert out["address"]["state"] == MASKED_DATA_WITH_INNER_DICT["address"]["state"]
    assert (
        out["address"]["country"] == MASKED_DATA_WITH_INNER_DICT["address"]["country"]
    )
    assert out["salary"]["salary"] == MASKED_DATA_WITH_INNER_DICT["salary"]["salary"]
    assert out["numbers"]["mobile"] == MASKED_DATA_WITH_INNER_DICT["numbers"]["mobile"]
    assert out["numbers"]["home"] == MASKED_DATA_WITH_INNER_DICT["numbers"]["home"]
    assert out["numbers"]["work"] == MASKED_DATA_WITH_INNER_DICT["numbers"]["work"]


def test_mask_dict_with_inner_dict_inplace():
    tmp = deepcopy(TEST_DATA_WITH_INNER_DICT)
    out = mask(tmp, DATA_TO_MASK, inplace=True)
    assert out is None
    assert tmp["name"] == MASKED_DATA_WITH_INNER_DICT["name"]
    assert tmp["DOB"] == MASKED_DATA_WITH_INNER_DICT["DOB"]
    assert tmp["email"] == MASKED_DATA_WITH_INNER_DICT["email"]
    assert (
        tmp["address"]["door_no"] == MASKED_DATA_WITH_INNER_DICT["address"]["door_no"]
    )
    assert tmp["address"]["street"] == MASKED_DATA_WITH_INNER_DICT["address"]["street"]
    assert tmp["address"]["city"] == MASKED_DATA_WITH_INNER_DICT["address"]["city"]
    assert tmp["address"]["state"] == MASKED_DATA_WITH_INNER_DICT["address"]["state"]
    assert (
        tmp["address"]["country"] == MASKED_DATA_WITH_INNER_DICT["address"]["country"]
    )
    assert tmp["salary"]["salary"] == MASKED_DATA_WITH_INNER_DICT["salary"]["salary"]
    assert tmp["numbers"]["mobile"] == MASKED_DATA_WITH_INNER_DICT["numbers"]["mobile"]
    assert tmp["numbers"]["home"] == MASKED_DATA_WITH_INNER_DICT["numbers"]["home"]
    assert tmp["numbers"]["work"] == MASKED_DATA_WITH_INNER_DICT["numbers"]["work"]


def test_mask_dict_with_inner_list_not_inplace():
    out = mask(TEST_DATA_WITH_INNER_LIST, DATA_TO_MASK)
    assert out
    assert out["name"] == MASKED_DATA_WITH_INNER_LIST["name"]
    assert out["DOB"] == MASKED_DATA_WITH_INNER_LIST["DOB"]
    assert out["email"] == MASKED_DATA_WITH_INNER_LIST["email"]
    assert (
        out["neighbors"][0]["name"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["name"]
    )
    assert (
        out["neighbors"][0]["mobile"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["mobile"]
    )
    assert (
        out["neighbors"][0]["street"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["street"]
    )
    assert (
        out["neighbors"][0]["city"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["city"]
    )
    assert (
        out["neighbors"][0]["email"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["email"]
    )


def test_mask_dict_with_inner_list_inplace():
    tmp = deepcopy(TEST_DATA_WITH_INNER_LIST)
    out = mask(tmp, DATA_TO_MASK, inplace=True)
    assert out is None
    assert tmp["name"] == MASKED_DATA_WITH_INNER_LIST["name"]
    assert tmp["DOB"] == MASKED_DATA_WITH_INNER_LIST["DOB"]
    assert tmp["email"] == MASKED_DATA_WITH_INNER_LIST["email"]
    assert (
        tmp["neighbors"][0]["name"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["name"]
    )
    assert (
        tmp["neighbors"][0]["mobile"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["mobile"]
    )
    assert (
        tmp["neighbors"][0]["street"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["street"]
    )
    assert (
        tmp["neighbors"][0]["city"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["city"]
    )
    assert (
        tmp["neighbors"][0]["email"]
        == MASKED_DATA_WITH_INNER_LIST["neighbors"][0]["email"]
    )


def test_mask_dict_not_inplace_with_custom_filler():
    out = mask(TEST_DICT, DATA_TO_MASK, fill="-")
    assert out
    assert out["name"] == MASKED_TEST_DICT["name"].replace("*", "-")
    assert out["DOB"] == MASKED_TEST_DICT["DOB"]
    assert out["email"] == MASKED_TEST_DICT["email"].replace("*", "-")


def test_mask_dict_inplace_with_custom_filler():
    tmp = deepcopy(TEST_DICT)
    out = mask(tmp, DATA_TO_MASK, inplace=True, fill="-")
    assert out is None
    assert tmp["name"] == MASKED_TEST_DICT["name"].replace("*", "-")
    assert tmp["DOB"] == MASKED_TEST_DICT["DOB"]
    assert tmp["email"] == MASKED_TEST_DICT["email"].replace("*", "-")
