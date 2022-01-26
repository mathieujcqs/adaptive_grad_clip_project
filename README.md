# Adaptive Gradient Clipping VS BatchNorm

This repo is the result of the work done regarding the study of the adaptive gradient clipping (AGC) on the ResNet architectures
It's made out of four folders.

The folder 'comparison_study' contains the networks we used to make a comparison between the AGC, a normalizer-free, and a vanilla ResNet50. Those nets were trained on the CIFAR-10 dataset.
<br />
Then, the folder 'different_netwrok_size' holds the file of different sizes of ResNet architecture implemented with the AGC. Those nets were trained with the CIFAR-10 dataset.
<br />
Following is the folder 'plantclef_nets' contains the same nets as the 'comparison_study' one but this time the nets are trained on the PlantCLEF 2013 dataset.
<br />
Finally, the last folder 'plantclef_preprocess' contains the scripts to transform the data from PlantCLEF 2013 into a usable dataset.

## Implementation of AGC

This work is based on the paper High-Performance Large-Scale Image Recognition Without Normalization and was implemented using Keras thanks to the work of P. Sayak [ 1 ] [ 2 ].

## Citations

[ 1 ] A. Brock, S. De, S. Smith, K. Simonyan (2021). High-Performance Large-Scale Image Recognition Without Normalization.
[ 2 ] P. Sayak, Adaptive Gradient Clipping Repo:https://github.com/sayakpaul/Adaptive-Gradient-Clipping
