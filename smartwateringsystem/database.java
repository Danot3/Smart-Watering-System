package com.example.smartwateringsystem;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class database extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_database);
        TextView r = (TextView) findViewById(R.id.parameter);
        String value = getIntent().getStringExtra(ValveC.PARAM);
        r.setText(value);
    }
}
