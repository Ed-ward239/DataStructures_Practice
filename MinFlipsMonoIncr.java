public int minFlipsMonoIncr(String s) {
  int n = s.length();
  int f0, f1;
  // init
  if (s.charAt(0) == '0') f0 = 0; f1 = 1;
  else                    f0 = 1; f1 = 0;
  // dp
  for (int i = 1; i < n; ++i) {
    if (s.charAt(i) == '0') {
      // int minTemp = Math.min(f0, f1);
      f0 = f0;
      f1 = Math.min(f0, f1) + 1; // actually do not need minTemp
    } else { // == '1'
      int minTemp = Math.min(f0, f1);
      f0 = f0 + 1;
      f1 = minTemp; // or calculate the f1 first then get rid of minTemp
    }
  }
  return Math.min(f0, f1);
}