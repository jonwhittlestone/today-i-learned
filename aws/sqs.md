# SQS

Today I learnt ...

## ... how to provision an SQS queue with CloudFormation


> 2024-01-24T18:32:03+00:00
> Bringing up an SQS, enquing things, checking the contents, and deleting it.


#### Prerequisites
- `aws-cli` & AWS access credentials 
	- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html


### Recipe

1. Run stack

```bash
cd assets/sqs/cloudformation;

aws cloudformation create-stack --stack-name til-sqs-example --template-body file://sqsqueue.yaml
```

2. Get `QueueUrl` (optional)

```bash
aws cloudformation describe-stacks --stack-name til-sqs-example --query "Stacks[0].Outputs[?OutputKey=='QueueUrl'].OutputValue" --output text

https://sqs.eu-west-2.amazonaws.com/665898652183/til-sql-example
```

3. Enqueue

```bash
cd ..;
aws sqs send-message --queue-url https://sqs.eu-west-2.amazonaws.com/665898652183/til-sql-example --message-body "test"
```

4. Receive messages (purge the queue)

```bash
aws sqs receive-message --queue-url $(aws cloudformation describe-stacks --stack-name til-sqs-example --query "Stacks[0].Outputs[?OutputKey=='QueueUrl'].OutputValue" --output text) --attribute-names All

```

5. Delete stack

```bash
aws cloudformation delete-stack --stack-name til-sqs-example

```

### Resources
    - https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message.html