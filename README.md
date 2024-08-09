# Document Query and History Management App

This is a Streamlit-based web application that allows users to upload documents, query them, and retrieve relevant information. The application securely stores data in a database, maintains user history, and provides the option to download chat history in PDF format.

## Features

- **User Authentication**: Users can register and log in to the application securely.
- **Document Upload**: Supports uploading of `.pdf`, `.docx`, and `.txt` files.
- **Querying Documents**: Users can ask questions about the content of the uploaded documents, and the application will provide relevant answers.
- **User History**: Maintains a record of user interactions, including queries and responses.
- **Download Chat History**: Users can download their chat history in a PDF format.
- **Multi-Page Navigation**: Clean and user-friendly interface with multiple pages for login, document querying, and logout.

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ninja-whale/Document-Query-App.git
   cd document-query-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   streamlit run main.py
   ```

## Usage

### 1. Authentication

- **Registration**: New users can register by providing a username and password.
- **Login**: Registered users can log in using their credentials. Successful login redirects to the document query page.

### 2. Document Upload and Querying

- After logging in, users can upload documents in `.pdf`, `.docx`, or `.txt` format.
- The uploaded document's text content is extracted, and users can then input queries to retrieve relevant information from the document.

### 3. Viewing and Downloading History

- Users can view their query history on the same page.
- An option is provided to download the chat history as a PDF file.

### 4. Logout

- Users can log out from the application, which will clear the session and redirect to the login page.

## Database

- The application uses SQLite to manage user authentication and query history.
- **Users Table**: Stores usernames and hashed passwords.
- **User History Table**: Stores user queries, responses, and timestamps.

## Security

- Passwords are securely hashed using `bcrypt`.
- User history and interactions are protected, ensuring that each user's data is only accessible to them.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs, feature requests, or suggestions.


