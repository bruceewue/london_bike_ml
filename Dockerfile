# Dockerfile

# FROM python:3.10-buster
# WORKDIR /app
# COPY . /app
# RUN pip install fastapi uvicorn pandas xgboost

# EXPOSE 8000
# CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]


FROM public.ecr.aws/lambda/python:3.10

WORKDIR /var/task


COPY lambda_function.py .
COPY model.pkl .


RUN python3 -m pip install --upgrade pip
RUN pip install pandas scikit-learn


CMD ["lambda_function.lambda_handler"]