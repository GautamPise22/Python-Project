package com.example.shakecolorchanger;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Context;
import android.graphics.Color;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.view.View;
import android.widget.RelativeLayout;
import android.widget.Toast;

import java.util.Random;

public class MainActivity extends AppCompatActivity implements SensorEventListener {

    private SensorManager sensorManager;
    private Sensor accelerometer;
    private RelativeLayout layout;
    private long lastShakeTime;
    private static final int SHAKE_THRESHOLD = 800;
    private static final int MIN_TIME_BETWEEN_SHAKES = 1000; // in milliseconds

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize sensor manager and accelerometer
        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        if (sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER) != null) {
            accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        } else {
            Toast.makeText(this, "Accelerometer not available on this device", Toast.LENGTH_SHORT).show();
        }

        // Get reference to the layout
        layout = findViewById(R.id.mainLayout);
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (accelerometer != null) {
            sensorManager.registerListener(this, accelerometer, SensorManager.SENSOR_DELAY_NORMAL);
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        sensorManager.unregisterListener(this);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if (event.sensor.getType() == Sensor.TYPE_ACCELEROMETER) {
            long currentTime = System.currentTimeMillis();
            
            float x = event.values[0];
            float y = event.values[1];
            float z = event.values[2];
            
            // Calculate acceleration
            float acceleration = (float) Math.sqrt(x * x + y * y + z * z) - SensorManager.GRAVITY_EARTH;
            
            if (acceleration > 5) { // Threshold for shake detection
                if (currentTime - lastShakeTime > MIN_TIME_BETWEEN_SHAKES) {
                    lastShakeTime = currentTime;
                    changeBackgroundColor();
                }
            }
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        // Not used in this example
    }

    private void changeBackgroundColor() {
        Random random = new Random();
        int color = Color.rgb(random.nextInt(256), random.nextInt(256), random.nextInt(256));
        layout.setBackgroundColor(color);
    }
} 