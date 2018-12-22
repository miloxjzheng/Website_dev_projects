#!/bin/bash
build_img(){
   CURRENT_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
   env=$1
   cd $CURRENT_DIR/.. && \
   mvn clean && \
   mvn compile && \
   mvn package -DskipTests && \
   if test ${env} ="dev"
   then
       java -jar target/token72.jar
       echo "Building done！"
   elif test ${env} = "test"
   then
      java -jar target/token72.jar --spring.profiles.active=${env}
      echo "Building done！"
   elif test ${env} = "prod"
   then
      nohup java -jar target/token72.jar --spring.profiles.active=${env}&
      echo "Building done！"
   else
      echo 'Wrong parameter!'
   fi
}
echo "********************Building token72 program in ${1} mode************************"
ENV=$1
case ${ENV} in
    "dev")
        build_img dev
        ;;
    "test")
        build_img test
        ;;
    "prod")
        build_img prod
        ;;
    *)
        build_img dev
        ;;
esac
