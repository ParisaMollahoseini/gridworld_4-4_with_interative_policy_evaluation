# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:44:36 2020

@author: Soheil_Pc
"""
import numpy as np
class my_ai:
    
    def __init__(self,landa):

        self.grid_v = np.zeros((4,4))
        
        
        
        
        self.actions = [0,1,2,3]#up,down,left,right
        
        self.s_chosen = [(-1,0),(1,0),(0,-1),(0,1)]
        
        self.pr_actions = [0.25,0.25,0.25,0.25]#all action probs are equal
        
        self.pr_states_by_action = np.array((4,4))
        
        self.pr_states_by_action = [[0.5,0,0.25,0.25],#up
                               [0,0.5,0.25,0.25],#down
                               [0.25,0.25,0.5,0],#left
                               [0.25,0.25,0,0.5]]#right
        
        self.R_immediate = -1#for each iteration 
        self.landa = 0.5
        
        for k in range(10):
            for i in range(4):
                for j in range(4):
                    if ((i==0 and j==0 )or (i==3 and j==3)):
                        self.grid_v[i][j] = 0
                    else:
                        self.grid_v[i][j] = np.sum([self.pr_actions[act]*(np.sum([(self.pr_states_by_action[act][s]*(self.R_immediate+self.landa*self.grid_v[self.build_s_index(self.s_chosen[s],i,j)])) for s in range(4)])) for act in range(4)])
                    
            print("...................................")
            print("k={}".format(k))
            np.set_printoptions(precision=3)
            print("gridworld:\n",self.grid_v)
            print("...................................")        
    def build_s_index(self,s,i,j):
        if s[0]+i >= 4:
            x = i
        elif s[0]+i<0:
            x = i
        else:
            x = s[0]+i
        if s[1]+j>=4:
            y = j
        elif s[1]+j<0:
            y = j
        else:
            y = s[1]+j
        return (x,y)
    def run(self,start_point):
        self.grid_s = np.zeros((4,4))
        self.start_point = start_point
        self.grid_s[start_point] = 1
        
        counter = 1
        
        flag = True
        while flag:
            
            print("route of object")
            print(self.grid_s)
            
            if self.start_point[0]==0:
                v_up = -1000
                v_down = self.grid_v[self.start_point[0]+1][self.start_point[1]]
            elif self.start_point[0]==3:
                v_down = -1000
                v_up = self.grid_v[self.start_point[0]-1][self.start_point[1]]
            else:
                v_down = self.grid_v[self.start_point[0]+1][self.start_point[1]]
                v_up = self.grid_v[self.start_point[0]-1][self.start_point[1]]
        
            if self.start_point[1]==0:
                v_left = -1000
                v_right = self.grid_v[self.start_point[0]][self.start_point[1]+1]
            elif self.start_point[1]==3:
                v_right = -10000
                v_left = self.grid_v[self.start_point[0]][self.start_point[1]-1]
            else:
                v_right = self.grid_v[self.start_point[0]][self.start_point[1]+1]
                v_left = self.grid_v[self.start_point[0]][self.start_point[1]-1]
                
            max_v = np.argmax([v_up,v_down,v_left,v_right])
            #print(max_v)
            if np.all(np.sum([self.s_chosen[max_v],self.start_point],0)==(0,0)) or np.all(np.sum([self.s_chosen[max_v],self.start_point],0)==(3,3)):
                counter = counter + 1
                self.grid_s[tuple(np.sum([self.s_chosen[max_v],self.start_point],0))] = counter
                flag = False
            else:
                counter = counter + 1
                self.grid_s[tuple(np.sum([self.s_chosen[max_v],self.start_point],0))] = counter
                self.start_point = np.sum([self.s_chosen[max_v],self.start_point],0)
                    
                    
            
            #flag = False
        print("route of object")
        print(self.grid_s)