DATA_TO_MASK = {
    "name": "str",
    "email": "email",
    "street": "str",
    "door_no": "str",
    "city": "str",
    "state": "str",
    "mobile": "str",
    "home": "str",
    "work": "str",
    "salary": "znumber",
    "id": "number",
}

TEST_DICT = {
    "name": "Jennifer",
    "DOB": "04/04/1994",
    "email": "Jennifer@outlook.com",
    "id": 987654321,
}

MASKED_TEST_DICT = {
    "name": "J******r",
    "DOB": "04/04/1994",
    "email": "J******r@o*****k.com",
    "id": 987654321,
}

TEST_DATA_WITH_INNER_DICT = {
    "name": "Jennifer",
    "DOB": "04/04/1994",
    "email": "Jennifer@outlook.com",
    "address": {
        "door_no": "372",
        "street": "Wood Avenue",
        "city": "Iselin",
        "state": "NJ",
        "country": "USA",
    },
    "salary": {"salary": 2500000, "currency": "USD"},
    "numbers": {
        "mobile": "(234)-567-8900",
        "work": "(234)-567-8901",
        "home": "(234)-567-8902",
    },
}

MASKED_DATA_WITH_INNER_DICT = {
    "name": "J******r",
    "DOB": "04/04/1994",
    "email": "J******r@o*****k.com",
    "address": {
        "door_no": "3**",
        "street": "W*********e",
        "city": "I****n",
        "state": "N*",
        "country": "USA",
    },
    "salary": {"salary": 0, "currency": "USD"},
    "numbers": {
        "mobile": "(************0",
        "work": "(************1",
        "home": "(************2",
    },
}

TEST_DATA_WITH_INNER_LIST = {
    "name": "Jennifer",
    "DOB": "04/04/1994",
    "email": "Jennifer@outlook.com",
    "address": {
        "door_no": "372",
        "street": "Wood Avenue",
        "city": "Iselin",
        "state": "NJ",
        "country": "USA",
    },
    "numbers": {
        "mobile": "(234)-567-8900",
        "work": "(234)-567-8901",
        "home": "(234)-567-8902",
    },
    "neighbors": [
        {
            "name": "Catherine",
            "street": "23rd Avenue",
            "city": "Iselin",
            "email": "cat@gmail.com",
            "mobile": "2132132134",
        },
        {
            "name": "Kevin",
            "street": "2nd Avenue",
            "city": "Iselin",
            "email": "KEN@gmail.com",
            "mobile": "2032032134",
        },
    ],
}

MASKED_DATA_WITH_INNER_LIST = {
    "name": "J******r",
    "DOB": "04/04/1994",
    "email": "J******r@o*****k.com",
    "address": {
        "door_no": "3**",
        "street": "W*********e",
        "city": "I****n",
        "state": "N*",
        "country": "USA",
    },
    "numbers": {
        "mobile": "(************0",
        "work": "(************1",
        "home": "(************2",
    },
    "neighbors": [
        {
            "name": "C*******e",
            "street": "2*********e",
            "city": "I****n",
            "email": "c**@g***l.com",
            "mobile": "2********4",
        },
        {
            "name": "K***n",
            "street": "2********e",
            "city": "I****n",
            "email": "K**@g***l.com",
            "mobile": "2********4",
        },
    ],
}
