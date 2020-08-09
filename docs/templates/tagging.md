# Fashion Tagging

## Overview

Visual features are enough for the models to identify trend and rank them. However they are not interpretable.
We developed a fashion tagging model which can tag images with fashion attributes, there are about 1000 tags in the training dataset we used

Tagging can help the user interpret the results of the ranking algorithm much better
Dashboards can be made where highly ranked fashion images and their corresponding tags can be used to give insightful plots

Moreover these tags can also be used for textual search, where the user can search whether a particular fashion is in trend
by using words.


## Dataset

We used DeepFashion Attribute prediction dataset. This dataset had about 280,000 images belonging to 5000 classes, each class had its own unique fashion style

## Training

### Model

We used ResNet model as the backbone, the last layer was a 1000 units linear layer with sigmoid activation function.

### Loss 

We used the cross entropy loss


### Scope For Improvement

We can make make an end-to-end model with bbox regressor and attribute classifier to improve the accuracy of the model.