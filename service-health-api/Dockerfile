# ---------- Stage 1: Build -------------
FROM maven:3.9-eclipse-temurin-17 AS builder

WORKDIR /build

# Copy pom.xml (dependency caching)
COPY pom.xml .

RUN mvn dependency:go-offline

# Copy source code
COPY src ./src

# Build the jar
RUN mvn clean package

# ------------ Stage 2: Runtime ----------

#1. Base image: Java Runtime
FROM eclipse-temurin:17-jre

#2. Set working directory inside container
WORKDIR /app

#3. Copy jar from builder stage
COPY --from=builder /build/target/service-health-api-0.0.1-SNAPSHOT.jar app.jar

#4. Command to run when container starts
ENTRYPOINT ["java", "-jar", "app.jar"]
