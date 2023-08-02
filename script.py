    # parse the command line
import os
import sys
import argparse
import shutil

from jetson_inference import imageNet
from imagenet import process_image
from jetson_utils import videoSource, videoOutput, cudaFont, Log

parser = argparse.ArgumentParser(description="Classify a live camera stream using an image recognition DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=imageNet.Usage() + videoSource.Usage() + videoOutput.Usage() + Log.Usage())

parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="googlenet", help="pre-trained model to load (see below for options)")
parser.add_argument("--topK", type=int, default=1, help="show the topK number of class predictions (default: 1)")

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# declare a variable called error
categories = os.listdir(args.input)
total = 0
error = 0

# get the length of the input folder and assign it to a variable called length
images = os.listdir(args.input)
total = len(images)

# loop through images in input
# TODO: define categories



for category in categories:
    category_folder_path = os.path.join(args.input, category)
    result_category_folder_path = os.path.join(args.output, category)

    if os.path.exists(result_category_folder_path):
        shutil.rmtree(result_category_folder_path)
    os.makedirs(result_category_folder_path, exist_ok=True)

    images = os.listdir(category_folder_path)

    total += len(images)

    for image in images:
        image_path = os.path.join(category_folder_path, image)
        output_image_path = os.path.join(result_category_folder_path, "test_{}".format(image))

        labels = process_image(image_path, output_image_path, args.network, args.topK)

        if category not in labels:
            error += 1

# redefine total to be the whole dataset
accuracy = (total - error) / total
print("Accuracy: ", accuracy)
    

# call process_image() with image, output folder path, network, and topK and assign the result to a variable called labels

# loop through the labels list to check if the folder name is in the list

# if the folder name (correct label) is not in the list, add one to error

# outside the loop, calculate the accuracy:
# accuracy = (total - error) / total

# def error
#     import os
#     size = 0
#     folderpath = 'NVIDIA/jetson-inference/jetson-inference/python/classification/data/face'
#     for path, dirs, files in os.walk(Folderpath):
#     for f in files:
#         fp = os.path.join(path, f)
#         size += os.path.getsize(fp)
    
#     os.listdir 
 
 
# print("accuracy: ", accuracy)


