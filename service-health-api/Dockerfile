#1. Base image: provides Java Runtime
FROM eclipse-temurin:17-jre

#2. Set working directory inside container
WORKDIR /app

#3. Copy the executable JAR from host to container
COPY target/service-health-api-0.0.1-SNAPSHOT.jar app.jar

#4. Command to run when container starts
ENTRYPOINT ["java", "-jar", "app.jar"]
