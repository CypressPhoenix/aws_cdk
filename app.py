from aws_cdk import App
from ovrs_code_pipeline.forntmain import FrontMain
from ovrs_code_pipeline.frontdev import FrontDev
from front_infrastructure.front_infra_main import FrontInfrastructureMain
from front_infrastructure.front_infra_dev import FrontInfrastructureDev
import os
from dotenv import load_dotenv
load_dotenv()

region = os.environ.get("REGION_HOME")

app = App()
FrontInfrastructureMain(app, "FrontInfraMain", env={'region': region})
FrontInfrastructureDev(app, "FrontInfraDev", env={'region': region})
FrontDev(app, "FrontDevStack", env={'region': region})
FrontMain(app, "FrontMainStack", env={'region': region})
app.synth()

