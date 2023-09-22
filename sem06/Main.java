public class Main {
    public static void main(String[] args) {
    int [] arr1 = {5,6,7,8,9,10};
    int [] arr2 = {50,6,7,8,9,10};
    try {
    System.out.println(MSE(arr1, arr2));
    }catch (RuntimeException e){
    System.out.println(e.getMessage());
    }
    }
    
    public static double MSE(int [] arr1, int [] arr2){
    double sum = 0;
    if (arr1.length != arr2.length) 
    throw new RuntimeException("Массивы не равны");

    for (int i = 0; i < arr1.length; i++) {
    sum += Math.pow((arr2[i]-arr1[i]), 2.0);
    }
    
    return sum / arr1.length;
    }
    }