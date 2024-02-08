from aws_cdk import (
    Stack,
    aws_lambda
)
import os
from constructs import Construct

class AwsLambdaPythonEngineerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        list_all_channels_function = aws_lambda.Function(
            self,
            id='list_all_channels_function',
            code=aws_lambda.Code.from_asset('./aws_lambda_python_engineer/slack'),
            handler='list_all_channels.lambda_handler',
            runtime=aws_lambda.Runtime.PYTHON_3_11
        )

        list_all_messages_function = aws_lambda.Function(
            self,
            id='list_all_messages_function',
            code=aws_lambda.Code.from_asset('./aws_lambda_python_engineer/slack'),
            handler='list_all_messages.lambda_handler',
            runtime=aws_lambda.Runtime.PYTHON_3_11
        )

        list_all_comments_function = aws_lambda.Function(
            self,
            id='list_all_comments_function',
            code=aws_lambda.Code.from_asset('./aws_lambda_python_engineer/slack'),
            handler='list_all_comments.lambda_handler',
            runtime=aws_lambda.Runtime.PYTHON_3_11
        )
