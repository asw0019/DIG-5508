
float mean(float[] sequence){
  float sum = 0;
  for (int i = 0; i < sequence.length; i++){
    sum = sum + sequence[i];
  }
  sum = sum / sequence.length;
  return sum;
}
// https://beginnersbook.com/2018/10/java-program-to-sort-an-array-in-ascending-order for the sort function.
float median(float[] sequence){
  float sum = 0;
  int i;
  float k;
  float l;
  float med;
  for (i = 0; i < sequence.length; i++){
    // The array is sorted. At each number, the sort sees if the remaining numbers are greater.
    for (int j = i + 1; j < sequence.length; j++){
      if (sequence[i] > sequence[j]){
        k = sequence[i];
        sequence[i] = sequence[j];
        sequence[j] = k;
      }
    }
  }
  // Checks for odd or even sized array
  i = (i / 2);
  if (sequence.length % 2 == 0){
  med = (sequence[i] + sequence[i - 1]) / 2;
  }
  else{
  med = sequence[i];
  }
  return med;
}
// I used https://stackoverflow.com/questions/40117353/standard-deviation-calculator-java for my standard deviation.
float standardDev(float[] sequence){
  float sum = 0;
  float newSum = 0; 
  float [] newArray = new float [500]; 
  // first, calculate mean
  for (int i = 0; i<sequence.length; i++){
    // add the numbers in a sequence
    sum = sum + sequence[i];
  }
  // divides the total by the length
  float mean = (sum) / (sequence.length); 
  // next, 
  for (int j = 0; j<sequence.length; j++){
    // finds the distance from each number in sequence from mean, squares it, and adds it together
    newArray[j] = ((sequence[j] - mean) * (sequence[j] - mean)); 
    newSum = newSum + newArray[j]; 
  }
  // next, it divides the sum of the squared distances from each number in sequence, by the sequence length.
  float squaredDiffMean = (newSum) / (sequence.length); 
  // finally, it takes the square root...
  float standardDev = (sqrt(squaredDiffMean)); 
  // ...and finally, returns it!
  return standardDev; 
}

float[] values = {75,100,5,200};
// 9,10,25,33,35,52,73,76,86
void setup(){
  size(200, 100);
  // Strings loading methods from https://processing.org/reference/loadStrings_.html
  String[] highs = loadStrings("219-0.txt");
  String[] lows = loadStrings("1342-0.txt");
  int size = highs.length;
  int size2 = lows.length;
  float [] arr = new float [size];
  float [] arr2 = new float[size2];
  for (int i = 0; i < highs.length; i++){
    // from https://www.geeksforgeeks.org/float-parsefloat-method-in-java-with-examples/
    arr[i] = Float.parseFloat(highs[i]);
    rect(i * 10,100 - Float.parseFloat(highs[i]),10,Float.parseFloat(highs[i]));
  }
  for (int j = 0; j < lows.length; j++){
    arr2[j] = Float.parseFloat(lows[j]);
    rect(j * 10,100 - Float.parseFloat(highs[j]),10,Float.parseFloat(highs[j]));
  }
  println("The average high temperature from this period in this location was: " + mean(arr) + " degrees Fahrenheit.");
  println("The average low temperature from this period in this location was: " + mean(arr2) + " degrees Fahrenheit.");
  println("");
  println("The median high temperature from this period in this location was: " + median(arr) + " degrees Fahrenheit.");
  println("The median low temperature from this period in this location was: " + median(arr2) + " degrees Fahrenheit.");
  println("");
  println("The standard deviation high temperature from this period in this location was: " + standardDev(arr) + " degrees Fahrenheit.");
  println("The standard deviation low temperature from this period in this location was: " + standardDev(arr2) + " degrees Fahrenheit.");
}
