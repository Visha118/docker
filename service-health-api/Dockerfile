#1. Base image: provides JDK, maven, Java Runtime
FROM maven:3.9-eclipse-temurin-17

#2. Set working directory inside container
WORKDIR /app

#3. Copy everything from current build context to current working directory (source code, pom.xml)
COPY . .

#4. Build this project into a jar
RUN mvn clean package

#4. Command to run when container starts
ENTRYPOINT ["java", "-jar", "target/service-health-api-0.0.1-SNAPSHOT.jar"]
