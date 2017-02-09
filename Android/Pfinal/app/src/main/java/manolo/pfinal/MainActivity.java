package manolo.pfinal;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Spinner;

public class MainActivity extends AppCompatActivity {

    Spinner Opcion;
    ListView lista;
    Boolean tipo;
    int aux;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Opcion = (Spinner)findViewById(R.id.spin);
        lista = (ListView)findViewById(R.id.ejer);

        ArrayAdapter values = new ArrayAdapter(getApplicationContext(),android.R.layout.simple_list_item_1,getResources().getStringArray(R
        .array.intensidad));



        Opcion.setAdapter(values);
        Opcion.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {

                switch (position) {
                    case 0:
                        ArrayAdapter cheche = new ArrayAdapter(getApplicationContext(), android.R.layout.simple_list_item_1, getResources().getStringArray(
                                R.array.Baja));
                        lista.setAdapter(cheche);
                        tipo = false;
                        break;
                    case 1:
                        ArrayAdapter chido = new ArrayAdapter(getApplicationContext(), android.R.layout.simple_list_item_1, getResources().getStringArray(
                                R.array.Alta));
                        lista.setAdapter(chido);
                        tipo = true;
                        break;
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        lista.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                if (position == 0){
                    aux=1;
                    }else{
                    aux=2;
                }
                Intent Adios = new Intent(getApplicationContext(),Ejercicio.class);
                Adios.putExtra("pos",aux);
                Adios.putExtra("kind",tipo);
                startActivity(Adios);
            }
        });

    }
}
