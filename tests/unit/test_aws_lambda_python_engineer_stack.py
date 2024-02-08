import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_lambda_python_engineer.aws_lambda_python_engineer_stack import AwsLambdaPythonEngineerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_lambda_python_engineer/aws_lambda_python_engineer_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsLambdaPythonEngineerStack(app, "aws-lambda-python-engineer")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
