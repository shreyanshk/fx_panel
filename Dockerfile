FROM alpine:3.6
RUN apk update
RUN apk add python3
# nodejs nodejs-npm
# RUN /usr/bin/npm --global install node-sass babel-cli babel-preset-env
ADD requirements.txt /
RUN pip3 install -r /requirements.txt
ADD . /app/
# compile sass and babel files
# RUN /usr/bin/node-sass /app/src/sass -o /app/static/css &&\
# /usr/bin/babel --no-babelrc /app/src/es6 -d /app/static/js &&\
# rm -rf /app/src &&\
# echo " ---> Finished preprocessing SASS and ES6"
# done compiling
EXPOSE 5000
CMD ["python3", "/app/fx_panel.py"]
