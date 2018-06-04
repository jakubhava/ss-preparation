# Preparation for Spark Summit

 Content:
  - Slides
  - Demo for Training
  - Demo for Scoring

## Training Demo

Demo for Training contains two scripts:

 - ``start_jupiter.sh`` - use to start Jupiter and train Sparkling Water pipeline

 - ``start_dai.sh`` - use to start Driverless AI and create Mojo Pipeline

The folder ``Demo1-Training`` also contains:

 - ``sw.pipeline`` - train Sparkling Water pipeline
 - ``dai.pipeline`` - train Driverless AI pipeline

## Scoring Demo

For Scoring, the following properties needs to be defined, easiest is to put them into ``spark-env.sh`` in your ``$SPARK_HOME/conf`` directory

``AWS_ACCESS_KEY_ID``
``AWS_SECRET_ACCESS_KEY``

### Deploying Driverless AI Pipeline

For scoring, ``license.file`` needs to be in the ``Demo2-Training`` folder and needs to contain valid DAI license

.. code:: bash

	./deploy-dai-pipeline.sh ../Demo1-Training/dai.pipeline/pipeline.mojo ../Demo1-Training/dai.pipeline/mojo2-runtime.jar


### Deploying Sparkling Water Pipeline

.. code:: bash

	./deploy-sw-pipeline.sh ../Demo1-Training/sw.pipeline
