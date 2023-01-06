from argparse import ArgumentParser
from .converter import Converter
from .options import OPTIONS

def run():
    parser = ArgumentParser(description = 'media-morfosis')
    parser.add_argument('file')
    parser.add_argument('-c', choices=OPTIONS.values())
    args = parser.parse_args()

    converter = Converter(args.file)
    method = getattr(converter, args.c)
    method()

if __name__ == "__main__":
    run()
