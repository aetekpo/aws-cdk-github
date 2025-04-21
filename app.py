#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk_github.aws_cdk_github_stack import AwsCdkGithubStack

app = cdk.App()
AwsCdkGithubStack(app, "AwsCdkGithubStack")
app.synth()
