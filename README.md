
-------------------------------------------------------
Home assignment - DevOps Engineer - Karin Nechama:
-------------------------------------------------------

The feature:

Whenever a pull request is merged in a GitHub repository, all files that were changed (added / updated /
removed) should be logged.
 


To get started with this Terraform project, follow these steps:

1.  in "\test-karin\modules\api_gateway\variables.tf" change the "repo_name" to the needed name.

2. Make sure that you are using with your GitHub token that saved at AWS SecretManager (use the caommand below)
and change the secret name in "\test-karin\modules\github_function\function_code\lambda.py" line 13
    aws secretsmanager create-secret --name <YOUR-SECRET-NAME> --secret-string <YOUR-GITHUB-TOKEN>

2. Initialize Terraform:
    terraform init

3. Plan the terraform configuration:
    terraform plan

 Note:
 In "\test-karin\providers.tf" there is the GitHub token to use the webhook resorce.
 The best practices is to inject the token from GitHub secret, but I didn't make a GitiOps process to terraform
 And this is the reson it hardcoded.
