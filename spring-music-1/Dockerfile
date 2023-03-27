FROM openjdk:8-jdk as server

COPY /build/libs/spring-music-1.0.jar /app/spring-music.jar
COPY start.sh /app/
EXPOSE 8080
ENV PORT 8080

WORKDIR /app

ENTRYPOINT ["/app/start.sh"]
