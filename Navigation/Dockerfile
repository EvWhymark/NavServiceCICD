FROM eclipse-temurin:21-jdk
EXPOSE 8080
ADD target/Navigation-0.0.1-SNAPSHOT.jar NavService.jar
ENTRYPOINT ["java", "-jar", "NavService.jar"]