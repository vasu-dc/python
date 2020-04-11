import boto3

aws_con=boto3.session.Session(profile_name='608515732360-ADFS-MHF-SystemAdministrator')

client=aws_con.client('ec2')
response = client.describe_transit_gateway_attachments()
print(type(response))

for tg in response['TransitGatewayAttachments']:
    print(f"{tg['TransitGatewayId']}:{tg['ResourceId']}:{tg['State']}")

