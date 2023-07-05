FROM python:3.10-buster

# Install Chrome dependency for selenium crawling
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get install -yq google-chrome-stable

# Copy files
COPY . /app
WORKDIR /app

# Install Python requirements
RUN pip install -r requirements.txt

# Add non-root user
RUN groupadd -g 20010 -r appuser && useradd -r -m -u 10010 -g appuser -d /home/appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# Default endpoint
ENTRYPOINT [ "python", "-u", "./main.py" ]