from aws_cdk import (
    Stack,
    pipelines,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions
)
from constructs import Construct

class frontdev(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        git_repo_owner = "Oversecured-traine"
        git_repo_name = "ovsrd-trainee-front"
        git_branch = "dev"
        connection_arn = "arn:aws:codestar-connections:eu-north-1:592699102634:connection/1810dca9-5df5-41e4-8885-59f5bd6de8b0"
        git_input = pipelines.CodePipelineSource.connection(
            repo_string=git_repo_owner + "/" + git_repo_name,
            branch=git_branch,
            connection_arn=connection_arn
        )

        code_pipeline = codepipeline.Pipeline(
            self, "Pipeline",
            pipeline_name="dev-pipeline",
            cross_account_keys=False
        )

        synth_step = pipelines.ShellStep(
            id="Synth",
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


