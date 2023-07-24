from aws_cdk import (
    Stack,
    pipelines,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions
)
from constructs import Construct
import os

from dotenv import load_dotenv
load_dotenv()

class frontmain(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        git_repo_owner = os.environ.get("GIT_REPO_OWNER")
        git_repo_name = os.environ.get("GIT_REPO_NAME")
        git_branch = os.environ.get("GIT_BRANCH_MAIN")
        connection_arn = os.environ.get("CONNECTION_ARN")


        git_input = pipelines.CodePipelineSource.connection(
            repo_string=git_repo_owner + "/" + git_repo_name,
            branch=git_branch,
            connection_arn=connection_arn
        )

        code_pipeline = codepipeline.Pipeline(
            self, "Pipeline",
            pipeline_name="main-pipeline",
            cross_account_keys=False
        )

        synth_step = pipelines.ShellStep(
            id="Synth",
            install_commands=[
                'echo "Build"'
            ],
            commands=[
                'echo "Build"'
            ],
            input=git_input
        )

        pipeline = pipelines.CodePipeline(
            self, 'CodePipeline',
            self_mutation=True,
            code_pipeline=code_pipeline,
            synth=synth_step
        )


