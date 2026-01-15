[app]
title = Arif Khan Service
package.name = arifservice
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1
orientation = portrait
# قمت بتغيير هذا السطر لبناء نسخة واحدة فقط لضمان النجاح السريع
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
