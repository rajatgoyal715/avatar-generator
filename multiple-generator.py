import os
from argparse import ArgumentParser

count = 0

def readArguments():
    parser = ArgumentParser()
    parser.add_argument("-c", "--count", dest="count", help="Number of images to generate")

    args = parser.parse_args()
    global count
    count = int(args.count)

def main():
	readArguments()
	for i in range(count):
		print("generating image: " + str(i+1))
		os.system("python generator.py -f test/test" + str(i+1) + ".png")


if __name__ == "__main__":
    main()