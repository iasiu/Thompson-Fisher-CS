from data import jobsData
from model import Factory, Machine, Task
import ffmpeg

import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D

#f = Factory(jobsData)

alh = SwarmPackagePy.pso(50, tf.easom_function, -10, 10, 2, 20,
                         w=0.5, c1=1, c2=1)
animation(alh.get_agents(), tf.easom_function, -10, 10)
animation3D(alh.get_agents(), tf.easom_function, -10, 10, sr=True)