# Movie Rating API

This is a simple Flask-based REST API for managing movie ratings. It allows users to add new movies with ratings and retrieve movie information.

## Features

- Add new movies with name and rating
- Retrieve movie information
- Automatic ranking of movies based on addition order

## Requirements

- Python 3.6+
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Requests (for testing)

## Installation

1. Clone this repository:
  git clone https://github.com/yanirhaim/movie-rating-api.git
  cd movie-rating-api

2. Create a virtual environment (optional but recommended)

3. Install the required packages:
   pip install -r requirements.txt


## Usage
1. Start the Flask application:
   python app.py
 2. The API will be available at `http://localhost:5000`

## API Endpoints

- `PUT /movie/<name>`: Add a new movie
- Request body: `{ "name": "Movie Name", "rate": 8 }`
- `GET /movie/<name>`: Retrieve movie information

## Testing

A test script is provided to check various API functionalities. To run the tests:

1. Ensure the Flask application is running
2. Run the test script:
    python test_api.py
