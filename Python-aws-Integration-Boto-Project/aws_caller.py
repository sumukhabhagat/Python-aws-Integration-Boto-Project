import boto3

from aws_wrapper import show_buckets,upload_file,list_files,create_bucket

s3_obj=boto3.resource('s3')

show_buckets(s3_obj)


#file_path= '/home/ubuntume/DevOps_Zero_To_Hero/home.pdf'
#upload_file(s3_obj,'my-bucket-sharma-21111998-new',file_path,'sample')


#list_files(s3_obj,'my-bucket-sharma-21111998-new')


#create_bucket(s3_obj,'my-bucket-sharma-21111998-new')