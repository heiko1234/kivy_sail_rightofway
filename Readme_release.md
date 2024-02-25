

https://developer.android.com/studio/publish/app-signing



https://groups.google.com/g/kivy-users/c/5-G7wkbHb_k?pli=1

https://www.javatpoint.com/keytool-error-java-io-filenotfoundexception


# https://developer.android.com/studio/publish/app-signing#generate-key

https://developer.android.com/studio


# https://developer.android.com/studio/publish/app-signing#generate-key


# Video: https://www.youtube.com/watch?v=su7sxZVpcAE




In general, the steps are:

1. Generate Keystore (once)
2. Create Release APK
3. Sign APK
4. Zip-align APK




# 1. Generate Keystore (once)
 Done with Android Studio 

 worked quite nicely. 

 Copied the keys into the folder keystores which is in .gitignore and do not get pushed :)


# 2. Create Release APK
# release for market: app store    # build of .aab  file
buildozer android release


# 3. Sign APK

Do not forget to replace the keystore and the alias with your own values.
my_password needs to be replaced with the password of the keystore

P4A_RELEASE_KEYSTORE=./keystores/android_keystore_2024.jks P4A_RELEASE_KEYSTORE_PASSWD="my_password" P4A_RELEASE_KEYALIAS="android_key" P4A_RELEASE_KEYALIAS_PASSWD="my_password" buildozer android release




Generate an upload key and keystore

If you don't already have an upload key, which is useful when configuring Play App Signing, you can generate one using Android Studio as follows:

    In the menu bar, click Build > Generate Signed Bundle/APK.
    In the Generate Signed Bundle or APK dialog, select Android App Bundle or APK and click Next.
    Below the field for Key store path, click Create new.

    On the New Key Store window, provide the following information for your keystore and key, as shown in figure 2.

    Figure 2. Create a new upload key and keystore in Android Studio.

    Keystore
        Key store path: Select the location where your keystore should be created. Also, a file name should be added to the end of the location path with the .jks extension.
        Password: Create and confirm a secure password for your keystore.

    Key
        Alias: Enter an identifying name for your key.
        Password: Create and confirm a secure password for your key. This should be the same as your keystore password. (Please refer to the known issue for more information)
        Validity (years): Set the length of time in years that your key will be valid. Your key should be valid for at least 25 years, so you can sign app updates with the same key through the lifespan of your app.
        Certificate: Enter some information about yourself for your certificate. This information is not displayed in your app, but is included in your certificate as part of the APK.

    Once you complete the form, click OK.

    If you would like to build and sign your app with your upload key, continue to the section about how to Sign your app with your upload key. If you only want to generate the key and keystore, click Cancel.






Sign your app with your key

If you already have an upload key, use it to sign your app. If instead your app is already signed and published to the Google Play store with an existing app signing key, use it to sign your app. You can later generate and register a separate upload key with Google Play to sign and upload subsequent updates to your app.

To sign your app using Android Studio, follow these steps:

    If you don’t currently have the Generate Signed Bundle or APK dialog open, click Build > Generate Signed Bundle/APK.
    In the Generate Signed Bundle or APK dialog, select either Android App Bundle or APK and click Next.
    Select a module from the drop down.

    Specify the path to your keystore, the alias for your key, and enter the passwords for both. If you haven't yet prepared your upload keystore and key, first Generate an upload key and keystore and then return to complete this step.

    Figure 3. Sign your app with your upload key.

    Note: For increased security, Google Play is introducing a new process to upload signing keys, and the option Export encrypted key in Android Studio is being deprecated. If you're signing an app with an existing app signing key, and you'd like to opt your app in to Play App Signing, see Opt in an existing app for the process to encrypt and export your signing key.

    Click Next.

    In the next window (shown in figure 4), select a destination folder for your signed app, select the build type, choose the product flavor(s) if applicable.

    If you are building and signing an APK, you need to select which Signature Versions you want your app to support. To learn more, read about app signing schemes




Using Play App Signing

As described earlier in this page, configuring Play App Signing is required to sign your app for distribution through Google Play (except for apps created before August 2021, which may continue distributing self-signed APKs). The steps you need to take depend on whether your app has not yet been published to Google Play, or your app is already signed and was published before August 2021 using an existing app signing key.
Configure a new app

To configure signing for an app that has not yet been published to Google Play, proceed as follows:

    If you haven’t already done so, generate an upload key and sign your app with that upload key.
    Sign in to your Play Console.
    Follow the steps to prepare & roll out your release to create a new release.
    After you choose a release track, configure app signing under the App signing section as follows:
        To have Google Play generate an app signing key for you and use it to sign your app, you don't have to do anything. The key you use to sign your first release becomes your upload key, and you should use it to sign future releases.
        To use the same key as another app on your developer account, select Change app signing key > Use the same key as another app in this account, select an app, and then click Continue.
        To provide your own signing key for Google to use when signing your app, select Change app signing key and select one of the Export and upload options that lets you securely upload a private key and its public certificate.

Note: If you haven't already accepted the Terms of Service, you are required to review the terms and select Accept to continue.

In the section called App Bundles, click Browse files to locate and upload the app you signed using your upload key. For more information about releasing your app, refer to prepare & roll out your release. When you release your app after configuring Play App Signing, Google Play generates (unless you upload an existing key) and manages your app’s signing key for you. Simply sign subsequent updates to your app using your app’s upload key before uploading it to Google Play.

If you need to create a new upload key for you app, go to the section about how to Reset a lost or compromised private upload key.
Opt in an existing app

If you’re updating an app that’s already published to Google Play using an existing app signing key, you can opt in to Play App Signing as follows:

    Sign in to your Play Console and navigate to your app.
    On the left menu, click Release > Setup > App signing.
    If applicable, review the Terms of Service and select Accept.
    Select one of the options that best describes the signing key you want to upload to Google Play and follow the instructions that are shown. For example, if you are using a Java Keystore for your signing key, select Upload a new app signing key from Java Keystore and follow the instructions to download and run the PEPK tool, and upload the generated file with your encrypted key.
    Click Enroll.

You should now see a page with the details of your app’s signing and upload certificates. Google Play now signs your app with your existing key when deploying it to users. However, one of the most important benefits to Play App Signing is the ability to separate the key you use to sign the artifact you upload to Google Play from the key that Google Play uses to sign your app for distribution to users. So, consider following the steps in the next section to generate and register a separate upload key.
Generate and register an upload certificate

When you're publishing an app that is not signed by an upload key, the Google Play Console provides the option to register one for future updates to the app. Although this is an optional step, it’s recommended that you publish your app with a key that’s separate from the one Google Play uses to distribute your app to users. That way, Google keeps your signing key secure, and you have the option to reset a lost or compromised private upload key. This section describes how to create an upload key, generate an upload certificate from it, and register that certificate with Google Play for future updates of your app.

The following describes the situations in which you see the option to register an upload certificate in the Play Console:

    When you publish a new app that’s signed with a signing key and opt it in to Play App Signing.
    When you are about to publish an existing app that’s already opted in to Play App Signing, but it is signed using its signing key.

If you are not publishing an update to an existing app that’s already opted in to Play App Signing, and you’d like to register an upload certificate, complete the steps below and continue on to the section about how to reset a lost or compromised private upload key.

If you haven’t already done so, generate an upload key and keystore.

After you create your upload key and keystore, you need to generate a public certificate from your upload key using keytool, with the following command:

$ keytool -export -rfc
  -keystore your-upload-keystore.jks
  -alias upload-alias
  -file output_upload_certificate.pem

Now that you have your upload certificate, register it with Google when prompted in the Play Console or when resetting your upload key.
Upgrade your app signing key

In some circumstances, you might want to change your app's signing key. For example, because you want a cryptographically stronger key or your signing key has been compromised. However, because users can only update your app if the update is signed with the same signing key, it's difficult to change the signing key for an app that's already published.

If you publish your app to Google Play, you can upgrade the signing key for your published app through the Play Console—your new key is used to sign installs and app updates on Android 13 and higher, while your older app signing key is used to sign updates for users on earlier versions of Android.

To learn more, read Upgrade your app signing key.
Reset a lost or compromised private upload key

If you lost your private upload key or your private key has been compromised, you can create a new one and request an upload key reset in the Play console.
Note: Resetting your upload key will not affect the app signing key that Google Play uses to re-sign APKs before delivering to users.
Configure the build process to automatically sign your app

In Android Studio, you can configure your project to sign the release version of your app automatically during the build process by creating a signing configuration and assigning it to your release build type. A signing configuration consists of a keystore location, keystore password, key alias, and key password. To create a signing configuration and assign it to your release build type using Android Studio, complete the following steps:

    In the Project window, right click on your app and click Open Module Settings.
    On the Project Structure window, under Modules in the left panel, click the module you would like to sign.
    Click the Signing tab, then click Add .

    Select your keystore file, enter a name for this signing configuration (as you may create more than one), and enter the required information.

    Figure 7. The window for creating a new signing configuration.
    Click the Build Types tab.
    Click the release build.

    Under Signing Config, select the signing configuration you just created. 









n general, the steps are:

1. Generate Keystore (once)
2. Create Release APK
3. Sign APK
4. Zip-align APK

For a specific example of doing a release, here is the setup for my SayThis app:

* My keystore is in ~/keystores
* My project root is in ~/saythis
* Which means buildozer.spec is at ~/saythis/buildozer.spec
* The virtualenv for the project is activated

The specific commands I use to release the SayThis app are:

$ cd ~
$ keytool -genkey -v -keystore ./keystores/net-clusterbleep-saythis.keystore -alias cb-play -keyalg RSA -keysize 2048 -validity 10000
$ cd ~/saythis
$ buildozer android release
$ cd ~
$ jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ./keystores/net-clusterbleep-saythis-release.keystore ./saythis/bin/SayThis-1.1.6-release-unsigned.apk cb-play
$ .buildozer/android/platform/android-sdk-21/tools/zipalign -v 4 ./saythis/bin/SayThis-1.1.6-release-unsigned.apk ./saythis/bin/SayThis.apk

The SayThis.apk is what you upload to Google Play. Please make sure you use your own name for the keystore and APKs.



# ####################### What is needed to be done

# 1. Generate Keystore (once)

# /home/heiko/Schreibtisch/Repos/kivy_apps/kivy_sail_rightofway/.keystores/keystore
# keytool -genkey -v -keystore .keystores/keystore -alias cb-play -keyalg RSA -keysize 2048 -validity 10000


# keytool -genkey -v -keystore ./.keystores -alias cb-play -keyalg RSA -keysize 2048 -validity 10000

# keytool -genkey -v -keystore ./keystores -alias cb-play -keyalg RSA -keysize 2048 -validity 10000

keytool 



# 2. Create Release APK   # AAB File

# release for market: app store    # build of .aab  file
buildozer android release


# 3. Sign APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ./keystores/.keystore ./bin/.aab cb-play

# 4. Zip-align APK
.buildozer/android/platform/android-sdk-21/tools/zipalign -v 4 ./bin/.aab ./bin/.apk














