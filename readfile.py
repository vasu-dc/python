import boto3


account_list =[]
region_list =[]


file= open("profiles","r+")
file2 = open("Regions","r+")
file3=open("vpcinfo","a+")
file4=open("tgwinfo","a+")

for prf in file:
    account_list.append(prf)
for reg in file2:
    region_list.append(reg)

for profile in account_list:
    print("Listing for ")
    for region in region_list:
        aws_con=boto3.session.Session(profile_name=profile,region_name=region)
        client=aws_con.client('ec2')
        response1 = client.describe_vpcs()
        response2 = client.describe_transit_gateway_attachments()
        for vpc in response1['Vpcs']:
            if 'Tags' in vpc:
                for tag in vpc['Tags']:
                    file3.write(f"{vpc['VpcId']}::{tag['Value']}")
            else:
                file3.write(f"{vpc['VpcId']}::NoTag")

        for tg in response2['TransitGatewayAttachments']:
            file4.write(f"{tg['TransitGatewayId']}:{tg['ResourceId']}:{tg['State']}")


file.close()
file1.close()