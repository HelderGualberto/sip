#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import logging

logging.basicConfig(filename="rekognition.log", level=logging.INFO)

class Rekognition:

    def __init__(self, region="us-east-1"):
        self.client = boto3.client('rekognition', region_name=region)

    def detect_labels(self, image):
        try:
            response = self.client.detect_labels(Image={'Bytes': image})
            return response
        except Exception as ex:
            logging.error("Error while detecting labels on image")
            raise ex
    
    def detect_faces(self, image):
        try:
            response = self.client.detect_faces(Image={'Bytes': image})
            return response
        except Exception as ex:
            logging.error("Error while detecting faces on image")
            raise ex

    def detect_labels_local_file(self, path):
        logging.debug("Start detect labels from file...")
        try:
            with open(path, 'rb') as image:
                response = self.detect_labels(image=image.read())
                logging.info(response)
                return response
        except Exception as ex:
            logging.error(f"Error while detecting labels form file {path}...")
            raise ex

    def detect_faces_local_file(self, path):
        logging.debug(f"Start detecting faces from file {path}")
        try:
            with open(path, 'rb') as image:
                response = self.detect_faces(image.read())
                logging.info(response)
                return response
        except Exception as ex:
            logging.error(f"Error while detecting faces from file {path}")
            raise ex

class RekognitionTools:
    @staticmethod
    def get_labels_from_confidence(labels_response, min=0.0, max=100.0, return_full_object=False):
        if "Labels" not in labels_response:
            logging.error("Error: Wrong labels_response object")
            raise Exception("Missing Labels key")

        labels = list(filter(lambda label: (label["Confidence"] > min and label["Confidence"] <= max), labels_response["Labels"]))

        if return_full_object:
            return labels
        
        return list(map(lambda label: label["Name"], labels))