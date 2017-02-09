package manolo.drawable;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.RadioGroup;

public class MainActivity extends AppCompatActivity {
    RadioButton op1,op2,op3;
    RadioGroup  caja;
    ImageView imagen;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

         /*op1 = (RadioButton)findViewById(R.id.radioButton);
         op2 = (RadioButton)findViewById(R.id.radioButton2);
        op3 = (RadioButton)findViewById(R.id.radioButton3);*/
        caja = (RadioGroup)findViewById(R.id.group);
         imagen = (ImageView)findViewById(R.id.imgcont);

        caja.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                switch (checkedId){
                    case R.id.radioButton:
                        imagen.setImageResource(R.drawable.img);
                        break;
                    case R.id.radioButton2:
                        imagen.setImageResource(R.drawable.lily);
                        break;
                    case R.id.radioButton3:
                        imagen.setImageResource(R.drawable.nigga);
                }

            }
        });

    }
}
