FROM python:3.9-slim-buster

WORKDIR /app
USER root

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install

COPY . .

ENTRYPOINT ["pytest", "--playwright", "--browser=chromium"]
CMD ["kivi_playwright/"]