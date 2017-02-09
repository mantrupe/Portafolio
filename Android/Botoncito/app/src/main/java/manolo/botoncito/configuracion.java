package manolo.botoncito;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.RadioGroup;
import android.widget.Switch;
import android.widget.TextView;

public class configuracion extends AppCompatActivity {

    RadioGroup cont;
    int clicks;
    Switch hardcore;
    TextView modillo;
    Button Lback,ST;
    boolean M = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_configuracion);

        /*-----------------Asignaciom-------------------*/
        cont = (RadioGroup)findViewById(R.id.gr);
        hardcore = (Switch)findViewById(R.id.modo);
        modillo = (TextView)findViewById(R.id.Txmodo);
        Lback = (Button)findViewById(R.id.back);
        ST = (Button)findViewById(R.id.pl);

        /*----------Funciones------------------*/
        cont.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                switch (checkedId){
                    case R.id.cs25:
                        clicks = 25;
                        break;
                    case R.id.cs50:
                        clicks = 50;
                        break;
                    case R.id.cs75:
                        clicks = 75;
                        break;
                    case R.id.cs100:
                        clicks = 100;
                        break;
                }
            }
        });

        hardcore.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    modillo.setText("MAME");
                    M = true;
                } else {
                    modillo.setText("Normal");
                    M = false;
                }
            }
        });

        Lback.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent regre = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(regre);
            }
        });
        ST.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent P = new Intent(getApplicationContext(), Menu.class);
                P.putExtra("max", clicks);
                P.putExtra("modo",M);
                startActivity(P);
            }
        });


    }

}
