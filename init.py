import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

import schedule
import time
import sys

import google.generativeai as genaiA
from google import genai

from google.genai import types
import wave
import requests

import os
import datetime
import time
import subprocess
import pyperclip
import pyautogui
import glob
import gspread
import random # (ย้าย import random มาไว้ด้านบน)

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from google.oauth2.service_account import Credentials


try:
    GEMINI_API_KEY = "AIzaSyCrmJGlqOoAk1TkjY29XE_CKSaOdpiABdc"
    genaiA.configure(api_key=GEMINI_API_KEY)
except ValueError as e:
    print(e)
    print("เกิดข้อผิดพลาด: กรุณาตั้งค่า GEMINI_API_KEY ใน Environment Variable")
    exit()

file_ThaiFood = "source/ThaiFood.jpg"
file_Sunset = "source/Sunset.jpg"