<h2 align="center">
    A package to hide/mask PII information in the JSON object.
</h2>

<p align="center">
<a href="https://coveralls.io/github/parvathirajan/the-mask?branch=main"><img alt="Coverage Status" src="https://coveralls.io/repos/github/parvathirajan/the-mask/badge.svg?branch=main"></a>
<a href="https://github.com/parvathirajan/the-mask/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pypi.org/project/the-mask/"><img alt="PyPI" src="https://img.shields.io/pypi/v/the-mask"></a>
<a href="https://github.com/parvathirajan/the-mask"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Installation and usage

### Installation

The-mask requires Python 3.6+ and can be easily installed using the most common Python packaging tools. 

We recommend installing the latest stable release from PyPI with pip:

```bash
$ pip install the-mask
```

### Usage and documentation

the-mask is used to mask the PII or sensitive data in the JSON object
with more flexible way.

```python
from mask import mask
payload = {
    "name": "Jennifer",
    "email" "Jenn@abc.corp",
    "salary": "250000"
}
data_to_mask = {
    "name": "str", # It can also be `string`
    "email": "email",
    "salary": "znumber"
}
result = mask(payload, data_to_mask) # Option: 1
print(result)

# Result:
# {
#     "name": "J******r",
#     "email" "J**n@a**.corp",
#     "salary": "0"
# }


# Alternative Way: If the user wanted to modify the Payload itself
# Pass the inplace option as True
mask(payload, data_to_mask, inplace = True) # Option: 2
print(payload)

# Result:
# {
#     "name": "J******r",
#     "email" "J**n@a**.corp",
#     "salary": "0"
# }
```

##### How the Data to Mask param works?

| Type of Data                                | Example Dict Key | Value   | Description                                                                                                     |
|---------------------------------------------|------------------|---------|-----------------------------------------------------------------------------------------------------------------|
| Plain Text values i.e., Name, Address etc., | name             | `str`     | `string` or `str` can be passed to determine the value is a string                                              |
| Email ID                                    | emailAddress     | `email`   | `email` is to mask the email id i.e., `K***n@a**.corp`                                                            |
| Numerical Values                            | salary           | `znumber` | `znumber` is used to convert the numerical value into 0  i.e., 250000 -> 0, 10000.90 -> 0.0, "1,135,000" -> "0" |
| Identity based Numerical Values               | id               | `number`  | `number` converts the value into random number with equivalent length.                                          |


## License

MIT

## Code of Conduct

Everyone participating in _the-mask_ project, and in particular in the issue tracker,
and pull requests is expected to treat other people with respect.

---

Give a ⭐️ if this project helped you!
