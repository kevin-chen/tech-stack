# USAGE
# python detect_face_parts.py --shape-predictor shape_predictor_68_face_landmarks.dat --video name.mp4

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
from imutils.video import VideoStream
from imutils.video import FPS
import time as t
from datetime import datetime, time

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-v", "--video", help="path to the (optional) video file")

args = vars(ap.parse_args())
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

## helper function to get distance between upper and lower lip
def getDistance(lst):
	# shape lst(lst): [[x,y], [x,y], [x,y]]
	# find highest and lowest positions
	# OpenCV Screen: x-axis: increases going up
	# 				 y-axis: decreases going up
	lst = lst.tolist()
	largest_x = 0
	largest_y = 0
	smallest_x = 500
	smallest_y = 500
	for elem in lst:
		x = elem[0]
		y = elem[1]
		if x > largest_x:
			largest_x = x;
		elif x < smallest_x:
			smallest_x = x;
		if y > largest_y:
			largest_y = y;
		elif y < smallest_y:
			smallest_y = y

	return largest_y - smallest_y

# video vs webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()
else:
	vs = cv2.VideoCapture(args["video"])

file = open("lip_distance.txt", "w")

t.sleep(2.0)
counter = 0
start_time = datetime.now()

# loops through frame
while True:
	# grab the current frame
	image = vs.read()

	# now = datetime.now()
	# counter += 1
	# seconds = (now - start_time).seconds
	#
	# if seconds != 0:
	# 	print("FPS", counter//seconds)

	# print(image.shape)

	# handle the frame from VideoCapture or VideoStream
	image = image[1] if args.get("video", False) else image

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if image is None:
		break

	try:
		# load the input image, resize it, and convert it to grayscale
		# image = cv2.imread(args["image"])
		image = imutils.resize(image, width=500)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# detect faces in the grayscale image
		rects = detector(gray, 1)

		# loop over the face detections
		for (i, rect) in enumerate(rects):
			# determine the facial landmarks for the face region, then
			# convert the landmark (x, y)-coordinates to a NumPy array
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			# loop over the face parts individually
			for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
				# clone the original image so we can draw on it, then
				# display the name of the face part on the image

				if name != "mouth":
					break

				# clone = image.copy()
				cv2.putText(image, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
					0.7, (0, 0, 255), 2)

				# loop over the subset of facial landmarks, drawing the
				# specific face part
				# print("\nBegin")
				# print(shape)
				for (x, y) in shape[i:j]:
					# print(x,y)
					cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
					# break
				distance = getDistance(shape)
				file.write(str(distance) + "\n")

				# print("Distance", distance)
				# print("End\n")

				# extract the ROI of the face region as a separate image
				(x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
				roi = image[y:y + h, x:x + w]
				roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)

				# show the particular face part
				# cv2.imshow("ROI", roi)
				cv2.imshow("Image", image)
				# cv2.waitKey(0)
			# visualize all facial landmarks with a transparent overlay
			output = face_utils.visualize_facial_landmarks(image, shape)
			cv2.imshow("Image", output)

			# cv2.waitKey(0)
	except:
		pass
		# print("Error")

	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break


# if we are not using a video file, stop the camera video stream
# otherwise, release the camera
if not args.get("video", False):
	vs.stop()
else:
	vs.release()

file.close()

# close all windows
cv2.destroyAllWindows()
