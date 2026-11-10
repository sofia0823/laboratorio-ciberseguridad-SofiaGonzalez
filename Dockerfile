FROM python:alpine
WORKDIR /app
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
EXPOSE 8080
CMD ["/bin/sh", "/app/entrypoint.sh"]
