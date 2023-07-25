from aws_cdk import (
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_codebuild as codebuild,
    Stack,
)
from constructs import Construct
import os
from dotenv import load_dotenv

load_dotenv()
class FrontMain(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        connection_arn = os.environ.get("CONNECTION_ARN_OVRS")
        git_branch = os.environ.get("GIT_BRANCH_MAIN")
        git_repo_name = os.environ.get("GIT_REPO_NAME_FRONT_OVRS")
        git_repo_owner = os.environ.get("GIT_REPO_OWNER_OVRS")


        pipeline_1 = codepipeline.Pipeline(self, "Pipeline1", pipeline_name="Pipeline1")

        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        github_source_action = codepipeline_actions.CodeStarConnectionsSourceAction(
            action_name="GitHubSource",
            owner=git_repo_owner,
            repo=git_repo_name,
            branch=git_branch,
            connection_arn= connection_arn,
            output=source_output,
            trigger_on_push=True,
        )

        pipeline_1.add_stage(stage_name="Source", actions=[github_source_action])

        project = codebuild.PipelineProject(
            self,
            "Pipeline1Project",
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
            environment=codebuild.BuildEnvironment(
                build_image=codebuild.LinuxBuildImage.STANDARD_1_0
            ),
        )

        build_action = codepipeline_actions.CodeBuildAction(
            action_name="BuildAction",
            input=source_output,
            project=project,
            outputs=[build_output],
        )


        pipeline_1.add_stage(stage_name="Build", actions=[build_action])