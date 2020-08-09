# Fashion2Vec 


## Overview

Fashion2Vec is essentially a CNN (in our case ResNet) which is trained using supervised contrastive learning method
this allows the CNN to generate very accurate feature representations of the fashion Images

## Dataset

We used DeepFashion Attribute prediction dataset. This dataset had about 280,000 images belonging to 5000 classes, each class had its own unique fashion style

## Training

### Triplet Sampling

We sampled triplets from this dataset to give as input to image
The triplets contained 
- An anchor image from a class
- A positive image which belongs to same class as anchor image 
- A negative image which belongs to a different class

### Loss 

We used the triplet margin loss available in PyTorch

### Method

Each image is individually passed through the CNN, note that for each triplet, the CNN has same weight
The embeddings after the last GlobalAveragePooling layer is taken and triplet loss is computed for triplets

### Scope For Improvement

We could use quadruplet loss, which has soft positive and hard positive, the semantics of the class names can be used to identify soft positive and hard positive classes