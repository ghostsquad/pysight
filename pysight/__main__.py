import traceback
import sys
import logging

logger = logging.getLogger(__name__)

def main(args):
    pass

if __name__ == '__main__':
    try:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        main(sys.argv[1:])
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)