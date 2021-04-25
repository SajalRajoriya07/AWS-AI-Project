import cv2
import boto3

#using webcam to click pic - STEP 1
myphoto = "sajal.jpg"
cap = cv2.VideoCapture(0)
ret , photo = cap.read()
cv2.imwrite(myphoto, photo)
cap.release()


#uploading pic on the s3- STEP 2
region = "ap-south-1"
bucket = "sajalawsai-workshop"
upimage = "file.jpg"

s3 = boto3.resource('s3')
s3.Bucket(bucket).upload_file(myphoto, upimage)

#asking Rek to get Image from S3 - STEP 3
rek = boto3.client('rekognition', region)

response = rek.detect_labels(
     Image={
          'S3Object': {
              'Bucket': bucket,
              'Name': upimage,
              
          }
      },
      MaxLabels=10,
      MinConfidence=90
)

for i in range(2):
    print(response['Labels'][i]['Name'])