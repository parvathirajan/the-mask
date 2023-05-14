import copy
from typing import Dict, Optional

from mask._common import (
    __EMAIL_TYPES,
    __NUMBER,
    __STRING_TYPES,
    __ZNUMBER,
    mask_email,
    mask_string,
    randnum,
    znum,
)


def mask(
    payload,
    data_to_mask: Dict,
    inplace: Optional[bool] = False,
    fill: Optional[str] = "*",
):
    """
    Get the JSON payload along with the keys to mask

    Once the data is masked, either
        - returned the masked data (`inplace = False` by default)
        - Modify the payload itself (If `inplace = True`)

    Parameters
    ----------
    #### payload: `List[Dict]` or `Dict`
        - Data to masked (JSON payload) in the form of list of dict or dict

    #### data_to_mask : `Dict` i.e., `{"name": "str", ...}`
        - dictionary of keys and types, Listed below
        - To mask the string values: `'string'` or `'str'` # both behaves same
        - To mask the email: `'email'`
        - To mask the number: `'znumber'` or `'number'` # both have different usage
            - `znumber`: will convert the data into 0 (irrespective of the type)
            - `number`: will provide the random number with the same length as input

    #### inplace : `Optional[bool] = False` (default False)
        - If the inplace is passed as True then the JSON payload
        will be modified itself and it will return `None`

    #### fill : `Optional[str] = '*'` (default '*')
        - character to fill while masking the data
        - For example, if the user wants to mask the data with '#'
        in the place of characters then the fill should be passed as '#'

    Returns
    -------
    - `List[Dict]` or `Dict` or `None` (Incase if `inplace = True`)

    Usage
    ------
    >>> from mask import mask
    >>> payload = {
            "name": "Jennifer",
            "email" "Jenn@abc.corp",
            "salary": "250000"
        }
    >>> data_to_mask = {
            "name": "str", # It can also be `string`
            "email": "email",
            "salary": "znumber"
        }
    >>> result = mask(payload, data_to_mask) # Option: 1
    >>> print(result)
    >>> {
            "name": "J******r",
            "email" "J**n@a**.corp",
            "salary": "0"
        }
    >>> mask(payload, data_to_mask, inplace = True) # Option: 2
    >>> print(payload)
    >>> {
            "name": "J******r",
            "email" "J**n@a**.corp",
            "salary": "0"
        }
    >>>
    """
    if not inplace:
        payload = copy.deepcopy(payload)
    keys_to_mask = data_to_mask.keys()
    if isinstance(payload, dict):
        for key, val in payload.items():
            if isinstance(val, dict):
                mask(val, data_to_mask, inplace=True, fill=fill)
            elif isinstance(val, list):
                for dct in val:
                    mask(dct, data_to_mask, inplace=True, fill=fill)
            else:
                if key in keys_to_mask:
                    type = data_to_mask[key]
                    if type in __STRING_TYPES and val:
                        payload[key] = mask_string(val, fill=fill)
                    elif type in __EMAIL_TYPES and val:
                        payload[key] = mask_email(val, fill=fill)
                    elif type == __ZNUMBER and val:
                        payload[key] = znum(val)
                    elif type == __NUMBER and val:
                        payload[key] = randnum(len(str(val)))

    if isinstance(payload, list):
        for dct in payload:
            mask(dct, data_to_mask, inplace=True)

    if not inplace:
        return payload
