# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which your frontend application will run (if necessary)
EXPOSE 3000

# Run the npm run start:frontend command to start your React/Node.js application
CMD ["npm", "run", "start:frontend"]
