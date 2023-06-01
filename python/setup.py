import os
import sys
import datetime

def main():
    if not os.path.exists('home'):
        os.makedirs('home')
    if not os.path.exists('bin'):
        os.makedirs('bin')
    if not os.path.exists('scripts'):
        os.makedirs('scripts')
    if not os.path.exists('addons'):
        os.makedirs('addons')
    if not os.path.exists('documents'):
        os.makedirs('documents')
    if not os.path.exists('home/user'):
        os.makedirs('home/user')
    if not os.path.exists('home/user/documents'):
        os.makedirs('home/user/documents')
    if not os.path.exists('home/user/documents/projects'):
        os.makedirs('home/user/documents/projects')
    if not os.path.exists('system'):
        os.makedirs('system')
    if not os.path.exists('system/scripts'):
        os.makedirs('system/scripts')
    if not os.path.exists('system/logs'):
        os.makedirs('system/logs')
    if not os.path.exists('mount'):
        os.makedirs('mount')
    