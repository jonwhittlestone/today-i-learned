# awk

Today I learnt ...

## ... how to extract a full S3 bucket name from a grepped output

> 2024-01-04T10:40:11+00:00
>
> The output from `aws-cli s3 ls` is space delimited so grepped the bucket name followed by awk to extract the full id

#### Prerequisites
- `aws-cli` 
	- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

#### Recipe
```bash
aws s3 ls | grep storage-for-single-user | awk -F' ' '{print $3}'

storage-for-single-user-s3bucket-n7a7fpecimhe

```


#### Resources
- https://stackoverflow.com/a/36011760
 