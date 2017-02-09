package manolo.botoncito;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.Chronometer;
import android.widget.TextView;

public class Resultados extends AppCompatActivity {
    Button volver,menu;
    Chronometer resu;
    String resultado;
    TextView cuadro;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_resultados);

        volver = (Button)findViewById(R.id.PA);
        menu =(Button)findViewById(R.id.menuR);
        //resu = (Chronometer)findViewById(R.id.chroR);
        resultado = getIntent().getStringExtra("resultad");
        cuadro = (TextView)findViewById(R.id.R);


        cuadro.setText(resultado);
        volver.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent Play = new Intent(getApplicationContext(),Menu.class);
                startActivity(Play);

            }
        });

        menu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent Menu = new Intent(getApplicationContext(),MainActivity.class);
                startActivity(Menu);
            }
        });
    }
}
