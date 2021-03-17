FROM python:3.8 AS builder
COPY requirements.txt .
# INSTALL DEPENDENCIES
RUN pip install --user -r requirements.txt

FROM python:3.8-slim
WORKDIR /code
RUN mkdir -p /root/.local/lib/python3.8/site-packages
COPY --from=builder /root/.local/lib/python3.8/site-packages/ /root/.local/lib/python3.8/site-packages/
COPY --from=builder /root/.local/bin /root/.local
COPY run.py run.py
COPY backend/ backend/
ENV PATH=/root/.local:$PATH
ENV PYTHONPATH=.
# START COMMAND
CMD [ "python", "run.py" ]