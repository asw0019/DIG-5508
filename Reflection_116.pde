// This is exercise 12-1, in which I calculate the median.

float mean(float[] sequence){
  float sum = 0;
  int i;
  float k;
  float l;
  for (i = 0; i < sequence.length; i++){
    for (int j = i + 1; j < sequence.length; j++){
      if (sequence[i] > sequence[j]){
        k = sequence[i];
        sequence[i] = sequence[j];
        sequence[j] = k;
      }
    }
  }
  if (sequence.length % 2 == 0){
  i = (i / 2) - 1;
  }
  else{
  i = (i / 2);
  }
  return sequence[i];
}

float[] values = {2,3,1};
// 9,10,25,33,35,52,73,76,86
void setup() {
  size(200, 100);
  // rect(30,15,20,10);
  for (int i = 0; i < values.length; i++){
    rect(i * 20,100 - values[i],20,values[i]);
  }
  rect(0, 100 - mean(values), 200, 0);
  println(mean(values));
}
