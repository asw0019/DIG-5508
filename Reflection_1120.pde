// This is exercise 12-3, in which I calculate the standard deviation.
// I used https://stackoverflow.com/questions/40117353/standard-deviation-calculator-java for my standard deviation.
float standardDev(float[] sequence){
  float sum = 0;
  float newSum = 0; 
  float [] newArray = new float [20]; 
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
float[] values = {9,25,52,10,33,76,35,86,73,10};
// 9,10,25,33,35,52,73,76,86
void setup() {
  size(200, 100);
  // rect(30,15,20,10);
  for (int i = 0; i < values.length; i++){
    rect(i * 20,100 - values[i],20,values[i]);
  }
  rect(0, 100 - standardDev(values), 200, 0);
  println(standardDev(values));
}
