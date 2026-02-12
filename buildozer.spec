[app]

# Application version
version = 1.0.0

# Title of your application
title = HelloWorld

# Package name
package.name = helloworld

# Package domain (needed for android/ios packaging)
package.domain = org.example

# Source directory where main.py is located
source.dir = .

# Source files to include (comma-separated)
source.include_exts = py,png,jpg,kv,atlas

# Main Python file
requirements = python3,kivy

# Python version to use
python.version = 3.9

# Android specific configurations
android.api = 33
android.minapi = 21
android.ndk = 27c
android.ndk_api = 21
android.sdk = 33

# Permissions needed (none for basic Hello World)
android.permissions =

# Features to use
android.features =

# Boot animation
android.boot_animation = 0

# Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# Add java jars
android.add_jars =

# Add libraries
android.add_libs_armeabi =

# Add assets
android.add_assets =

# Google services JSON file (if using Firebase etc.)
# android.google_api_key =
# android.google_app_id =

# iOS specific (optional)
ios.kivy_ios_dir = ./kivy-ios
ios.deployment_target = 13.0

# Build configurations
buildozer_log_level = 2

# P4A configurations
p4a.branch = master
p4a.bootstrap = sdl2

# Orientation (portrait or landscape)
orientation = portrait

# Fullscreen mode
fullscreen = 0

# Allow backup
android.allow_backup = False

# Hardware features
android.hardware =
