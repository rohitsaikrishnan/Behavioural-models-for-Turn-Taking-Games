import random
import numpy as np
import matplotlib.pyplot as plt

def PlayerPayoffs(node):
    if node==1:
        return [3,1]
    if node==2:
        return [2,1]
    if node==3:
        return [4,1]
    if node==4:
        return [5,1]
    if node==5:
        return [6,1]


def prob_distribution(level):
    if level==0:
        return [0.5,0.5,0.5,0.5]
    prob_dist=[]
    prob_dist_level=prob_distribution(level-1)
    node4=0
    forward_payoff_3=prob_dist_level[3]*PlayerPayoffs(5)[1]+(1-prob_dist_level[3])*PlayerPayoffs(4)[1]
    node3=(np.exp(forward_payoff_3))/(np.exp(forward_payoff_3)+np.exp(PlayerPayoffs(3)[0]))
    forward_payoff_2=prob_dist_level[2]*(node4*PlayerPayoffs(5)[0]+(1-node4)*PlayerPayoffs(4)[0])+(1-prob_dist_level[2])*PlayerPayoffs(3)[1]
    node2=(np.exp(forward_payoff_2))/(np.exp(forward_payoff_2)+np.exp(PlayerPayoffs(2)[0]))
    forward_payoff_1=(1-prob_dist_level[1])*PlayerPayoffs(2)[1]+((prob_dist_level[1])*((1-node3)*PlayerPayoffs(3)[0]+node3*(prob_dist_level[3]*PlayerPayoffs(5)[1]+(1-prob_dist_level[3])*PlayerPayoffs(4)[1])))
    node1=(np.exp(forward_payoff_1))/(np.exp(forward_payoff_1)+np.exp(PlayerPayoffs(1)[0]))
    return [node1,node2,node3,node4]


def gameMove(node,probability):
    if node==5:
        return 0
    else:
        if random.random() < probability:
            return node+1
        else:
            return 0
def gamePlay():
    mu, sigma=0, 0.1
    normal_dist=np.random.normal(mu, sigma, 2)
    normal_dist_1=normal_dist[0]
    normal_dist_2=normal_dist[1]
    if normal_dist_1 < mu + sigma and normal_dist_1 > mu - sigma:
        level_1=1
    elif normal_dist_1 < mu-sigma:
        level_1=0
    else:
        level_1=2
    mu, sigma = 0, 0.01
    if normal_dist_2 < mu + sigma and normal_dist_1 > mu - sigma:
        level_2 = 1
    elif normal_dist_1 < mu - sigma:
        level_2 = 0
    else:
        level_2 = 2
    final_utility=[]
    Prob_player1=prob_distribution(level_1)
    Prob_player2=prob_distribution(level_2)
    node=1
    while True:
        if node==5:
            final_utility=[PlayerPayoffs(5)[1],PlayerPayoffs(5)[0]]
            break
        elif node%2!=0:
            game_decision=gameMove(node,Prob_player1[node-1])
            if game_decision:
                node=node+1
            else:
                final_utility=[PlayerPayoffs(node)[0], PlayerPayoffs(node)[1]]
                break
        else:
            game_decision=gameMove(node,Prob_player2[node-1])
            if game_decision:
                node=node+1
            else:
                final_utility=[PlayerPayoffs(node)[1], PlayerPayoffs(node)[0]]
                break
    if level_2==level_1:
        Utility[level_1].append(np.mean([final_utility[0],final_utility[1]]))
    else:
        Utility[level_1].append(final_utility[0])
        Utility[level_2].append(final_utility[1])


mean_0=0
mean_1=0
mean_2=0
Utility = [[],[],[]]
Utility_mean=[[],[],[]]
Iterations=[]
for i in range(6000):
    gamePlay()
    if i%500==0 and i!=0:
        Iterations.append(i)
        for j in range(3):
            Utility_mean[j].append(np.mean(Utility[j]))

        print (np.mean(Utility[0]), np.mean(Utility[1]), np.mean(Utility[2]))
plt.plot(Iterations,Utility_mean[0],color='blue', label='level-0')
plt.plot(Iterations,Utility_mean[1],color='red', label='level-1')
plt.plot(Iterations,Utility_mean[2],color='black', label='level-2')
plt.xlabel('# of games')
plt.ylabel(('Average Utilities'))
plt.title('Average Utilities of players')
plt.legend()
plt.grid()
plt.show()













