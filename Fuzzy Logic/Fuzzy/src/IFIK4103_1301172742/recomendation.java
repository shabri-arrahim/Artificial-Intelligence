/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package IFIK4103_1301172742;

/**
 *
 * @author Tiravieri
 */
public class recomendation {
    float titik1 = 0.0f;
    float titik2 = 100.0f;
    
    public float tinggi(float x) {
        return titik1 + (x*(titik2-titik1));
    }
    
    public float rendah(float x) {
        return titik2 - (x*(titik2 - titik1));
    }
}
