# kivy_right_of_way


This is a small sail right of way learning app.

![sailcommando_logo](./sailcommander/assets/logos/SAIL_Commander.png)


# Install

The Repo is created with poetry.

```dash

# create virtual environment
python -m venv .venv

# poetry
python -m pip install --upgrade pip

python -m pip install poetry

# poetry update and install of packages

poetry update --lock -vvv

poetry install

```



## MDApp Design

https://m3.material.io/
https://m3.material.io/components


https://github.com/kivymd/KivyMD/wiki/

Chips:
https://github.com/kivymd/KivyMD/wiki/Components-Chip


ICONs:
https://pictogrammers.com/library/mdi/
# https://pictogrammers.com/library/mdi/   # ICONs


## Links


https://github.com/kivymd/KivyMD/wiki/Modules-Material-App#minimal-app

https://kivymd.readthedocs.io/en/1.1.1/getting-started/



# Sounds

# idea https://www.youtube.com/watch?v=YqseTGOnzYg

convert with audocity




## Screens of the App

The App contains 2 Screens.






# To make an android app

[Here](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04-de) a link to make buildozer work on ubuntu.

Install `javac` see [here](https://stackoverflow.com/questions/66853462/how-to-install-javac-on-linux-mint).

```dash

# for Ubuntu
sudo apt-get install openjdk-8-jdk

# check version
javac -version   
# javac 1.8.0_352

```

Be sure libssl-dev and java is up-to-date on your machine. it cause strange errors like not installing sdk-tools on the machine or not establishing ssl download conections.

```dash

sudo apt-get update

sudo apt-get install libssl-dev

java -version #1.8

sudo apt install default-jre

java -verion #11.0.18

```



```dash
# additionally

sudo apt install libltdl-dev

sudo apt install libffi-dev

sudo apt-get update

```


In case sdk-tools get not installed, do it manually, but there is a deeper problem.

https://stackoverflow.com/questions/59330223/sdkmanager-not-installed

Install buildozer in the virtual environment with poetry

```dash

poetry add buildozer

poetry add cython

# do not miss to add `.buildozer` to  .gitignore  file

```
It will be automatically installed, if all is up-to-date.

Optional:

Install [sdkmanager](https://developer.android.com/studio/command-line/sdkmanager)


Download the latest "command line tools only" package from the Android Studio downloads page and unzip the package.
Move the unzipped cmdline-tools directory into a new directory of your choice, such as android_sdk. This new directory is your Android SDK directory.

Add the unzipped files to your .venv or .buildozer/android/app/plattform/android-sdk/tools/....


## Config buildozer

Required if something goes wrong.


Download the SDK manager here: wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip (run this on your command line in your buildozer directory)

Then you unzip it with the command: $ unzip sdk-tools-linux-3859397.zip

when you see a tools directory you have successfully installed sdkmanager

Create a .spec file with 
```dash 
buildozer init
```

Then edith your .spec (buildozer.spec) file(in your kivy app folder) line 112 with the path where you unzipped your SDK file

andriod.sdk_path = (Your file path) eg /home/freezy/buildozer/


Important for kivy and kivymd is to specifiy for buildozer the version in the buildozer.spec file snce it does not read th poetry.lock file for versions, so it may break the app when it starts up.

In case packages for buildozer needs to be updated: 

```dash

buildozer android clean
```

Anyway, here are the things to look on:

Although kivy 2.0.0 is used locally it requires for buildozer 2.1.0 because a package is missing else.

```dash

# update all your reverenced pics for buildozer

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# always update specifically
requirements = python3,kivy==2.1.0, kivymd==1.1.1, pyyaml==6.0, python-dotenv==0.21.1

# buildozer.spec  file: 
# line 127
# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =
android.sdk_path = /home/heiko/Repos/kivy/kivy_health_repo/kivy_health/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager.sh

# copy unzipped downloaded sdkmanager into the folder android-sdk/tools/bin/...
# problem solved with update libssl-dev

```


# Work with buildozer

Following the description [here](https://realpython.com/mobile-app-kivy-python/)

```dash

# to make it testable

buildozer init

buildozer -v android debug

```

When running buildozer to create the android related files they will show up in the new created `bin` folder.


![bin_apk](./assets/bin_apk.png)




# How to deploy on Android

Install the android debug bridge for deploying the apk file to your mobile for test reasons.

[Here](https://www.youtube.com/watch?v=pzsvN3fuBA0) is a video for this.

[Troubleshooting](https://www.youtube.com/watch?v=We45D_TjKdc) video for adb connections.

```dash

# install linux tools
sudo apt install android-tools-adb
sudo apt install android-tools-fastboot


# install android debug bridge (adb)
sudo apt install adb


# connect to device
adb connect 192.168.0.158:5555  # works not for me

# to list all connections
adb devices

sudo adb kill-server
sudo adb start-server

adb devices

# my list of devices
# 222be3df
# 29477c1e

# switch to dir of bin
cd ./bin

# transfer apk from ./bin/ folder:
adb -s 29477c1e install sailcommander-0.1-arm64-v8a_armeabi-v7a-debug.apk

# for error logging
adb -s 29477c1e logcat *:S python:D   


```


![adb_devices](./assets/adb_devices.png)




## How to do it in a fast way


``` powershell

# creat the apk
buildozer -v android debug

buildozer android debug deploy run logcat


adb logcat -s python

# switch to dir of bin
cd ./bin

# adb devices
# # my personal list of devices
# # 222be3df
# # 29477c1e

# transfer apk from ./bin/ folder:
# adb -s 29477c1e install sailcommander-0.1-arm64-v8a_armeabi-v7a-debug.apk

adb -s 29477c1e install sail_rightofway-0.1-arm64-v8a_armeabi-v7a-debug.apk


```


## Release on the market¶

If you have built your own APK with Buildozer or with python-for-android, you can create a release version that may be released on the Play store or other Android markets.

To do this, you must run Buildozer with the release parameter (e.g. buildozer android release), or if using python-for-android use the --release option to build.py. This creates a release AAB in the bin directory, which you must properly sign and zipalign. The procedure for doing this is described in the Android documentation at https://developer.android.com/studio/publish/app-signing.html#signing-manually - all the necessary tools come with the Android SDK.




# All on Mobil

![login](./assets/screenshoots/App_start.jpg)

![sail_down](./assets/screenshoots/App_Sail_down.jpg)

![sail_scenario](./assets/screenshoots/App_Scenario.jpg)

![sail_up](./assets/screenshoots/App_Sail_up.jpg)

![sail_commando](./assets/screenshoots/App_Sail_Commando.jpg)

![sail_bedingung](./assets/screenshoots/App_Sail_Bedingung.jpg)



## Create a video

"STRG + Shift + ALT + R" to record a 30 second video

![video](./assets/video_sail_commander.webm)






## Impressumpflicht


Den meisten Betreibern einer Online-Präsenz – ob eigene Website oder Online-Shop – ist klar, dass sie ein Impressum und eine Datenschutzerklärung auf den Internetseiten ihres Auftrittes einbinden müssen. Sie sichern sich somit gegen mögliche Rechtsansprüche seitens der Kunden und Anwaltskanzleien ab. Des Weiteren verringern sie damit das Risiko gegenüber Abmahnungen, die empfindliche Geldstrafen mit sich bringen können. Diese können sich derzeit auf bis zu 500 Euro belaufen. Das Wissen um eine Impressumspflicht für Apps hat sich jedoch bei vielen App-Anbietern noch nicht ausreichend herumgesprochen. Doch mit dem 2007 in Kraft getretenen Telemediengesetz (TMG) bezieht sich das Impressum auch auf die Nutzung von solchen Medien. Dies trifft sowohl auf kostenlose als auch kostenpflichtige Apps zu. Vor allem §5 des TMG vereint die notwendigen Informationen bezüglich dieser Thematik. Ein Aspekt, der aufgrund des vorherrschenden Platzmangels in der eigenen App auch vergessen oder als nicht wichtig angesehen wird. Mit wenigen Handgriffen lassen sich diese Probleme ausräumen, um die Apps online stellen zu können und sicherzugehen, dass sie in den App Stores weiterhin zum Download bereitstehen.

### i

In dem Dialogfenster können die notwendigen Angaben eingegeben werden. Darunter zählen unter anderem:

- vollständiger Name (Name der Firma, verantwortliche Personen)
- Anschrift
- E-Mail-Adresse
- Telefonnummer
- USt-Identifikationsnummer (falls vorhanden)
- Eintrag in das Handelsregister (falls vorhanden) uvm.

Nach der erfolgreichen Eingabe der Daten erscheint im oberen linken Bereich in der App ein i-Icon. Dieses steht stellvertretend für das Impressum.




