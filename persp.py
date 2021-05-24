from googleapiclient import discovery
import json
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import discord
from discord.ext import commands
import youtube_dl
import os
import random


API_KEY = 'AIzaSyASJ0y5PJbGn27Z6Zq2Qn1owg2c6rLBPvI'

value="a"

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1")


def score(text):
  analyze_request = {
      'comment': { 'text': text },
      'requestedAttributes': {'TOXICITY': {},'FLIRTATION':{}}
    }

  response = client.comments().analyze(body=analyze_request).execute()

  global toxic_value,flirt_value,spam_value

  toxic_value = response['attributeScores']['TOXICITY']["spanScores"][0]['score']['value']
  flirt_value = response['attributeScores']['FLIRTATION']["spanScores"][0]['score']['value']
  
  
  print("TOXICITY RATING:",toxic_value)
  print("Flirt Rating:",flirt_value)

