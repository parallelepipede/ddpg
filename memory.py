#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:01:05 2021

@author: paul
"""

import numpy as np
from collections import deque

class ReplayBuffer:
    def __init__(self,buffer_size,batch_size):
        """
        ReplayBuffer contains tuples with : 
            - current state 
            - action 
            - reward
            - next state
        """
        self.buffer_size = int(buffer_size)
        self.replay_buffer = deque(maxlen=self.buffer_size)
        self.batch_size = batch_size
        
    def append(self,state,action,reward,next_state):
        self.replay_buffer.append([state,action,np.expand_dims(reward,-1),next_state])
        
        
    def get_batch(self):
        #np.random.shuffle(self.replay_buffer)
        #self.replay_buffer[:self.batch_size]
        print()
        print(self.replay_buffer, " dans memory get_batch")
        print()
        #return np.random.choice(self.replay_buffer,size=min(len(self.replay_buffer),self.batch_size))
        indexes = np.random.choice(len(self.replay_buffer), size = min(len(self.replay_buffer), self.batch_size))
        print()
        print([self.replay_buffer[index] for index in indexes], "dans memory get_batch, replay-buffer index")
        print()
        return [self.replay_buffer[index] for index in indexes]
    
    def reset(self):
        self.replay_buffer = deque(maxlen=self.buffer_size)
    
    
    
        
        
        