# GAN-Workplace
A location where I can work on my GAN networks for various uses and experimentation.

# Notes on GANs

Generative adversarial networks (GANs) are a generative models (as per the name). Generative models are able to create unique data and give outputs given some arbitrary encoding. 

## An Overview of GANs

Contain two models.
1. Generator
2. Discriminator / Critic

The role of the generator is to figure out manipulations of the noise to fool the discriminator into believing the data is real instead of generated. The discriminator is designed to decided whether the output is real or generated.

There must be a healthy amount of competition between both the generator and discriminator. Conflicts in this could cause problems when trying to train both of the models and won't lead to realistic generated data.

## Principles of GANs

A GAN is analogous to a counterfeiter and police scenario. At the academy, the police are taught how to determine whether a dollar bill is either genuine or fake. Samples of real dollar bills from the bank and fake money from the counterfeiter are used to train the police. However, from time to time, the counterfeiter will attempt to pretend that he printed real dollar bills. Initially, the police will not be fooled and will tell the counterfeiter why the money is fake. Taking into consideration this feedback, the counterfeiter hones his skills again and attempts to produce new faker dollar bills. As expected, the police will be able to both spot the money as fake and justify why the dollar bills are fake.

This process continues indefinitely, but it will come to a point where the counterfeiter has mastered the creation of fake money to the extent that the fakes are indistinguishable from real money - even to the most highly practiced of police. The counterfeiter can then infinitely print dollar bills without getting caught by the police as they are no longer identifiable as counterfeit.

The input to the generator is noise, and the output is synthesized data. Meanwhile, the discriminator's input will either be real or synthesized data. Genuine data comes from the true sampled data, while the fake data comes from the generator. All of the valid data is labeled 1.0 (that is, a 100% probability of being real), while all the synthesized data is labeled 0.0 (that is, a 0% probability of being real). Since the labeling process is automated, GANs are still considered part of the unsupervised learning approach in DL.