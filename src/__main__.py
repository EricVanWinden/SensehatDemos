import argparse
import logging.config
from advanced_rainbow import AdvancedRainbow
from compass import Compass
from count_down import CountDown
from sandbox import SandBox


def main() -> None:
    parser = argparse.ArgumentParser(description="Run SenseHat demo(s)")
    parser.add_argument(
        "--demo",
        choices=["0", "1", "2", "3", "4"],
        default="0",
        help="Which demo to run (default: 0)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')

    if args.demo == "0":
        demo = AdvancedRainbow()
    elif args.demo == "1":
        demo = Compass()
    elif args.demo == "2":
        demo = CountDown()
    elif args.demo == "3":
        demo = SandBox()
    else:
        logging.error(f"Invalid demo choice: {args.demo}")
        return
    demo.run()


if __name__ == "__main__":
    main()
