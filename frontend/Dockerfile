FROM node:18-alpine

# set work directory
ENV FRONTEND_APP_HOME=/usr/src/app/frontend
WORKDIR $FRONTEND_APP_HOME

RUN apk add libc6-compat

COPY ./package.json ./package-lock.json $FRONTEND_APP_HOME

# Install dependencies
#RUN npm install --production
RUN npm install

# Copy all files
COPY . $FRONTEND_APP_HOME

# Build app
#RUN npm run build

# Expose the listening port
EXPOSE 3000

# Run npm start script when container starts
#CMD [ "npm", "start" ]
CMD [ "npm", "run", "dev" ]