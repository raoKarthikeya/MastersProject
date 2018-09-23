package com.example.sjsu.masterproject;

import android.graphics.Bitmap;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;
import android.app.Fragment;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.encoder.QRCode;
import com.journeyapps.barcodescanner.BarcodeEncoder;
//import net.glxn.qrgen.android.QRCode;
//import net.glxn.qrgen.core.scheme.VCard;
import org.jetbrains.annotations.Nullable;

public class QrGeneratorActivity extends AppCompatActivity{
    private Button gen_btn;
    private EditText qr_input;
    private ImageView imageView;
    View qrGenView;
    @Nullable
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstaceState){
        qrGenView = inflater.inflate(R.layout.qr_generator,container,false);
        return qrGenView;
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.qr_generator);
        gen_btn = (Button) findViewById(R.id.gen_btn);
        qr_input = findViewById(R.id.qr_gen);
        gen_btn = findViewById(R.id.gen_btn);
        imageView = findViewById(R.id.imageView);
        gen_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View qrGenView) {
                String text = qr_input.getText().toString().trim();
                if (text != null) {

                    try {
                        MultiFormatWriter multiFormatWriter = new MultiFormatWriter();
                        BitMatrix bitMatrix = multiFormatWriter.encode(text, BarcodeFormat.QR_CODE, 500, 500);
                        BarcodeEncoder barcodeEncoder = new BarcodeEncoder();
                        Bitmap bitmap = barcodeEncoder.createBitmap(bitMatrix);
                        imageView.setImageBitmap(bitmap);
                    } catch (WriterException e) {
                        e.printStackTrace();
                    }
                }
                /*
                else{
                    try{
                        VCard abhay=new VCard("Abhay")
                                .setEmail("anand.abhay1910@gmail.com")
                                .setAddress("India")
                                .setTitle("Tutorial")
                                .setCompany("studytutorial")
                                .setPhoneNumber("258999")
                                .setWebsite("www.studytutorial.in");
                        Bitmap bitmap= QRCode.from(abhay).bitmap();
                        imageView.setImageBitmap(bitmap);
                    }catch (WriterException e){

                    }
                }*/
            }
        });
    }
}