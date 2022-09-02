FROM maven:3.6-jdk-11 as builder

# Copy local code to the container image.
#WORKDIR /app
#COPY pom.xml .
#RUN mvn package -DskipTests
#COPY src ./src

# Build a release artifact.

COPY ./server/target/userbackend-0.0.1-SNAPSHOT.jar .
# Run the web service on container startup.
CMD ["java","-jar","userbackend-0.0.1-SNAPSHOT.jar","--spring.profiles.active=prod"]
