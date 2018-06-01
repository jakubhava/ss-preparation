docker run -it --rm --init -u $(id -u):$(id -g) -p 12345:12345 -v $(pwd)/tmp:/tmp -v $(pwd)/log:/log docker.h2o.ai/opsh2oai/h2oai-runtime:1.1.3
