import logging.config
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from advanced_rainbow import AdvancedRainbow

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
    rb = AdvancedRainbow()
    rb.run()
