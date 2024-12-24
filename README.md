
# Sentiment Analysis on Jetson Nano

This repository hosts a multilingual sentiment analysis project implemented for Jetson Nano. The project performs sentiment analysis using a pre-trained model, detects the input text's language, and provides an audio response with sentiment details.

## Features

- **Sentiment Analysis**: Detects if the sentiment is positive, negative, or neutral using Hugging Face's `transformers` library.
- **Language Detection**: Supports English (`en`), French (`fr`), and Spanish (`es`) for responses.
- **Audio Output**: Generates an audio response with the sentiment result and additional information such as the current date and confidence score.

## Prerequisites

Before running the project, ensure the following are set up on your Jetson Nano:

- Python 3.6 or later
- JetPack SDK installed
- Network connection for initial setup

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/sentiment-analysis-jetson-nano.git
   cd sentiment-analysis-jetson-nano
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Required Libraries**:
   - `transformers`
   - `langdetect`
   - `gTTS`
   - `mpg321` (for audio playback)

   To install `mpg321` on Jetson Nano, use:
   ```bash
   sudo apt-get install mpg321
   ```

4. Verify the installation:
   ```bash
   python3 -c "import transformers, langdetect, gtts"
   ```

## Running the Project

1. Navigate to the project directory:
   ```bash
   cd sentiment-analysis-jetson-nano
   ```

2. Run the script:
   ```bash
   python3 sentiment_analysis.py
   ```
