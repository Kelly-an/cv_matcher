# Use the official MongoDB image as the base
FROM mongo:latest

# Set environment variables (optional)
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=rootpassword

# Expose MongoDB's default port
EXPOSE 27017

# Copy any custom initialization scripts if needed (optional)
# COPY ./init-mongo.js /docker-entrypoint-initdb.d/

# Volumes for persistent data
VOLUME ["/data/db"]

# The default entrypoint is already set by the MongoDB image
# so we don't need to add a CMD or ENTRYPOINT

# Run MongoDB as the default process
CMD ["mongod"]
