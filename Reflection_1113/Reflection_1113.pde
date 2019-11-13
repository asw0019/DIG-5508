// This is exercise 12-1, in which I calculate the median
// https://www.tutorialspoint.com/Java-program-to-calculate-mode-in-Java for finding the mode.
float mode(float[] sequence){
  float[] modes = {};
  float maxValue = 0;
  float maxCount = 0;
  int i;
  int j;
  for (i = 0; i < sequence.length; ++i){
    int count = 0;
    for (j = 0; j < sequence.length; ++j){
      if (sequence[j] == sequence[i]){
        ++count;
      }
    }
    if (count > maxCount) {
      maxCount = count;
      maxValue = sequence[i];
  //    modes.append(sequence[i]);
    }
  }
  // return modes (If I have time, find this. It's giving me conversion issues.)
  return maxValue;
}

float[] values = {75,75,100,5,200,200};
// 9,10,25,33,35,52,73,76,86
void setup() {
  size(200, 100);
  // rect(30,15,20,10);
  for (int i = 0; i < values.length; i++){
    rect(i * 20,100 - values[i],20,values[i]);
  }
  rect(0, 100.0 - mode(values), 200, 0);
  println(mode(values));
}
