# AWS Lambda

Today I learnt ...

## ... how to quickly iterate on a nodejs function that uses other AWS services

> 2024-01-23T12:32:03+00:00
> A nodejs script with dependencies can be zipped and function code updated using the `aws-cli` 

#### Prerequisites
- `aws-cli` 
	- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

- An [sqs.md](SQS queue)

### Recipe

1. Create the Role

    Create the role and attach a policy to the role that grants permissions to the lambda function to log to CloudWatch

    <details>
    <summary>Expand for code</summary>

    ```bash
    pwd /home/jon/code/today-i-learned
    cd assets/aws-lambda
    aws iam create-role --role-name til-lambda-example-role --assume-role-policy-document file://trust-policy.json;

    aws iam attach-role-policy --role-name til-lambda-example-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

    ```
    </details>
    <br>
2. Create a barebones Lambda with aws-cli

    See the start version of the lambda:
    [assets/aws-lambda/start/index.js](index.js)
    
    Add this file to a zip and run `aws lambda create-function` populating the ARN to the role with your AWS account number.

    <details>
    <summary>Expand for code</summary>

    ```bash
    cd assets/aws-lambda/start/
    zip -r9 lambda.zip index.js package.json;

    aws lambda create-function --function-name til-lambda-example --runtime nodejs20.x --zip-file fileb://lambda.zip --handler index.handler --role "arn:aws:iam::YOUR_ACCOUNT_NUMBER:role/til-lambda-example-role"

    ```
    </details>

    <br>

3. Invoke the Lambda with aws-cli

    To test the basic lambda has been created, invoke it passing a sample payload `event.json`

    After running the code, look in `response.json`

    <details>
    <summary>Expand for code</summary>

    ```bash
    aws lambda invoke --function-name til-lambda-example --payload file://event.json response.json;

    cat response.json
    {"headers":{"Content-Type":"application/json"},"statusCode":200,"body":"{\"success\":true}"}%    

    ```
    </details>

    <br>


4. Now we know we can invoke a simple lambda, let's try one with packages.
    
    We'll use the existing lambda function and use the [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html](update-function-code) `aws-cli` method to update the code.

    In the script's directory, install packages, create a new zip, and update the function code.

    <details>
    <summary>Expand for code</summary>

    ```bash
    cd ../packages
    npm install
    
    zip -r9 lambdapackages.zip .
    aws lambda update-function-code --function-name til-lambda-example --zip-file fileb://lambdapackages.zip

    # Invoke lambdapackages remotely
    aws lambda invoke --function-name til-lambda-example --payload file://event.json response.json
    cat response.json
    {"headers":{"Content-Type":"application/json"},"statusCode":200,"body":"{\"success\":true}"}%    
    ```
    </details>
    <br>
5. Iterate accordingly.

    Modify your code, rezip, update the function code and run it

    <details>
    <summary>Expand for code</summary>

    ```bash
    rm -rf lambdapackages.zip; 

    zip -r9 lambdapackages.zip .
    aws lambda update-function-code --function-name til-lambda-example --zip-file fileb://lambdapackages.zip


    aws lambda invoke --function-name til-lambda-example --payload file://event.json response.json
    cat response.json
    {"headers":{"Content-Type":"application/json"},"statusCode":200,"body":"{\"success\":true}"}%    
    ```
    </details>
    <br>

6. Remove role and lambda when you've finished.

    <details>
    <summary>Expand for code</summary>

    ```bash
    aws lambda delete-function --function-name til-lambda-example;

    aws iam delete-role --role-name til-lambda-example-role
    ```
    </details>

#### Resources
- https://stackoverflow.com/a/34439125
- https://bobbyhadz.com/blog/aws-cli-create-lambda-function
- https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-nodejs.html

- Update environment variables
    - https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
    - https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html
    - 
        ```bash
        aws lambda update-function-configuration --function-name til-lambda-example --environment "Variables={JW_AWS_ACCESS_KEY_ID=XXX,JW_AWS_SECRET_ACCESS_KEY=YYY}"
        ```
