from linkedin_api import Linkedin
import os

user, password = os.getenv('LINKEDIN_USER'), os.getenv('LINKEDIN_PASSWORD')

class LinkedIn:
  def __init__(self):
    self.linkedin = Linkedin(user, password)
    
  def get_profile(self, username):
    try:
      profile = self.linkedin.get_profile(username)
      return profile
    except Exception as E:
      print(E)
      
  def get_conversations(self):
    try:
      conversations = self.linkedin.get_conversations()
      return conversations
    except Exception as E:
      print(E)