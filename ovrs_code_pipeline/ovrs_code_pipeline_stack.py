from aws_cdk import (
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_codebuild as codebuild,
    Stack,
)
from constructs import Construct
class FrontMain(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)



        pipeline_1 = codepipeline.Pipeline(self, "Pipeline1", pipeline_name="Pipeline1")


        github_source_action = codepipeline_actions.CodeStarConnectionsSourceAction(
            action_name="GitHubSource",
            owner="",
            repo="",
            branch="",
            connection_arn="",
            output=codepipeline.Artifact(),
            trigger_on_push=True,
        )

        pipeline_1.add_stage(stage_name="Source", actions=[github_source_action])

        project = codebuild.PipelineProject(
            self,
            "Pipeline1Project",
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
            environment=codebuild.BuildEnvironment(
                build_image=codebuild.LinuxBuildImage.STANDARD_1_0()
            ),
        )

        build_action = codepipeline_actions.CodeBuildAction(
            action_name="BuildAction",
            input=pipeline_1.stages[0].action_outputs[0],
            project=project,
            outputs=[codepipeline.Artifact()],
        )


        pipeline_1.add_stage(stage_name="Build", actions=[build_action])

