import os
from dotenv import load_dotenv
from fastapi import APIRouter
import requests

load_dotenv()
router = APIRouter(prefix="/ai")