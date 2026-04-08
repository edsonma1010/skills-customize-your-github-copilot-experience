# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build RESTful APIs using the FastAPI framework in Python, including creating endpoints, handling requests, and returning responses.

## 📝 Tasks

### 🛠️ Create a Basic API Endpoint

#### Description
Create a simple FastAPI application with a single GET endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Use FastAPI to create an application
- Have a GET endpoint at `/` that returns a JSON response with a welcome message
- Run the server and verify the endpoint works

### 🛠️ Add CRUD Endpoints for Items

#### Description
Extend the API to include CRUD operations for managing a list of items (e.g., products or tasks).

#### Requirements
Completed program should:

- Include POST endpoint to create new items
- Include GET endpoint to retrieve all items or a specific item by ID
- Include PUT endpoint to update an item by ID
- Include DELETE endpoint to remove an item by ID
- Use Pydantic models for request/response validation
- Store items in memory (list or dictionary)