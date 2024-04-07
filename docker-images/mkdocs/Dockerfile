# mkdocs-material with latest release
FROM python:3-slim

ARG VERSION="x.x.x"


# install mkdocs-material beta (latest release is downloaded in build.sh)
COPY files/mkdocs-material.tar.gz /tmp/mkdocs-material.tar.gz
RUN pip3 install /tmp/mkdocs-material.tar.gz && rm /tmp/mkdocs-material.tar.gz

# install python packages
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt && rm /requirements.txt

# copy example docs
ADD test_docs /docs
RUN chown -R $USERNAME:$USERNAME /docs

RUN echo mkdocs >> /build_date.txt && \
    date >> /build_date.txt

WORKDIR /docs

CMD mkdocs  serve -a 0.0.0.0:8000
