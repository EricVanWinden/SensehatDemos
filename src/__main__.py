import argparse
import logging.config
from advanced_rainbow import AdvancedRainbow
from compass import Compass
from count_down import CountDown
from red_blue_gradient import RedBlueGradient
from number_matrix import NumberMatrix
from joystick import Joystick
from point_up import Accelerometer
from weather import Weather


def main() -> None:
    parser = argparse.ArgumentParser(description="Run SenseHat demo(s)")
    parser.add_argument(
        "--demo",
        choices=["0", "1", "2", "3", "4", "5"],
        default="0",
        help="Which demo to run (default: 0)",
    )

    parser.add_argument(
        "--direction",
        choices=["0", "90", "180", "270"],
        default="0",
        help="How to rotate the matrix (default: 0)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')

    nm = NumberMatrix()
    nm.direction = int(args.direction)
    if args.demo == "0":
        demo = AdvancedRainbow()
    elif args.demo == "1":
        demo = Compass()
    elif args.demo == "2":
        demo = CountDown()
    elif args.demo == "3":
        demo = RedBlueGradient()
    elif args.demo == "4":
        demo = Joystick()
    elif args.demo == "5":
        demo = Accelerometer()
    elif args.demo == "6":
        demo = Weather()
    else:
        logging.error(f"Invalid demo choice: {args.demo}")
        return
    demo.nm = nm
    demo.run()


if __name__ == "__main__":
    main()
