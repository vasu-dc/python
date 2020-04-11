import boto3


aws_con=boto3.session.Session(profile_name='608515732360-ADFS-MHF-SystemAdministrator')

client=aws_con.client('ec2')
response = client.describe_vpcs()


for vpc in response['Vpcs']:
    if 'Tags' in vpc:
        for tag in vpc['Tags']:
            print(f"{vpc['VpcId']}::{tag['Value']}")
    else:
        print(f"{vpc['VpcId']}::NoTag")
