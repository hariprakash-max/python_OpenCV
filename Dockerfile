FROM ubuntu:latest
LABEL authors="mnhar"

ENTRYPOINT ["top", "-b"]