import json
import os
import boto3
import urllib.request

def lambda_handler(event, context):

    # Create a Secrets Manager client
    secretsmanager = boto3.client('secretsmanager')

    # Retrieve the GitHub API token from AWS Secrets Manager
    try:
        secret_response = secretsmanager.get_secret_value(SecretId='KarinsGitHubAPIToken')
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret was not found.")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
        else:
            print("The request failed because of an unknown error:", e)
    else:
        # Extract the GitHub API token from the secret response
        github_api_token = secret_response['SecretString']

    body= event['body']
    body_dict = json.loads(body)
    
    repo_name= body_dict['repository']['name']
    pr_number = body_dict['pull_request']['number']
    owner_name = body_dict['repository']['owner']['login']

    pr_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/pulls/{pr_number}/files"
    headers = {'Authorization': f'token {github_api_token}'}
    req = urllib.request.Request(pr_url, headers=headers)
    response = urllib.request.urlopen(req)
    files_changed = [file['filename'] for file in json.loads(response.read().decode('utf-8'))]

    # Log the details to CloudWatch
    print(f"Repository: {owner_name}/{repo_name}")
    print(f"Files Changed: {files_changed}")

    # Return the files changed as a JSON object
    return {
        "statusCode": 200,
        "body": json.dumps({
            "repository": f"{owner_name}/{repo_name}",
            "files_changed": files_changed
        })
    }