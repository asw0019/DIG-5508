// This is exercise 12-1, in which I calculate the median
// https://beginnersbook.com/2018/10/java-program-to-sort-an-array-in-ascending-order for the sort function.
float median(float[] sequence){
  float sum = 0;
  int i;
  float k;
  float l;
  float med;
  for (i = 0; i < sequence.length; i++){
    for (int j = i + 1; j < sequence.length; j++){
      if (sequence[i] > sequence[j]){
        k = sequence[i];
        sequence[i] = sequence[j];
        sequence[j] = k;
      }
    }
  }
  i = (i / 2);
  if (sequence.length % 2 == 0){
  med = (sequence[i] + sequence[i - 1]) / 2;
  }
  else{
  med = sequence[i];
  }
  return med;
}

float[] values = {75,100,5,200};
// 9,10,25,33,35,52,73,76,86
void setup() {
  size(200, 100);
  // rect(30,15,20,10);
  for (int i = 0; i < values.length; i++){
    rect(i * 20,100 - values[i],20,values[i]);
  }
  rect(0, 100 - median(values), 200, 0);
  println(median(values));
}
