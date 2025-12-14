import logging.config
from advanced_rainbow import AdvancedRainbow

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
    rb = AdvancedRainbow()
    rb.run()
