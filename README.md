# GAN-Workplace
A location where I can work on my GAN networks for various uses and experimentation.

# Notes on GANs

Generative adversarial networks (GANs) are a generative models (as per the name). Generative models are able to create unique data and give outputs given some arbitrary encoding. 

## An Overview of GANs

Contain two models.
1. Generator
2. Discriminator / Critic

The role of the generator is to figure out manipulations of the noise to fool the discriminator into believing the data is real instead of generated. The discriminator is designed to decided whether the output is real or generated.

There must be a healthy amount of competition between both the generator and discriminator. Conflicts in this could cause problems when trying to train both of the models and won't lead to 