import os
from aws_cdk import App
from ovrs_code_pipeline.ovrs_code_pipeline_stack import OvrsCodePipelineStack
from ovrs_code_pipeline.frontdev import frontdev
from ovrs_code_pipeline.forntmain import frontmain

app = App()

OvrsCodePipelineStack(app, "OvrsCodePipelineStack", env={
    "region": "eu-central-1"
})

frontmain(app, "frontmain", env={
    "region": "eu-central-1"
})

frontdev(app, "frontdev", env={
    "region": "eu-central-1"
})
app.synth()


