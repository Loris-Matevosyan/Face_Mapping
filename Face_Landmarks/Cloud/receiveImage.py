import boto3

bucket_name = 'bucket_name'
file_key = 'path/from.jpg'
download_path = 'path/to.jpg'

# try:
    # s3.downlaod_file(bucket_name, file_key, download_path)
# except Exception as e:
#     print(f'Error: {e}')