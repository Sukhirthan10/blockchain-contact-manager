# Blockchain Contact App

A simple contact management application that utilizes blockchain technology to securely store and manage user contact information. Each contact's name and phone number are encrypted and added to a blockchain, ensuring privacy and data integrity.

## Features

- Add contacts with names and phone numbers.
- Encrypt contact data before storing it in the blockchain.
- View the blockchain with details about each contact.
- Retrieve and decrypt contact information.

## Technologies Used

- Python
- Flask (Web Framework)
- PyCryptodome (Encryption)
- HTML/CSS (Frontend)

## Installation

### Prerequisites

Make sure you have Python 3.6 or higher installed on your machine. You'll also need `pip` to install the necessary packages.

### Steps to Set Up

1. **Clone the Repository**:

   Using the download clone on the website

2. **Create a Virtual Environment (optional but recommended)**:

   python -m venv venv  
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`  

3. **Install Dependencies**:

   pip install -r requirements.txt  

## Usage

1. **Run the Application**:

   python app.py  

   The application will start on `http://127.0.0.1:5000`.

2. **Access the Application**:

   Open your web browser and go to `http://127.0.0.1:5000` to access the contact app.

3. **Add a Contact**:

   - Fill in the contact name and phone number.
   - Click on "Add Contact" to save the information securely in the blockchain.

4. **View Blockchain**:

   Click the option to view the blockchain to see all added contacts and their encrypted data.

5. **Retrieve and Decrypt Data**:

   Select a block to view the decrypted name and phone number.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Inspired by blockchain technology and secure data storage practices.
