from libs.aws.rekognition import Rekognition
from libs.aws.rekognition import RekognitionTools

if __name__ == "__main__":
    image_path = "data/face6.png"

    rekognition = Rekognition()

    labels = rekognition.detect_labels_local_file(path=image_path)
    faces = rekognition.detect_faces_local_file(path=image_path)

    confident_labels = RekognitionTools.get_labels_from_confidence(labels_response=labels, min=97.0)
    print(confident_labels)
    print(faces)