from random import randint
from typing import Optional, Union

__STRING_TYPES = ("string", "str")
__EMAIL_TYPES = ("email",)
__ZNUMBER = "znumber"
__NUMBER = "number"


def mask_string(s, fill: Optional[str] = "*"):
    """
    Get the string and return the masked string

    Parameters
    ----------
    #### s: `str`
        - String to mask

    #### fill : `Optional[str] = '*'` (default '*')
        - character to fill while masking the data
        - For example, if the user wants to mask the data with '#'
        in the place of characters then the fill should be passed as '#'

    Returns
    -------
    - `str` : Will return the masked string

    Usage
    ------
    >>> from mask import mask_string
    >>> payload = {
            "name": "Jennifer",
            "email" "Jenn@abc.corp",
            "salary": "250000"
        }
    >>> result = mask_string(payload["name"]) # Option: 1
    >>> print(result)
    >>> J******r
    >>>
    >>> result = mask_string(payload["name"], fill = "_") # Option: 2
    >>> print(result)
    >>> J______r
    >>>
    """

    if s:
        s = str(s)
    else:
        return s
    return s[0] + (
        (fill * (len(s) - 2) + (s[len(s) - 1] if len(s) - 1 else "") if s else s)
        if len(s) >= 4
        else fill * (len(s) - 1)
    )


def randnum(num: Union[str, int]):
    """
    Get number to provide the random number with equivalent length

    Parameters
    ----------
    #### num: `Union[str, int]`
        - number to process

    Returns
    -------
    - `str` or `int` : Will return the random number with equal length

    Usage
    ------
    >>> from mask import randnum
    >>> payload = {
            "name": "Jennifer",
            "email" "Jenn@abc.corp",
            "salary": "250000"
        }
    >>> result = randnum(payload["salary"])
    >>> print(result)
    >>> 934890
    >>>
    """
    n = len(str(num))
    rand = randint(10 ** (n - 1), (10**n) - 1)
    if isinstance(num, str):
        return str(rand)
    else:
        return rand


def mask_email(email: str, fill: Optional[str] = "*"):
    """
    Get the email id to mask and return the masked email id

    Parameters
    ----------
    #### email: `str`
        - Email ID to mask

    #### fill : `Optional[str] = '*'` (default '*')
        - character to fill while masking the data
        - For example, if the user wants to mask the data with '#'
        in the place of characters then the fill should be passed as '#'

    Returns
    -------
    - `str` : Will return the masked email string

    Usage
    ------
    >>> from mask import mask_email
    >>> payload = {
            "name": "Jennifer",
            "email" "Jenn@abc.corp",
            "salary": "250000"
        }
    >>> result = mask_string(payload["email"]) # Option: 1
    >>> print(result)
    >>> J**n@a**.corp
    >>>
    >>> result = mask_string(payload["email"], fill = "_") # Option: 2
    >>> print(result)
    >>> J__n@a__.corp
    >>>
    """
    try:
        if not email:
            return email
        at_index = email.index("@")
        dot_index = email.index(".")
        return (
            mask_string(email[0:at_index], fill)
            + "@"
            + mask_string(email[at_index + 1 : dot_index], fill)
            + "."
            + email[dot_index + 1 :]
        )
    except ValueError:
        return email


def znum(num: Union[str, float, int]):
    """
    Get the single string to mask

    Parameters
    ----------
    #### num: `Union[str, float, int]`
        - String to mask

    #### fill : `Optional[str] = '*'` (default '*')
        - character to fill while masking the data
        - For example, if the user wants to mask the data with '#'
        in the place of characters then the fill should be passed as '#'

    Returns
    -------
    - `str` : Will return the masked string

    Usage
    ------
    >>> from mask import mask_string
    >>> payload = {
            "name": "Jennifer",
            "email" "Jenn@abc.corp",
            "salary": "250000"
        }
    >>> result = mask_string(payload["name"]) # Option: 1
    >>> print(result)
    >>> J******r
    >>>
    >>> result = mask_string(payload["name"], fill = "_") # Option: 2
    >>> print(result)
    >>> J______r
    >>>
    """
    if isinstance(num, int) and not isinstance(num, bool):
        return 0
    elif isinstance(num, float):
        return 0.0
    elif isinstance(num, str):
        return "0"
    else:
        return num
