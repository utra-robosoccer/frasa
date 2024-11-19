from setuptools import setup

setup(name="frasa_env", 
      version="1.0", 
      description='FRASA RL Environment',
      install_requires=[
          "gymnasium>=0.29.0",
          "numpy>=1.20.0",
          "stable_baselines3>=2.1.0",
          "sb3-contrib>=2.1.0", 
          "mujoco>=3.1.5",
          "meshcat>=0.3.2",
          "sbx-rl>=0.17.0",
          ], 
      )
