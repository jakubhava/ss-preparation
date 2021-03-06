# Copyright 2018 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

-------------------------------------------------------------------------------

                H2O DRIVERLESS AI STANDALONE MOJO SCORING PIPELINE


                           PROPRIETARY LICENSE -

                USE OF THIS SCORING PIPELINE REQUIRES A VALID,
                ONGOING LICENSE AGREEMENT WITH H2O.AI.

                Please contact sales@h2o.ai for more information.

-------------------------------------------------------------------------------

This folder contains a MOJO pipeline and Java runtime for deploying models
built with H2O Driverless AI. It enables low-latency, high-throughput scoring
on a broad range of hardware/software platforms with minimal requirements.

-------------------------------------------------------------------------------
REQUIREMENTS:

  - Java 8 runtime
  - Valid Driverless AI license

-------------------------------------------------------------------------------
DIRECTORY LISTING:

  run_example.sh            An bash script to score a sample test set.

  pipeline.mojo             Standalone scoring pipeline in MOJO format.

  mojo2-runtime.jar         MOJO Java runtime.

  example.csv               Sample test set (synthetic, of the correct format).

-------------------------------------------------------------------------------
QUICKSTART:

To score all rows in the sample test set (`example.csv`) with the MOJO pipeline (`pipeline.mojo`),
and license stored in environment variable `DRIVERLESS_AI_LICENSE_KEY`:

    $ bash run_example.sh

To score a specific test set `example.csv` with MOJO pipeline `pipeline.mojo` and license file:

    $ bash run_example.sh pipeline.mojo example.csv license.sig

To run Java application for MOJO scoring directly:

   $ java -cp license.sig:mojo2-runtime.jar ai.h2o.mojos.ExecuteMojo pipeline.mojo example.csv

-------------------------------------------------------------------------------
LICENSE SPECIFICATION

The license can be specified in the following ways:
  * Via an environment variable:
    - 'DRIVERLESS_AI_LICENSE_FILE' : Path to the Driverless AI license file, or
    - 'DRIVERLESS_AI_LICENSE_KEY'  : The Driverless AI license key (Base64 encoded string)
  * Via a system property of JVM ('-D' option):
    - 'ai.h2o.mojos.runtime.license.file' : Path to the Driverless AI license file, or
    - 'ai.h2o.mojos.runtime.license.key'  : The Driverless AI license key (Base64 encoded string)
  * Via application classpath
    - The license is loaded from resource called '/license.sig'
    - The default resource name can be changed via the JVM system property 'ai.h2o.mojos.runtime.license.filename'

For example:
    $ java -Dai.h2o.mojos.runtime.license.file=/etc/dai/license.sig -cp mojo2-runtime.jar ai.h2o.mojos.ExecuteMojo pipeline.mojo example.csv

