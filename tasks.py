from invoke import task

@task
def build(c):
   print('Building!')

@task
def hello(c):
   c.run('./script.py')