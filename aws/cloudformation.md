# cloudformation

Today I learnt ...

## ... how to create a stack programatically and clean up

> 2023-12-18T17:00:11+00:00
>
> Create a stack for a public S3 bucket and remove it

#### Resources

- Bucket policy
	- https://cloudkatha.com/how-to-create-s3-bucket-policy-using-cloudformation/

#### Prerequisites

- `aws-cli` & AWS access credentials 
	- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

#### Recipe

1. Save this CloudFormation template to a file `howapped-storage-bucket.yml`

	```yaml
	AWSTemplateFormatVersion: "2010-09-09"
	Description: Welcome to Howapped Storage
	Resources:
		HowappedStorageBucket:
		Type: "AWS::S3::Bucket"
	
	```

2. Create the stack

	```sh
	aws cloudformation create-stack --stack-name howapped-storage-bucket --template-body file://howapped-storage-bucket.yml
	```

3. Check  it exists

	```sh
	aws s3 ls | grep howapped-storage-bucket
	```

4. Delete it

	```sh
	aws cloudformation delete-stack --stack-name howapped-storage-bucket
	```