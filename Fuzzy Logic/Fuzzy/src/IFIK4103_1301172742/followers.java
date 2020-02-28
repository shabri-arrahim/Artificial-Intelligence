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
public class followers {
    private float followers ;   
    private float titik1 = 40600.0f ;
    private float titik2 = 51850.0f;
     
    public void input_followers(float x) {
        followers = x ;
    }
    
    public float sedikit() {
        if(followers <= titik1){
            return 1 ;
        }else if(followers >= titik2){
            return 0 ;
        }else{
            return (titik2 - followers)/(titik2- titik1);
        }
     }
     
     public float banyak() {
        if(followers <= titik1){
            return 0 ;
        }else if(followers >= titik2){
            return 1 ;
        }else{
            return (followers - titik1)/(titik2 - titik1);
        }
    }
}
