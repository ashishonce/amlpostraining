import os
from azureml.core import Experiment


def getMetrics(ws,experiment_name,tags={}):
    experiment = Experiment(workspace = ws, name = experiment_name)
    for run in experiment.get_runs(tags=tags):
        print (run.get_metrics());
