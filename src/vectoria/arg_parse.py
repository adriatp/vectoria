import os
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert your png\'s to vector images')
    parser.add_argument('--image_path', type=str, help='Image path')
    parser.add_argument('--output_path', type=str, help='Output path')
    parser.add_argument('first_arg', type=str, nargs='?', help='First positional argument (optional)')
    args = parser.parse_args()

    # If --image_path is not provided, take the first positional argument as the image path
    if args.image_path is None and args.first_arg is not None:
        args.image_path = args.first_arg

    # If --output_path is not provided, set it to 'out/{consecutivefile}'
    if args.output_path is None:
        consecutivefile = 1
        while True:
            if os.path.exists(f'out/{consecutivefile}'):
                consecutivefile += 1
            else:
                break
        args.output_path = f'out/{consecutivefile}.svg'

    # Check if there are no arguments or more than 1
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        parser.print_help()
        sys.exit(1)

    return args