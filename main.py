import argparse
from stegamesh import StegaMesh

parser = argparse.ArgumentParser()
parser.add_argument("source", help=".obj source")
parser.add_argument("text", nargs="?", help="Text to hide")
parser.add_argument("destination", nargs="?", help="File containing embedded text")
parser.add_argument("-d", action="store_true", help="Decode hidden text")

args = parser.parse_args()

if not (args.text or args.d):
    parser.error("Text to hide is missing.")


obj = StegaMesh(args.source)
if args.d:
    print(obj.extract_text())
else:
    obj.hide_text(args.text)
    obj.save(args.destination)

