[app]
title = WarnaKivyApp
package.name = warnakivy
package.domain = org.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,pkl
version = 1.0
requirements = python3,kivy,opencv-python,numpy,pandas,scikit-learn
orientation = portrait
fullscreen = 0

# Android-specific options
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0
android.ndk_api = 21
# Biarkan SDK & NDK path default, GitHub Actions akan mengatur dari ENV
# Jangan isi `android.sdk` atau `android.ndk` secara manual kecuali kamu tahu path-nya

[buildozer]
log_level = 2
warn_on_root = 1
