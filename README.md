# Preparation for Spark Summit
 Content:
  - Slides
  - Demo for Training
  - Demo for Scoring


Demo for Training contains 2 scripts:

 start_jupiter.sh - use to start jupiter and open prepared notebook with pipeline

 start_dai.sh - use to start dai and create mojo pipeline

 this folder also contains files with both trained pipelines


Demo for Scoring contains several scripts, the most important ones are:

For scoring, license.file needs to be in the Demo2 folder and needs to contain valid DAI license
deploy_dai_pipeline.sh and deploy_sw_pipeline.sh

use: ( so far only dai-pipeline is implemented)

./deploy-dai-pipeline.sh ../Demo1-Training/dai.pipeline/pipeline.mojo ../Demo1-Training/dai.pipeline/mojo2-runtime.jar
