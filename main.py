import boto3
import sys

def get_security_group_id(common_name):
    ec2 = boto3.client("ec2", region_name="us-west-2")

    response = ec2.describe_security_groups()
    for security_group in response['SecurityGroups']:
        if security_group['GroupName'] == common_name:
            return security_group['GroupId']
        
if __name__ == '__main__':
    if sys.argv[1] == "help" or sys.argv[1] == "--help" or sys.argv[1] == "usage" or sys.argv[1] == "--usage":
        print("USAGE: python3 main.py <security group name>")
    else:
        sg_id = get_security_group_id(sys.argv[1])
        if sg_id == None:
            print("Security Group Not found")
        else:
            print(sg_id)