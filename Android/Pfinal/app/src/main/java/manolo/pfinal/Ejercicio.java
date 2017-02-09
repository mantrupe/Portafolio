package manolo.pfinal;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class Ejercicio extends AppCompatActivity {
   int posi;
   ImageView work;
   TextView  titulo;
    Button web;
    Boolean cual;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ejercicio);

        work = (ImageView)findViewById(R.id.img);
        titulo = (TextView)findViewById(R.id.nombre);
        web = (Button)findViewById(R.id.button);
        cual = getIntent().getBooleanExtra("kind", true);
        posi = getIntent().getIntExtra("pos",0);

        if(cual){
            if (posi == 0){
                work.setImageResource(R.drawable.thor);
                titulo.setText("THOR");
            }else{
                work.setImageResource(R.drawable.hulk);
                titulo.setText("HULK");
            }
        }else{
            if (posi == 0){
               work.setImageResource(R.drawable.yoga);
                titulo.setText("YOGA");
            }else{
                work.setImageResource(R.drawable.ironman);
                titulo.setText("IRONMAN");
            }
        }

        web.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(Intent.ACTION_VIEW, Uri.parse("www.darebee.com"));
                startActivity(i);
            }
        });
    }
}
