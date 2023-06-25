from math import exp
from random import random

START_TEMP  = 100 # 1回の遷移で変化するスコアの絶対値の最大値
END_TEMP    = 10  # 1回の遷移で変化するスコアの絶対値の最小値
LIMIT_TIME  = 2
now_time    = None # 経過時間 0 <= now_time <= LIMIT_TIME
now_temp    = START_TEMP + (END_TEMP - START_TEMP) * (now_time / LIMIT_TIME)
delta_score = None # スコアの変化量
prob        = exp(delta_score / now_temp)
TRANSITION  = prob > random() # TRANSITIONがTrueなら遷移を受け入れる