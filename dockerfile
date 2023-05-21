# Use an existing docker image as a base
FROM mysql:8.0

# Install python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install python dependencies
RUN pip3 install requests pandas sqlalchemy pymysql

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=mydb

# Set the working directory
WORKDIR /app

# Copy the script
COPY import_script.py .
COPY wait_and_import.sh .

# Grant permissions for the scripts to be executable
RUN chmod +x import_script.py wait_and_import.sh

# Run the script when container launches
CMD ["./wait_and_import.sh"]
