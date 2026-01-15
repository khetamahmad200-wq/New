[app]
title = Arif Khan Service
package.name = arifapp
package.domain = org.khetama
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False
android.logcat_filters = *:S python:D
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
