from libs.aws.aws_rekognition import AwsRekognition
from libs.aws.aws_rekognition import AwsRekognitionTools

if __name__ == "__main__":
    image_path = "data/face6.png"

    rekognition = AwsRekognition()

    labels = rekognition.detect_labels_local_file(path=image_path)
    faces = rekognition.detect_faces_local_file(path=image_path)

    