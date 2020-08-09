# Fashion Intel

This is the documentation for our solution to Flipkart Grid 2.0 

This documentation contains the explanation of the components used and demos

The trained model weights are hosted on GCP. Run the download_models.sh to use them

### Project Layout

- fashion_intel
    - apis: All the APIs for ML models used by the application
    - cloth_detector: Training and inference codes for the cloth detector
    - fashion2vec: Training and inference codes fashion2vec 
    - pytorch_cnn_trainer: The CNN trainer we built to train our models (Tagger, Fashion2Vec)
    - ranker: The ranking algorithms code
    - tagger: Training and inference codes for fashion tagger

- react_app
    - The code files for our frontend application

- scraper_scripts
    - The webscrapper scripts

