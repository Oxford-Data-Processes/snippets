FROM public.ecr.aws/lambda/python:3.11

RUN yum install -y git

ARG BUILD_DIR

COPY ${BUILD_DIR}/requirements.txt ./

RUN pip install -r requirements.txt

COPY ${BUILD_DIR}/ ./

COPY ./src/models ./models

CMD ["main.lambda_handler"]