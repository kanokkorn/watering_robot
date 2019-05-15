from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cv2
import os, time
import tensorflow as tf
import sys
import numpy

cascade = cv2.CascadeClassifier("./cascade.xml")
cv2.ocl.setUseOpenCL(True)
camera_a = cv2.VideoCapture("http://192.168.1.147:2000")
camera_b = cv2.VideoCapture("http://192.168.1.148:2000")


def fruit_detect():
    ret_a, img_a = camera_a.read()
    ret_b, img_b = camera_b.read()
    gray_a = cv2.cvtColor(img_a, cv2.COLOR_BGR2GRAY)
    gray_b = cv2.cvtColor(img_b, cv2.COLOR_BGR2GRAY)
    palm_fruit = cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in palm_fruit:
        cv2.rectangle(img_a, (x, y), (x + w, y + h), (175, 244, 65), 2)
        cv2.rectangle(img_b, (x, y), (x + w, y + h), (175, 244, 65), 2)

        roi_gray_a = gray_a[y : y + h, x : x + w]
        roi_gray_b = gray_b[y : y + h, x : x + w]

        roi_color_a = img_a[y : y + h, x : x + w]
        roi_color_b = img_b[y : y + h, x : x + w]

        cv2.imwrite(
            "./opencv/img_" + str(time.asctime(time.localtime())) + ".jpg", roi_color_a
        )
        cv2.imwrite(
            "./opencv/img_" + str(time.asctime(time.localtime())) + ".jpg", roi_color_b
        )
def load_graph(modelfile):
	graph = tf.Graph()
	graph_def = tf.GraphDef()

	with open(modelfile, "rb") as model:
		graph_def.ParseFromString(model.read())
	with graph.as_default():
		tf.import_graph_def(graph_def)
	return graph

def read_tensor(img, input_height=299, input_width=299, input_mean=0, input_std=255):
	input_name = "file_reader"
	output_name = "normalized"
	file_reader = tf.read_file()

def classific():
    ret_a, img_a = camera_a.read()
    ret_b, img_b = camera_b.read()
	flie_name_a = img_a

if __name__ == "__main__":
    fruit_detect()
    classific()
    exit()

