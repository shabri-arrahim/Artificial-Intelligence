/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package IFIK4103_1301172742;

import javax.swing.JOptionPane;

/**
 *
 * @author Tiravieri
 */
public class Fuzzy {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        data_input di = new data_input();
        followers follower = new followers();
        engangement engange = new engangement();
        recomendation recomendate = new recomendation();  

        float[] data_index = new float[200];
        float[] data_follower = new float[200];
        float[] data_engange = new float[200];
        di.baca(data_index , data_follower , data_engange);
        float[] index2 = new float[100];
        float[] score2 = new float[100];

        for(int j = 0 ; j < 100 ; j++){
            follower.input_followers(data_follower[j]);
            engange.input_engangement(data_engange[j]);

            float[] Y = new float[4];
            float[] Z = new float[4];

            Y[0] = Math.min(engange.rendah(), follower.sedikit());
            Y[1] = Math.min(engange.tinggi(), follower.sedikit());
            Y[2] = Math.min(engange.rendah(), follower.banyak());
            Y[3] = Math.min(engange.tinggi(), follower.banyak());

            Z[0] = recomendate.rendah(Y[0]);
            Z[1] = recomendate.tinggi(Y[1]);
            Z[2] = recomendate.rendah(Y[2]);
            Z[3] = recomendate.tinggi(Y[3]);

            //hitung score
            float pembilang = 0.0f , penyebut = 0.0f , score = 0.0f;       
            for(int i = 0 ; i < 4 ; i++) {
                pembilang += Y[i] * Z[i];
                penyebut += Y[i];
            }

            score = pembilang / penyebut ;

            index2[j] = j+1;
            score2[j] = score ;
        }
        
        di.tulis(index2, score2);
        JOptionPane.showMessageDialog(null, "check Tebakan.csv", "InfoBox: " + "titleBar", JOptionPane.INFORMATION_MESSAGE);
    }  
}
    

