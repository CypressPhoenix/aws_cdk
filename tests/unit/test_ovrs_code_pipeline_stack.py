import aws_cdk as core
import aws_cdk.assertions as assertions

from ovrs_code_pipeline.ovrs_code_pipeline_stack import OvrsCodePipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ovrs_code_pipeline/ovrs_code_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = OvrsCodePipelineStack(app, "ovrs-code-pipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
