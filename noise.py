#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:02:21 2021

@author: paul
"""

import numpy as np

class OrnsteinUhlenbeckActionNoise(object):
    # Comes from Open AI library : https://github.com/openai/baselines/blob/master/baselines/ddpg/noise.py
    def __init__(self,mu,sigma=.2,theta=.15,dt=1e-2,x0=None):
        self.theta = theta
        self.mu = mu
        self.dt = dt
        self.x0 = x0
        self.sigma = sigma
        self.reset()
    
    def reset(self):
        self.x_prev = self.x0 if self.x0 is not None else np.zeros_like(self.mu)
        
    def __repr__(self):
        return f'OrnsteinUhlenbeck(mu={self.mu},sigma={self.sigma})'
    
    def __call__(self):
        # noise = OrnsteinUhlenbeckActionNoise()
        # ourNoise = noise() -> __call__ is called
        x = self.x_prev  + self.theta * (self.mu - self.x_prev) * self.dt + self.sigma * np.sqrt(self.dt) * np.random.normal(size = self.mu.shape)
        self.x_prev = x
        return x

    
class GaussianNoise(object):
    
    def __init__(self,mu,sigma):
        self.mu = mu
        self.sigma = sigma
        
    def reset(self):
        pass
    
    def __repr__(self):
        return f'Gaussian(mu={self.mu},sigma = {self.sigma})'
    
    def __call__(self):
        return np.random.normal(self.mu,self.sigma)
    
    
class AdaptativeNoise(object):
    #TODO reduce the scale of the noise over the course of training. To test : reduction and augmentation of both parameters
    # Add adaptative noise depending on std evolution
    # Add noise at the end of learning too
    def __init__(self,mu,sigma,change_threshold,adjustment_coefficient):
        self.mu = mu
        self.sigma = sigma
        self.change_threshold = change_threshold
        
    
    def adapt(self,n_steps):
        if n_steps > self.change_threshold:
            self.mu /= self.adjustment_coefficient
        else:
            self.mu *= self.adjustment_coefficient
        
    def __call__(self):
        return np.random.normal(self.mu,self.sigma)
    
    def reset(self):
        pass
    
    
    
    
    
    