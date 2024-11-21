# Pull base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1        

# Set work directory
WORKDIR /app

# Install Python dependencies
# Copy just the requirements.txt first to leverage Docker cache
COPY backend/requirements.txt .
RUN pip install python-dotenv
RUN pip install django-cors-headers
RUN pip install mysqlclient
RUN pip install djangorestframework
RUN pip install Pillow
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
# If you have staticfiles or media files consider using .dockerignore to exclude those,
# as they should preferably be handled by a separate web server or service like Whitenoise
COPY backend .

# Expose the port your app runs on
EXPOSE 8000

# # After copying your project
# COPY ./wait-for-it.sh /wait-for-it.sh
# RUN chmod +x /wait-for-it.sh

# # Command to run the wait-for-it script before starting your service
# CMD ["/wait-for-it.sh", "mysql:3306", "--", "python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
