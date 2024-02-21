# LIHKG Scraper

The LIHKG Scraper is a Python-based tool designed to extract posts from the LIHKG forums. It leverages the power of Selenium, BeautifulSoup, and Pandas to navigate, parse, and analyze the webpage content efficiently.

## Features

- **Scrape by Range**: Easily target a series of posts by specifying a start and end point.
- **Comprehensive Data Extraction**: Capture various data such as post title, content, comments, and more.
- **CSV Export**: Quickly save the scraped content into a CSV file, simplifying the process of later use and data analysis.

## Installation

Ensure you have Python 3.6 or later installed on your machine. After cloning the repository or downloading the project, follow these steps to set up your local development environment.

### Prerequisites

- Python 3.6+
- Firefox Browser
- The necessary Python libraries are listed in `requirements.txt` and can be installed using the steps provided below.

### Environment Set Up

1. **Clone the repository** or **Download the source code**:

    ```
    git clone https://github.com/s1296322/LIHKG_scraper
    ```

2. **Navigate to the project directory**:

    ```
    cd lihkg_scraper
    ```

3. **Install the required Python libraries**:

    ```
    pip install -r requirements.txt
    ```

### Installing Firefox WebDriver

- **Geckodriver** (Firefox WebDriver) is required for Selenium to interface with the Firefox browser.

For further details on configuring Geckodriver, please refer to the [Selenium documentation](https://www.selenium.dev/documentation/en/).

## Usage

After completing the setup process, you're ready to use the scraper. Run the scraper using the script as shown below:

```bash
python lihkg_scraper.py --start [start_post_number] --end [end_post_number] --output [output_filename.csv] --headless [True/False]
