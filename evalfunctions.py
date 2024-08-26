import numpy as np


def random_importance(state):
  return np.random.uniform(-100, 100, 1)[0]



def dominate_player(state, i_candidates, j_candidates):
  freq = [0,0,0]

  if i_candidates[-1] >= state.row or j_candidates[-1] >= state.col or i_candidates[0] < 0 or j_candidates[0] < 0 or j_candidates[-1] < 0 or j_candidates[0] >= state.col:
    return None, None
  
  for i,j in zip(i_candidates, j_candidates):
    freq[state.board[i][j]] += 1
  
  if (freq[1] > 0 and freq[2] > 0) or freq[0] == 4:
    return None, None
  
  if freq[1] > 0:
    return 1, 4-freq[1]-1

  return 2, 4-freq[2]-1
  

def sliding_opp(state):
  player_scores = [0, 0, 0]
  cpu_scores = [0, 0, 0]

  #row and column advantages
  for i in range(state.row):
    for j in range(state.col):
      player, val = dominate_player(state,[i,i+1,i+2,i+3], [j]*4)
      if player == 1:
        player_scores[val] += 1
      elif player == 2:
        cpu_scores[val] += 1
      
      player, val = dominate_player(state,[i]*4,[j,j+1,j+2,j+3])
      if player == 1:
        player_scores[val] += 1
      elif player == 2:
        cpu_scores[val] += 1
      
      player, val = dominate_player(state,[i,i+1,i+2,i+3],[j,j+1,j+2,j+3])
      if player == 1:
        player_scores[val] += 1
      elif player == 2:
        cpu_scores[val] += 1
      
      player, val = dominate_player(state,[i,i+1,i+2,i+3],[j+3,j+2,j+1,j])
      if player == 1:
        player_scores[val] += 1
      elif player == 2:
        cpu_scores[val] += 1


  player_scores[0] *= 110
  cpu_scores[0] *= -100
  player_scores[1] *= 55
  cpu_scores[1] *= -50
  player_scores[2] *= 11
  cpu_scores[2] *= -10

  return sum(player_scores) + sum(cpu_scores)


# def open_paths(state):
#   player_scores = [0, 0, 0]
#   cpu_scores = [0, 0, 0]

#   #column advantages
#   for j in range(state.col):
#     spots_above = 0
#     curr_occupy = 0
#     player = None
#     for i in range(state.row-1,-1,-1):
#       if state.board[i][j] != 0 and player is not None:

#         if state.board[i][j] == player:
#           curr_occupy += 1
#         else:
#           break

#       elif state.board[i][j] != 0 and player is None:
#         player = state.board[i][j]
#       else:
#         spots_above += 1
    
#     if curr_occupy + spots_above >= 4 and player == 1:
#       player_scores[4-curr_occupy-1] += 1
    
#     if curr_occupy + spots_above >= 4 and player == 2:
#       cpu_scores[4-curr_occupy-1] += 1


#   #row advantages
#   for i in range(state.row):
#     spots_above = 0
#     curr_occupy = 0
#     player = None
#     for j in range(state.col):
      
    
  
  





#   player_scores[0] *= 100
#   cpu_scores[0] *= -100
#   player_scores[1] *= 50
#   cpu_scores[1] *= -50
#   player_scores[2] *= 10
#   cpu_scores[2] *= -10

#   return sum(player_scores) + sum(cpu_scores)





    




