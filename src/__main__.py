import logging
import logging.config
import json
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from xyz import *
from advanced_rainbow import AdvancedRainbow

if __name__ == "__main__":
    rb = AdvancedRainbow()
    rb.run()
    