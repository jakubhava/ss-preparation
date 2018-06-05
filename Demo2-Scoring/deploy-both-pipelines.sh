daipipeline=$1
sparkpipeline=$2
mojoruntime=$3
DRIVERLESS_AI_LICENSE_FILE=license.file ../sparkling-water/bin/run-python-script.sh --driver-memory 3G --jars $mojoruntime --packages com.amazonaws:aws-java-sdk:1.7.4,org.apache.hadoop:hadoop-aws:2.7.3  score-both-pipelines.py $daipipeline $sparkpipeline
