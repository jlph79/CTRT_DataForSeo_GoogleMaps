# DataForSEO Google Maps Data Collection

## Overview

This repository contains a Python script for collecting data from the Google Maps API using the DataForSEO platform. The script submits tasks to the DataForSEO API, processes the responses, and saves the output as a raw JSON file. This repository is designed for educational purposes, specifically for students learning about data science and API integration.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Script Flow](#script-flow)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following:

1. **Python**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
2. **API Key**: Obtain an API key from DataForSEO. Sign up at [DataForSEO](https://dataforseo.com/) to get your API key.
3. **Libraries**: Install the required Python libraries.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/jlph79/CTRT_DataForSeo_GoogleMaps
    cd dataforseo-google-maps
    ```

2. **Install Required Libraries**

    Install the necessary Python libraries using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Elke DataForSEO gebruiker heeft een 'account' en een uniek wachtwoord dat door DataForSEO gegenereerd wordt. Dit is niet hetzelfde wachtwoord als je wachtwoord voor inloggen in de DataForSEO portal. De account en API wachtwoord kun je terugvinden in het DataForSEO dashboard. Voor de documentatie van de API endpoints, kun je terecht op [DataForSEO API Documentation](https://docs.dataforseo.com/v3/serp/google/overview/?bash&_gl=1*eo9o81*_up*MQ..*_ga*MTUwMjUyMjQ5NC4xNzE4MzY1Njk1*_ga_T5NKP5Y695*MTcxODM2NTY5NC4xLjEuMTcxODM2NjkwMC4wLjAuMTE1OTcwMDQwNA..).

1. **Configure API Key**

    Open the `GoogleMapsEndPoint_raw.py` file and replace `'your_api_key_here'` with your actual DataForSEO API key.

    ```python
        RestClient = RestClient("your_account@example.com", "xxxxxxxxxxx") 
    ```

2. **Run the Script**

    Execute the script to start collecting data:

    ```bash
    python GoogleMapsEndPoint_raw.py
    ```

3. **Output**

    The script will generate a raw JSON file containing the collected data.

## Script Flow

The following flowchart illustrates the script flow:

1. **Initialize RestClient**
2. **Create RestClient Object**
3. **Submit Google Maps Task**
4. **Post Task to DataForSEO API**
5. **Task Submission Response**
   - **Success**: Extract Task IDs and wait for task completion
   - **Failure**: Log error and exit
6. **Check Task Status**
   - **Completed**: Save data to JSON file
   - **In Queue or Processing**: Wait and retry
   - **Error**: Log error and exit

For a detailed understanding, refer to the `GoogleMapsEndPoint_raw.py` script and the accompanying flowchart.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

 
