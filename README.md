# Shake Color Changer

A simple Android application that changes the background color when the device is shaken.

## Features

- Detects device shake using the accelerometer sensor
- Changes background color to a random color when shake is detected
- Simple and intuitive user interface

## Requirements

- Android Studio
- Android device with accelerometer sensor or an emulator that can simulate accelerometer events

## How to Use

1. Clone this repository
2. Open the project in Android Studio
3. Build and run the app on your device
4. Shake your device to see the background color change

## How It Works

The app uses the device's accelerometer sensor to detect shake gestures. When a shake is detected, the app calculates the total acceleration and if it exceeds a certain threshold, changes the background color to a random color.

## Project Structure

- `MainActivity.java`: Main activity that handles shake detection and color changing logic
- `activity_main.xml`: Layout file for the main activity
- `AndroidManifest.xml`: Android manifest file for the app
- `build.gradle`: Gradle build file for the app

## License

This project is open source and available under the MIT License. 