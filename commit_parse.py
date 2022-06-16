import json

data = {
    "commits": [
        {
            "commit": "7a2a281d09966da8dafd63a86389c1dbf9ab67f6",
            "parents": ["6f816f919771a8c0ed084d315ee77e9b43d12b00"],
            "refs": [],
            "Author": "João Pedro Patrocinio <jpedro9966@gmail.com>",
            "AuthorDate": "Thu Dec 3 21:08:49 2020 -0300",
            "Commit": "João Pedro Patrocinio <jpedro9966@gmail.com>",
            "CommitDate": "Thu Dec 3 21:08:49 2020 -0300",
            "message": "Initial commit",
            "files": [
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "40b878d"],
                    "action": "A",
                    "file": ".gitignore",
                    "added": "1",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "8571d6f"],
                    "action": "A",
                    "file": "maltese-backend/package.json",
                    "added": "12",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "06f320c"],
                    "action": "A",
                    "file": "maltese-backend/src/main.js",
                    "added": "1",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "4d29575"],
                    "action": "A",
                    "file": "maltese-web/.gitignore",
                    "added": "23",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "0c83cde"],
                    "action": "A",
                    "file": "maltese-web/README.md",
                    "added": "70",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "e7b0249"],
                    "action": "A",
                    "file": "maltese-web/package-lock.json",
                    "added": "37771",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "f6d44aa"],
                    "action": "A",
                    "file": "maltese-web/package.json",
                    "added": "38",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "a11777c"],
                    "action": "A",
                    "file": "maltese-web/public/favicon.ico",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "aa069f2"],
                    "action": "A",
                    "file": "maltese-web/public/index.html",
                    "added": "43",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fc44b0a"],
                    "action": "A",
                    "file": "maltese-web/public/logo192.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "a4e47a6"],
                    "action": "A",
                    "file": "maltese-web/public/logo512.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "080d6c7"],
                    "action": "A",
                    "file": "maltese-web/public/manifest.json",
                    "added": "25",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "e9e57dc"],
                    "action": "A",
                    "file": "maltese-web/public/robots.txt",
                    "added": "3",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "74b5e05"],
                    "action": "A",
                    "file": "maltese-web/src/App.css",
                    "added": "38",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "3784575"],
                    "action": "A",
                    "file": "maltese-web/src/App.js",
                    "added": "25",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "1f03afe"],
                    "action": "A",
                    "file": "maltese-web/src/App.test.js",
                    "added": "8",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ec2585e"],
                    "action": "A",
                    "file": "maltese-web/src/index.css",
                    "added": "13",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ef2edf8"],
                    "action": "A",
                    "file": "maltese-web/src/index.js",
                    "added": "17",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "9dfc1c0"],
                    "action": "A",
                    "file": "maltese-web/src/logo.svg",
                    "added": "1",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "5253d3a"],
                    "action": "A",
                    "file": "maltese-web/src/reportWebVitals.js",
                    "added": "13",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "8f2609b"],
                    "action": "A",
                    "file": "maltese-web/src/setupTests.js",
                    "added": "5",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "934256c"],
                    "action": "A",
                    "file": "maltesemobile/.buckconfig",
                    "added": "6",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "40c6dcd"],
                    "action": "A",
                    "file": "maltesemobile/.eslintrc.js",
                    "added": "4",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "b274ad1"],
                    "action": "A",
                    "file": "maltesemobile/.flowconfig",
                    "added": "73",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "d42ff18"],
                    "action": "A",
                    "file": "maltesemobile/.gitattributes",
                    "added": "1",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ad572e6"],
                    "action": "A",
                    "file": "maltesemobile/.gitignore",
                    "added": "59",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "5c4de1a"],
                    "action": "A",
                    "file": "maltesemobile/.prettierrc.js",
                    "added": "6",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "9e26dfe"],
                    "action": "A",
                    "file": "maltesemobile/.watchmanconfig",
                    "added": "1",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "23cd158"],
                    "action": "A",
                    "file": "maltesemobile/App.js",
                    "added": "114",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "1784766"],
                    "action": "A",
                    "file": "maltesemobile/__tests__/App-test.js",
                    "added": "14",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ad5ea4e"],
                    "action": "A",
                    "file": "maltesemobile/android/app/BUCK",
                    "added": "55",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "d79487d"],
                    "action": "A",
                    "file": "maltesemobile/android/app/build.gradle",
                    "added": "219",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fff270f"],
                    "action": "A",
                    "file": "maltesemobile/android/app/build_defs.bzl",
                    "added": "19",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "364e105"],
                    "action": "A",
                    "file": "maltesemobile/android/app/debug.keystore",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "11b0257"],
                    "action": "A",
                    "file": "maltesemobile/android/app/proguard-rules.pro",
                    "added": "10",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fa26aa5"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/debug/AndroidManifest.xml",
                    "added": "8",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "f5d509d"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/debug/java/com/maltesemobile/ReactNativeFlipper.java",
                    "added": "72",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "078a4f7"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/AndroidManifest.xml",
                    "added": "27",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "4b6e88a"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/java/com/maltesemobile/MainActivity.java",
                    "added": "15",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "55dda37"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/java/com/maltesemobile/MainApplication.java",
                    "added": "80",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "a2f5908"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-hdpi/ic_launcher.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "1b52399"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-hdpi/ic_launcher_round.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ff10afd"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-mdpi/ic_launcher.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "115a4c7"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-mdpi/ic_launcher_round.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "dcd3cd8"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-xhdpi/ic_launcher.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "459ca60"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-xhdpi/ic_launcher_round.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "8ca12fe"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-xxhdpi/ic_launcher.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "8e19b41"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "b824ebd"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "4c19a13"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "16a3b3b"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/values/strings.xml",
                    "added": "3",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "62fe59f"],
                    "action": "A",
                    "file": "maltesemobile/android/app/src/main/res/values/styles.xml",
                    "added": "9",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ed5a568"],
                    "action": "A",
                    "file": "maltesemobile/android/build.gradle",
                    "added": "37",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "3bdbd3d"],
                    "action": "A",
                    "file": "maltesemobile/android/gradle.properties",
                    "added": "28",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "f3d88b1"],
                    "action": "A",
                    "file": "maltesemobile/android/gradle/wrapper/gradle-wrapper.jar",
                    "added": "-",
                    "removed": "-"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "8422670"],
                    "action": "A",
                    "file": "maltesemobile/android/gradle/wrapper/gradle-wrapper.properties",
                    "added": "5",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "2fe81a7"],
                    "action": "A",
                    "file": "maltesemobile/android/gradlew",
                    "added": "183",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "62bd9b9"],
                    "action": "A",
                    "file": "maltesemobile/android/gradlew.bat",
                    "added": "103",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "dff62f0"],
                    "action": "A",
                    "file": "maltesemobile/android/settings.gradle",
                    "added": "3",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "6140a6c"],
                    "action": "A",
                    "file": "maltesemobile/app.json",
                    "added": "4",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "f842b77"],
                    "action": "A",
                    "file": "maltesemobile/babel.config.js",
                    "added": "3",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "a850d03"],
                    "action": "A",
                    "file": "maltesemobile/index.js",
                    "added": "9",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "2daf31d"],
                    "action": "A",
                    "file": "maltesemobile/ios/Podfile",
                    "added": "33",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ecbd496"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile-tvOS/Info.plist",
                    "added": "53",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ba72822"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile-tvOSTests/Info.plist",
                    "added": "24",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ff0c0a5"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile.xcodeproj/project.pbxproj",
                    "added": "791",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "69a7145"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile.xcodeproj/xcshareddata/xcschemes/maltesemobile-tvOS.xcscheme",
                    "added": "88",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "203fda3"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile.xcodeproj/xcshareddata/xcschemes/maltesemobile.xcscheme",
                    "added": "88",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ef1de86"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile/AppDelegate.h",
                    "added": "8",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "b25ec93"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile/AppDelegate.m",
                    "added": "58",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "118c98f"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile/Images.xcassets/AppIcon.appiconset/Contents.json",
                    "added": "38",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "2d92bd5"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile/Images.xcassets/Contents.json",
                    "added": "6",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "0248787"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile/Info.plist",
                    "added": "57",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "eb86b81"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile/LaunchScreen.storyboard",
                    "added": "58",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "b1df44b"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobile/main.m",
                    "added": "9",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "ba72822"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobileTests/Info.plist",
                    "added": "24",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "e85fa61"],
                    "action": "A",
                    "file": "maltesemobile/ios/maltesemobileTests/maltesemobileTests.m",
                    "added": "65",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "13a9642"],
                    "action": "A",
                    "file": "maltesemobile/metro.config.js",
                    "added": "17",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "139af8c"],
                    "action": "A",
                    "file": "maltesemobile/package-lock.json",
                    "added": "27887",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "22b2cb4"],
                    "action": "A",
                    "file": "maltesemobile/package.json",
                    "added": "29",
                    "removed": "0"
                }
            ]
        },
        {
            "commit": "6f816f919771a8c0ed084d315ee77e9b43d12b00",
            "parents": [],
            "refs": [],
            "Author": "Guilherme Avelino <gavelino@gmail.com>",
            "AuthorDate": "Fri Jan 17 08:22:35 2020 -0300",
            "Commit": "GitHub <noreply@github.com>",
            "CommitDate": "Fri Jan 17 08:22:35 2020 -0300",
            "message": "Initial commit",
            "files": [
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fe5ce64"],
                    "action": "A",
                    "file": "README.md",
                    "added": "2",
                    "removed": "0"
                }
            ]
        },
        {
            "commit": "6f816f919771a8c0ed084d315ee77e9b43d12b00",
            "parents": [],
            "refs": [],
            "Author": "Guilherme Avelino <gavelino@gmail.com>",
            "AuthorDate": "Fri Jan 17 08:22:35 2020 -0300",
            "Commit": "GitHub <noreply@github.com>",
            "CommitDate": "Fri Jan 17 08:22:35 2020 -0300",
            "message": "Initial commit",
            "files": [
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fe5ce64"],
                    "action": "A",
                    "file": "README.md",
                    "added": "2",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fe5ce64"],
                    "action": "A",
                    "file": "README.md",
                    "added": "2",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fe5ce64"],
                    "action": "A",
                    "file": "README.md",
                    "added": "2",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fe5ce64"],
                    "action": "A",
                    "file": "README.md",
                    "added": "2",
                    "removed": "0"
                },
                {
                    "modes": ["000000", "100644"],
                    "indexes": ["0000000", "fe5ce64"],
                    "action": "A",
                    "file": "README.md",
                    "added": "2",
                    "removed": "0"
                },
            ]
        }
    ]
}

#print(f"Commit: {data['commit'][0:7]} || Author: {data['Author'].split('<')[0]} || Files Changed: {len(data['files'])}")

info = []

for commit in data["commits"]:
    



