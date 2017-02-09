package manolo.botoncito;

import android.content.Context;
import android.content.Intent;
import android.content.res.Resources;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.os.SystemClock;
import android.support.v7.app.AppCompatActivity;
import android.util.DisplayMetrics;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AbsoluteLayout;
import android.widget.Button;
import android.widget.Chronometer;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TableLayout;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.common.api.GoogleApiClient;

import java.util.Random;

public class Menu extends AppCompatActivity {

    Chronometer crono;
    Button boton;
    int x, y, z, aux = 0,Max = 50,a,b,c,d;
    Random rand = new Random();
    RelativeLayout pantalla;
    String aux2,resul;
    double time;
    Boolean M;
    RelativeLayout.LayoutParams params = new RelativeLayout.LayoutParams(
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.MATCH_PARENT);

    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private GoogleApiClient client;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.menu);
        boton = (Button) findViewById(R.id.botoncito);
        pantalla = (RelativeLayout) findViewById(R.id.fondo);
        crono = (Chronometer) findViewById(R.id.chrono);
        //timo = (EditText)findViewById(R.id.tim);
        Max = getIntent().getIntExtra("max", 50);
        M =getIntent().getBooleanExtra("modo", false);

        if (M){
            boton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    if (aux == 0) {
                        aux2 = Integer.toString(aux);
                        x = rand.nextInt(255) ;
                        y = rand.nextInt(255) ;
                        z = rand.nextInt(255);
                        pantalla.setBackgroundColor(Color.rgb(x, y, z));
                        boton.setBackgroundColor(Color.rgb(255 - x, 255 - y, 255 - z));
                        boton.setText(aux2);
                        aux++;
                        crono.setBase(SystemClock.elapsedRealtime());
                        crono.start();

                    }
                    if (aux < Max && aux >= 1) {
                        aux2 = Integer.toString(aux);
                        x = rand.nextInt(255) ;
                        y = rand.nextInt(255) ;
                        z = rand.nextInt(255) ;
                        pantalla.setBackgroundColor(Color.rgb(x, y, z));
                        boton.setBackgroundColor(Color.rgb(255 - x, 255 - y, 255 - z));
                        boton.setText(aux2);
                        aux++;
                        a = rand.nextInt(500);
                        b = rand.nextInt(500);
                        c = rand.nextInt(700);
                        d = rand.nextInt(700);

                        params.setMargins(a, c, b, d);
                        boton.setLayoutParams(params);
                        /*boton.setHeight(70);
                        boton.setWidth(150);*/
                    }
                    if (aux ==  Max) {
                        crono.stop();
                        aux2 = Integer.toString(aux);
                        boton.setText(aux2);
                        //time = crono.getBase() - SystemClock.elapsedRealtime();
                        Intent resultado = new Intent(getApplicationContext(), Resultados.class);
                        startActivity(resultado);
                        time = (SystemClock.elapsedRealtime() - crono.getBase())/1000;
                        resul = Double.toString(time);
                       // timo.setText(resul);
                        Intent R = new Intent(getApplicationContext(),Resultados.class);
                        R.putExtra("resultad",resul);
                        startActivity(R);
                    }
                }
            });
        }else{
            boton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    if (aux == 0) {
                        aux2 = Integer.toString(aux);
                        x = rand.nextInt(255) ;
                        y = rand.nextInt(255) ;
                        z = rand.nextInt(255);
                        pantalla.setBackgroundColor(Color.rgb(x, y, z));
                        boton.setBackgroundColor(Color.rgb(255-x,255- y,255- z));
                        boton.setText(aux2);
                        aux++;
                        crono.setBase(SystemClock.elapsedRealtime());
                        crono.start();
                    }
                    if (aux < Max && aux >= 1) {
                        aux2 = Integer.toString(aux);
                        x = rand.nextInt(255) ;
                        y = rand.nextInt(255) ;
                        z = rand.nextInt(255) ;
                        pantalla.setBackgroundColor(Color.rgb(x, y, z));
                        boton.setBackgroundColor(Color.rgb(255-x,255-y,255-z));
                        boton.setText(aux2);
                        aux++;
                    }
                    if (aux == Max) {
                        crono.stop();
                        aux2 = Integer.toString(aux);
                        boton.setText(aux2);
                        //time = crono.getBase() - SystemClock.elapsedRealtime();
                        Intent resultado = new Intent(getApplicationContext(), Resultados.class);
                        startActivity(resultado);
                        time = (SystemClock.elapsedRealtime() - crono.getBase())/1000;
                        resul = Double.toString(time);
                        //timo.setText(resul);
                        Intent R = new Intent(getApplicationContext(),Resultados.class);
                        R.putExtra("resultad",resul);
                        startActivity(R);
                    }
                }
            });
        }




        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();
    }

    @Override
    public void onStart() {
        super.onStart();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client.connect();
        Action viewAction = Action.newAction(
                Action.TYPE_VIEW, // TODO: choose an action type.
                "Menu Page", // TODO: Define a title for the content shown.
                // TODO: If you have web page content that matches this app activity's content,
                // make sure this auto-generated web page URL is correct.
                // Otherwise, set the URL to null.
                Uri.parse("http://host/path"),
                // TODO: Make sure this auto-generated app deep link URI is correct.
                Uri.parse("android-app://manolo.botoncito/http/host/path")
        );
        AppIndex.AppIndexApi.start(client, viewAction);
    }

    @Override
    public void onStop() {
        super.onStop();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        Action viewAction = Action.newAction(
                Action.TYPE_VIEW, // TODO: choose an action type.
                "Menu Page", // TODO: Define a title for the content shown.
                // TODO: If you have web page content that matches this app activity's content,
                // make sure this auto-generated web page URL is correct.
                // Otherwise, set the URL to null.
                Uri.parse("http://host/path"),
                // TODO: Make sure this auto-generated app deep link URI is correct.
                Uri.parse("android-app://manolo.botoncito/http/host/path")
        );
        AppIndex.AppIndexApi.end(client, viewAction);
        client.disconnect();
    }
}
