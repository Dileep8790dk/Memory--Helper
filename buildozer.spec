[app]

# (str) Title of your application
title = ToDoApp (Kivy)

# (str) Package name
package.name = todoapp

# (str) Package domain (needed for Android/iOS packaging)
package.domain = org.test

# (str) Application versioning - Required
version = 0.1

# (list) Application requirements - Must include sqlite3
requirements = python3,kivy,sqlite3

# (str) Source code where the main.py lives - Points to your 'ToDoApp' subfolder
source.dir = ToDoApp

# CRITICAL FINAL FIX: Update NDK to the minimum supported version (25b)
# This resolves the "minimum supported NDK version is 25" error.
android.ndk = 25b

# (list) Permissions
android.permissions = INTERNET

[buildozer]
# (int) Log level (0 = None, 1 = Error, 2 = Warning, 3 = Info, 4 = Debug)
log_level = 2
