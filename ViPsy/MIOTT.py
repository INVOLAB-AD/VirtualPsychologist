import instapy
import facebook
import nltk
import numpy
import MySQLdb
import connections
import ArchiveDataRead
import sentiment
import DeceptionDetection
import RequestSend
import Promote

class MIOTT:
    def __init__(_self, Name):
        print("This Bot is Working for Brand Name ",Name)
        print("Initializing...")
        _self.SocialMediaobject = None
        _self.Username = None
        _self.Password = None
        _db_object = None

    def connect(_self, socialsite):
        _self.Username = input("Enter the username for ",socialsite.lower()," : ")
        _self.Password = input("Enter the password for ",socialsite.lower()," : ")

        if socialsite.upper()=='FACEBOOK':
            try:
                # code to connect to facebook
            except e:
                # write code for exception handling
        else:
            try:
                # code to connect to instagram
            except e:
                # write code for exception handling

    def db_Connect(_self,uname,password,server):
        # write code for DB_Connect

    def upload_data(_self):
        # write code for uploading data into database

    def download_data(_self):
        # fetch data from database into a file

    def search_for_tags(_self,sm_object):
        # searching tags function

    def do_follow(_self):
        # follow code

    def do_like(_self):
        # like code

    def do_send_friendRequest(_self):
        # sending friend request

    def senti_Analysis(_self):
        #analyze sentiments

    def deception_detection(_self):
        # detect truthfulness in reviews
    
    def start_promotions(_self, nums = 50):
        # promotions of post
