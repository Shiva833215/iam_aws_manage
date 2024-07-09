import sys
import boto3

def create_policy(policy_name):
    # Implement logic to create IAM policy
    client = boto3.client('iam')
    response = client.create_policy(
        PolicyName=policy_name,
        PolicyDocument='{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"*","Resource":"*"}]}'
    )
    print(f"Policy {policy_name} created successfully.")
    print(response)

def create_role(role_name):
    # Implement logic to create IAM role
    client = boto3.client('iam')
    response = client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument='{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},"Action":"sts:AssumeRole"}]}'
    )
    print(f"Role {role_name} created successfully.")
    print(response)

def delete_policy(policy_arn):
    # Implement logic to delete IAM policy
    client = boto3.client('iam')
    response = client.delete_policy(
        PolicyArn=policy_arn
    )
    print(f"Policy {policy_arn} deleted successfully.")
    print(response)

def delete_role(role_name):
    # Implement logic to delete IAM role
    client = boto3.client('iam')
    response = client.delete_role(
        RoleName=role_name
    )
    print(f"Role {role_name} deleted successfully.")
    print(response)

def attach_policy_to_role(role_name, policy_arn):
    # Implement logic to attach IAM policy to role
    client = boto3.client('iam')
    response = client.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    print(f"Policy {policy_arn} attached to role {role_name}.")
    print(response)

def detach_policy_from_role(role_name, policy_arn):
    # Implement logic to detach IAM policy from role
    client = boto3.client('iam')
    response = client.detach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    print(f"Policy {policy_arn} detached from role {role_name}.")
    print(response)

# Main execution based on command-line arguments
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 opr.py <operation> [arguments...]")
        sys.exit(1)

    operation = sys.argv[1]
    if operation == "create_policy":
        for policy_name in sys.argv[2:]:
            create_policy(policy_name)

    elif operation == "create_role":
        for role_name in sys.argv[2:]:
            create_role(role_name)

    elif operation == "delete_policy":
        for policy_arn in sys.argv[2:]:
            delete_policy(policy_arn)

    elif operation == "delete_role":
        for role_name in sys.argv[2:]:
            delete_role(role_name)

    elif operation == "attach_policy_to_role":
        role_name = sys.argv[2]
        for policy_arn in sys.argv[3:]:
            attach_policy_to_role(role_name, policy_arn)

    elif operation == "detach_policy_from_role":
        role_name = sys.argv[2]
        for policy_arn in sys.argv[3:]:
            detach_policy_from_role(role_name, policy_arn)

    else:
        print("Invalid operation specified.")
        sys.exit(1)

