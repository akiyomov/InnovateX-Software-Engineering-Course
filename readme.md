# Django Chatbot with OpenAI Integration

This Django project uses Django REST Framework to provide a simple chatbot API powered by OpenAI's GPT model. Follow these instructions to set up and run the project on your machine.
Prerequisites

### Before you start, ensure you have the following installed:

- Python (3.7 or higher)
- pip (Python package installer)
- Virtual environment (recommended) (venv)

### Installation
1. Clone the Repository

Start by cloning this repository to your local machine:

```
git clone https://github.com/akiyomov/InnovateX-Software-Engineering-Course
```

Checkout mid-term repository

```
git checkout mid-term
```

### 2. Set Up a Virtual Environment
```
python -m venv env

source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Set OPENAI API KEY 
Open settings.py on innovateXapi subdir
then set it

```
OPENAI_API_KEY = 'put api key here'
```

### 5. Migrate Database

Run migrations to set up your database schema:

```
python manage.py migrate
```

### 6. Running the Server

To start the Django server, run:

```
python manage.py runserver 0.0.0.0:3005
```

## Usage

Once the server is running, you can interact with the chatbot by sending POST requests to http://localhost:8000/api/chat/ with a JSON payload containing a message, e.g., {"message": "Hello"}.
Example POST Request

Using curl:

```bash
curl -X POST http://localhost:3005/api/chat/ \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello"}'
```

```bash
curl -X POST http://localhost:3005/api/translate/ \
     -H "Content-Type: application/json" \
     -d '{"message": "Translate this text to french: The quick brown fox jumps over the lazy dog"}'
```


```bash
curl -X POST http://localhost:3005/api/paraphrase/ \
     -H "Content-Type: application/json" \
     -d '{"message": "Paraphrase this text: The quick brown fox jumps over the lazy dog"}'
```

```bash
curl -X POST http://localhost:3005/api/grammar-check/ \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"Correct grammar on this text: The cat lays on the sofa, while it's owner watches television\"}"
```

Using direcly Django Resr Framework UI

`http://0.0.0.0:3005/api/chat/`

`http://0.0.0.0:3005/api/translate/`

`http://0.0.0.0:3005/api/grammar-check/`

`http://0.0.0.0:3005/api/praphrase/`





demo link

[Link](https://drive.google.com/file/d/1ABN3XJ8utuApAnx_z2K2xdrIsgefjWFS/view?usp=sharing)