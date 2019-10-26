# Terraform

This repository has several examples that deploy [Echo](../Python/web/echo) server on top of the AWS services:
  * [EC2 (auto-scaling), ELB, S3](./ec2-auto-scaling)
  * [Lambda (function), ELB, S3](./lambda-function)
  
# Requirements
Before using scenarios you must provide valid credentials to `~/.aws/credentials`.
Minimal configuration should look like:
```bash
# ~/.aws/credentials
[default]
aws_access_key_id=
aws_secret_access_key=
region=
output=json
```
Choose a scenario and adapt `variables.tf` for your needs.

# Execution

```bash
terraform init
terraform plan -out echo.plan
terraform applay "echo.plan"
```

# Cleaning
Be careful, S3 bucket can't be deleted in case if something was created inside, so delete it manually.
At some point, this functionality will be added to scenarios.

```bash
terraform destroy
```
