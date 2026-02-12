# Hello World APK - Build System 🔧

A complete APK build system for a simple Python "Hello World!" Android app using **Kivy** and **Buildozer**, with automated builds via **GitHub Actions**.

## 📋 Project Structure

```
apk-project/
├── main.py               # Kivy app displaying "Hello World!"
├── requirements.txt      # Python dependencies
├── buildozer.spec        # Buildozer configuration
├── .gitignore           # Excludes build artifacts
└── .github/
    └── workflows/
        └── build.yml    # GitHub Actions CI/CD pipeline
```

## 🚀 Quick Start

### Local Build (Termux/Ubuntu)

1. **Install dependencies:**

```bash
# Termux (Android)
pkg install python git openjdk-17 zip unzip autoconf libtool pkg-config \
  zlib-dev ncurses-dev cmake libffi libssl build-essential ccache \
  python-dev

# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y python3 python3-pip git openjdk-17-jdk \
  zip unzip autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
  libtinfo5 cmake libffi-dev libssl-dev build-essential ccache
```

2. **Install Python tools:**

```bash
pip install --upgrade pip setuptools wheel
pip install buildozer
```

3. **Build the APK:**

```bash
cd /path/to/apk-project
buildozer -v android debug
```

4. **APK location:**

After successful build, the APK will be at:
- `bin/HelloWorld-0.1-debug.apk` (or similar)

> ⚠️ **Note:** First build may take 30-60 minutes as Buildozer downloads and sets up the Android SDK/NDK, Python for Android, and all dependencies.

### GitHub Actions (Automated Builds)

1. **Push to repository:**

```bash
git init
git add .
git commit -m "Initial commit: Hello World APK build system"
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main
```

2. **Build triggers:**

   - Automatic build on every push to `main` branch
   - Artifacts stored for 14 days

3. **Download APK:**

   - Go to GitHub → Actions → Select workflow run → Artifacts
   - Download `android-apk` artifact

## 📱 Testing the APK

### On Android Device:

1. Enable **Unknown Sources** in Settings → Security
2. Transfer APK to device (USB, cloud, or email)
3. Tap to install
4. App will appear as "HelloWorld" with a Kivy icon
5. Launch → should see "Hello World!" in large centered text

### Using ADB:

```bash
adb install bin/*.apk
adb shell monkey -p org.example.helloworld -c android.intent.category.LAUNCHER 1
```

## 🔧 Buildozer Configuration

The `buildozer.spec` file controls:

- **Package metadata:** `title`, `package.name`, `package.domain`
- **Requirements:** `kivy` (plus any other dependencies)
- **Android settings:** API level 33, min API 21
- **Orientation:** Portrait mode
- **Permissions:** None (basic app)

To modify, edit `buildozer.spec` and rebuild.

## 🐛 Troubleshooting

### Build fails with Java errors:

```bash
# Ensure Java 17 is installed and JAVA_HOME is set
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
```

### Cython/NDK errors:

```bash
# Clean and rebuild
buildozer android clean
buildozer -v android debug
```

### Out of memory during build:

```bash
# Reduce parallel jobs
export BUILDOZER_ANDROID_NDK_JOBS=2
```

### APK not installing (parse error):

- Ensure you built with `android debug` (debuggable)
- Check min SDK version matches your device
- Try `buildozer android release` for production (requires keystore)

## 📊 Build Times

| Stage | Time |
|-------|------|
| First build | 30-60 min (SDK/NDK download) |
| Subsequent builds | 5-15 min |
| Incremental rebuilds | 1-3 min |

## 🔄 Continuous Integration

The GitHub Actions workflow:

1. ✅ Triggers on push to main/master
2. ✅ Sets up Python 3.9 environment
3. ✅ Installs system dependencies (OpenJDK, build tools)
4. ✅ Installs Buildozer and project requirements
5. ✅ Builds APK using `buildozer android debug`
6. ✅ Uploads APK as artifact (14-day retention)
7. ✅ Uploads build logs on failure (7-day retention)

## 📦 Dependencies

- **Kivy 2.3.0** - UI framework
- **Python 3.9** - Target Python version
- **Android API 33** - Target Android version
- **Buildozer** - Build tool

## 🔐 Security Notes

- Debug APKs are unsigned (use `buildozer android release` for production)
- No special permissions requested
- No network access required

## 📝 License

This example project is public domain. Feel free to use, modify, and distribute.

---

**Built with ❤️ using Kivy + Buildozer + GitHub Actions**
