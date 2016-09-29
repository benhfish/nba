import os

#edit chances and lotto_picks to use for any combination
chances=[114,113,112,111,99,89,79,69,59,49,39,29,19,9,6,4]
chances_pct=[float(chance)/sum(chances) for chance in chances]
lotto_picks=1

#global matrix of all probs that gets set in setprob
probs=[[0.0 for x in range(len(chances))] for y in range(len(chances))]

def setprob(row):
  #probability of this row happening
  p=1.0
  #probabilities of previous events in row happening
  ps=[0.0,]
  for ii in range(lotto_picks):
    p*=chances_pct[row[ii]]/(1-sum(ps))
    ps.append(chances_pct[row[ii]])
  #for each seed in a row, increase that seeds 
  #prob for acheiving that pick by the overall
  #prob for the entire row
  for pick,seed in enumerate(row):
    probs[seed][pick]+=p

def make_pick(picks, total_picks):
  #if already made all lottery picks fill remainng in order
  if len(picks)>=total_picks:
    for kk in range(len(chances)):
      if kk not in picks:
        picks.append(kk)
    #call to set prob then return
    setprob(picks)
    return
  #iterate through all picks and add if not already a pick
  for jj in range(len(chances)):
    if jj in picks:
      continue
    make_pick(picks+[jj],total_picks)

if __name__ == '__main__':
  #create a giant tree of all possible picks
  for ii in range(len(chances)):
    make_pick([ii,], lotto_picks)
  
  #these lines grew long quick... should probably break up but works for now
  print('seed \tchance {0}'.format(''.join('\tp({0}) '.format(x+1) for x in range(len(chances)))))
  print(os.linesep.join('{0} \t{1} {2}'.format(iter+1,chances[iter],''.join('\t{0:.2E} '.format(val) for val in row)) for iter,row in enumerate(probs)))
  
