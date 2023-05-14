from mask._common import mask_email, mask_string, randnum, znum
from mask.mask import mask

# module level doc-string
__doc__ = """
the-mask - python library for an easiest way to mask PII data
=====================================================================

**the-mask** is a Python package providing fast, and flexible, way of masking
the sensitive data (aka PII) which is coming in the JSON file or object. It will 
provide flexibility to the user to choose the key to mask at the root level of the 
object.


Main Features
-------------

  - Along with the data it gets the keys to mask the sensitive information
  - More flexible and reliable way to automate the masking with various options
  - Allows users to choose how to treat different kind of data based on the keys
"""

__all__ = ["mask", "mask_email", "mask_string", "znum", "randnum"]
