from aws_rekognition import AwsRekognition
from aws_rekognition import AwsRekognitionTools


def test_label_filter():
    import json
    content = json.load(open("../resources/labels.json"))

    print(AwsRekognitionTools.get_labels_from_confidence(labels_response=content))

test_label_filter()