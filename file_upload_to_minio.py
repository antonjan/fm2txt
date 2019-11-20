# Import MinIO library.
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('localhost:9000',
                    access_key='PX7Y4M4GOAW6ZM3VIRKN',
                    secret_key='JBejQ+JU5ClGYkAGgROYJM9sN+LnLNxsA+cEE200',
                    secure=False)

# Make a bucket with the make_bucket API call.
try:
       print(minioClient.make_bucket("antontest",location="None"))
except BucketAlreadyOwnedByYou as err:
       pass
except BucketAlreadyExists as err:
       pass
except ResponseError as err:
       raise

# Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
try:
       print(minioClient.fput_object('radio', 'recording_of_radio_station_3.wav', '/home/anton/fm2txt/recording_of_radio_station.wav'))
except ResponseError as err:
       print(err)


