
---

# FoodEx - Online Food Ordering System

**Author:** Eproject Sem-3  
**Date:** 18th January 2024

**Table of Contents:**
- [Description](#description)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

**Description:**

FoodEx is an Online Food Ordering System designed to simplify the process of food ordering for both restaurants and customers. This Python project empowers restaurant owners to showcase their menus online, and customers to conveniently place orders through a user-friendly web interface.

## Database Setup

To get started with FoodEx, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/foodex.git
   cd foodex
   ```

2. Set up the virtual environment (optional but recommended):

   ```bash
   virtualenv venv
   source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
   ```

3. Install dependencies:

   ```bash
   pip install -r config.txt
   ```

4. Run the database setup script:

   ```bash
   python database.py
   ```

   This script initializes the database tables, ensuring your FoodEx application is ready for use.

5. Run the application:

   ```bash
   python app.py
   ```

## Usage

1. Visit `http://localhost:5000` in your web browser.
2. Explore the menu, register, and place orders seamlessly with FoodEx.

**Contributing:**

We welcome contributions to enhance the FoodEx experience. To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

**License:**

This project is licensed under the [MIT License](LICENSE).

---
