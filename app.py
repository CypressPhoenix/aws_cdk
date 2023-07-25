from aws_cdk import App
from ovrs_code_pipeline.forntmain import FrontMain
from ovrs_code_pipeline.frontdev import FrontDev
import os
from dotenv import load_dotenv
load_dotenv()

region = os.environ.get("REGION")

app = App()
FrontDev(app, "FrontDevStack", env={'region': region})
FrontMain(app, "FrontMainStack", env={'region': region})
app.synth()

