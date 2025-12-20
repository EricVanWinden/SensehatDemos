import logging.config
from advanced_rainbow import AdvancedRainbow
from compass import Compass

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
    demo = AdvancedRainbow()
    demo.run()
    demo = Compass()
    demo.run()
