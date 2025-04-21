from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    Duration
)
from constructs import Construct

class AwsCdkGithubStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an S3 bucket
        bucket = s3.Bucket(self, "MyFirstBucket",
            versioned=True,
            bucket_name="cdk-github-demo-bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )

        # Create a Lambda function
        fn = _lambda.Function(self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="demo_lambda.lambda_handler",
            code=_lambda.Code.from_asset("lambda_code_demo"),
            timeout=Duration.seconds(30)
        )
