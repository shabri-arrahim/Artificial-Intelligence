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
public class engangement {
    private float engangement ;
    private float titik1 = 4.0f;
    private float titik2 = 5.0f;
    
    public void input_engangement(float x) {
        engangement = x ;
    }
    
    public float rendah() {
        if(engangement <= titik1){
            return 1 ;
        }else if(engangement > titik1 && engangement < titik2){
            return (titik2 - engangement)/(titik2 - titik1) ;
        }else{
            return 0 ;
        }
    }
    
    public float tinggi() {
        if(engangement <= titik1 ) {
            return 0 ;
        }else if(engangement >= titik2) {
            return 1;
        }else{
            return (engangement - titik1)/(titik2 - titik1) ;
        }
    }
}
