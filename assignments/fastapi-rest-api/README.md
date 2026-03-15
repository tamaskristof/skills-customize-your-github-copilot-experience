# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI and practice defining routes, handling JSON data, and validating request bodies with Pydantic models.

## 📝 Tasks

### 🛠️	Create the Core API

#### Description
Use FastAPI to build the first version of a homework tracker API. Your API should start a web server, return JSON responses, and expose endpoints that let a client view and create homework items.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Add a `GET /` endpoint that returns a short welcome message in JSON.
- Add a `GET /assignments` endpoint that returns the current list of homework items.
- Add a `POST /assignments` endpoint that accepts a new homework item and adds it to the in-memory list.
- Run successfully with Uvicorn so the interactive API docs are available at `/docs`.
- Example request body for `POST /assignments`:
  ```json
  {
    "title": "Read Chapter 4",
    "course": "Computer Science",
    "due_date": "2026-03-25"
  }
  ```

### 🛠️	Validate and Manage Homework Items

#### Description
Improve the API by adding request validation and endpoints for working with individual homework items. The API should return clear errors when a record does not exist and keep the data format consistent.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming homework data.
- Ensure each homework item has an `id`, `title`, `course`, `due_date`, and `completed` field.
- Add a `GET /assignments/{assignment_id}` endpoint that returns one homework item by ID.
- Add a `PUT /assignments/{assignment_id}/complete` endpoint that marks an item as completed.
- Return a `404` error when the requested homework item does not exist.
- Example response for a completed item:
  ```json
  {
    "id": 1,
    "title": "Read Chapter 4",
    "course": "Computer Science",
    "due_date": "2026-03-25",
    "completed": true
  }
  ```