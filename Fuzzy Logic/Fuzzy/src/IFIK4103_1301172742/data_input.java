/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package IFIK4103_1301172742;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 *
 * @author Tiravieri
 */
public class data_input {
    public void baca(float[] index , float[] pendapatan , float[] hutang) {
        String nama_file = "influencers.csv";
        File file = new File(nama_file);
        Scanner input_stream ;    
        try {
            input_stream = new Scanner(file);
            input_stream.useDelimiter("[,\n]");

            int i = 0 ;
            int j = 0 ;
            while(input_stream.hasNext()) {
                if(i > 2){
                    index[j] = Float.parseFloat(input_stream.next());
                    pendapatan[j] = Float.parseFloat(input_stream.next());
                    hutang[j] = Float.parseFloat(input_stream.next());
                    j++;
                } else {     
                    input_stream.next();
                }
            i++;
            }
        } catch (Exception e) {
            System.out.println("Gagal Membaca File");
        }
    }
    
    
    public void tulis(float[] index , float[] score) {
        try {
            FileWriter fw = new FileWriter("Tebakan.csv" , true);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter pw = new PrintWriter(bw);
            pw.print("20 Influencer Terbaik : \n");
            pw.print("Index" + "," + "Score\n");
            
            System.out.println("20 Influencer Terbaik : ");
            for(int i = 0 ; i < 20 ; i++) { 
                float score_tertinggi = 0.0f ;
                for(int j = i ; j < 100 ; j++) {
                    if(score_tertinggi < score[j]) {
                        score_tertinggi = score[j];
                        float tempt = score[i];
                        score[i] = score[j];
                        score[j] = tempt ;
                        float tempt_index = index[i] ;
                        index[i] = index[j];
                        index[j] = tempt_index ;
                    }
                }
                pw.print(Math.round(index[i]) + "," + score[i] + "\n" );
                System.out.println("Index ke-"+(int)index[i] + " Score : " +score[i]); 
            }
            pw.flush();
            pw.close();
        } catch(Exception e) {
            System.out.println("Gagal Menyimpan File");
        }
    }
    
}
