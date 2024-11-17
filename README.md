# Tax Calculator Project

The **Tax Calculator** is a web-based application designed to compute various types of taxes in India. It aims to simplify tax calculations and provide users with clear, concise, and accurate tax information. The project is built using Python for back-end logic and Flask for creating the web interface, along with HTML templates for presenting tax-related data.

## Features
- **Income Tax Calculator**: Helps users calculate individual income tax based on their salary and other taxable incomes.
- **GST Calculator**: Computes Goods and Services Tax (GST) for different categories and includes detailed GST slabs.
- **Corporate Tax Calculator**: Provides an interface for businesses to calculate corporate tax.
- **Property Tax Calculation**: Enables users to calculate taxes applicable to property ownership.
- **Customs Duty Calculator**: Calculates customs duties for imported goods.
- **Entertainment Tax**: Covers tax rates applicable to entertainment activities like movies and events.
- **Capital Gains Tax**: Helps users determine taxes on profits from investments such as real estate and stock sales.
- **Perquisites Tax Information**: Offers guidance on taxable perquisites received by employees.
- **Security Transaction Tax (STT)**: Calculates taxes applicable to securities trading.
- **Sales Tax Calculator**: Computes sales tax applicable to goods and services.

## Project Structure

### Key Files and Directories
- **`app.py`**: The main entry point for running the Flask application.
- **`templates/`**: Contains HTML templates for various tax types, such as `income_tax.html`, `gst.html`, `property_tax.html`, etc.
- **`static/`**: Holds static assets like CSS, JavaScript, and images (if any).
- **`services.py`**: Includes the business logic and computations for various tax types.
- **`test_service.py`**: Contains test cases to validate the correctness of tax calculations.
- **`TestCases.xlsx`**: A spreadsheet documenting sample test cases and scenarios.
- **`README.md`**: This documentation file explaining the project in detail.

### HTML Pages
- **`index.html`**: The landing page for the Tax Calculator.
- **`TypesOfTaxes.html`**: Overview of different tax categories.
- Individual pages for specific taxes (e.g., `income_tax.html`, `gst.html`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Anirudh1103/Tax-Calculator.git
   cd tax-calculator

2. Create a virtual environment (optional):
    ```bash
    python -m venv env
    source env/bin/activate  # For Linux/macOS
    env\Scripts\activate     # For Windows

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the application:
    ```bash
    python app.py #For windows
    python3 app.py #For Linux/macOS