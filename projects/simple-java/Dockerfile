#pull a base image which gives all required tools and libraries
FROM openjdk:17-jdk-alpine
#create a folder where the app will be stored
WORKDIR /app
#Copy the source code from your HoST machine to your container
COPY src/Main.java /app/Main.java
#compile the application code
RUN javac Main.java
#run the application
CMD ["java","Main"]
