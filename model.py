from io import BytesIO
import logging
from typing import Dict, List

import numpy as np
import requests


logger = logging.getLogger("ray.serve")



def test_model():
   
    return {"output":"test model works fine."}