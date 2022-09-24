#include <iostream>
#include <fstream>
#include <random>
#include <string>
using namespace std;

int shuffleArray(string array[], int arraySize);

int getWordsLetterIndex(string word, int letterIndex);

int sort(string array[], int arraySize, int letterIndex, int first);

int main() {
  ifstream words_file;
  int wordsCount = 100000;

  words_file.open("random.txt");
  string words[wordsCount];

  for (int i = 0; i < wordsCount; i++) {
    getline(words_file, words[i]);
  }

  words_file.close();

  shuffleArray(words, wordsCount);

  cout << "Enter the number of words: ";
  cin >> wordsCount;
  cout << endl;

  sort(words, wordsCount, 0, 0);
  for(int i = 0; i < wordsCount; i++) cout << words[i] << endl;

  cout << "Done" << endl;
  return 0;
}

int shuffleArray(string array[], int arraySize) {
  for(int i = 0; i < arraySize; i++) {
    double u = rand() * 1.0 / RAND_MAX;
    int j = u * arraySize;
    if(j == arraySize) j--;
    string temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }

  return 0;
}

int getWordsLetterIndex(string word, int letterIndex) {
  if(letterIndex >= word.length()) return 0;
  char letter = word[letterIndex];
  if(letter == 'a' || letter == 'A') return 1;
  if(letter == 'b' || letter == 'B') return 2;
  if(letter == 'c' || letter == 'C') return 3;
  if(letter == 'd' || letter == 'D') return 4;
  if(letter == 'e' || letter == 'E') return 5;
  if(letter == 'f' || letter == 'F') return 6;
  if(letter == 'g' || letter == 'G') return 7;
  if(letter == 'h' || letter == 'H') return 8;
  if(letter == 'i' || letter == 'I') return 9;
  if(letter == 'j' || letter == 'J') return 10;
  if(letter == 'k' || letter == 'K') return 11;
  if(letter == 'l' || letter == 'L') return 12;
  if(letter == 'm' || letter == 'M') return 13;
  if(letter == 'n' || letter == 'N') return 14;
  if(letter == 'o' || letter == 'O') return 15;
  if(letter == 'p' || letter == 'P') return 16;
  if(letter == 'q' || letter == 'Q') return 17;
  if(letter == 'r' || letter == 'R') return 18;
  if(letter == 's' || letter == 'S') return 19;
  if(letter == 't' || letter == 'T') return 20;
  if(letter == 'u' || letter == 'U') return 21;
  if(letter == 'v' || letter == 'V') return 22;
  if(letter == 'w' || letter == 'W') return 23;
  if(letter == 'x' || letter == 'X') return 24;
  if(letter == 'y' || letter == 'Y') return 25;
  if(letter == 'z' || letter == 'Z') return 26;
  return 0;
}

int sort(string array[], int arraySize, int letterIndex, int first) {
  int letterCounts[27];
  for(int i = 0; i < 27; i++) letterCounts[i] = 0;

  for(int i = first; i < first + arraySize; i++) letterCounts[getWordsLetterIndex(array[i], letterIndex)]++;
  for(int i = 0; i < 27; i++) cout << letterCounts[i] << endl;

  for(int i = 1; i < 27; i++) letterCounts[i] += letterCounts[i-1];
  for(int i = 0; i < 27; i++) cout << letterCounts[i] << endl;

  int lettersIterate[27];
  for(int i = 0; i < 27; i++) lettersIterate[i] = letterCounts[i];

  string words[arraySize];
  for(int i=0; i < arraySize; i++) {
    int index = lettersIterate[getWordsLetterIndex(array[i+first], letterIndex)] - 1;
    words[index] = array[i+first];
    lettersIterate[getWordsLetterIndex(array[i+first], letterIndex)]--;
  }

  for(int i = 0; i < arraySize; i++) array[i + first] = words[i];

  for(int i = 0; i < 26; i++) {
    if(letterCounts[i] < letterCounts[i + 1] - 1) sort(array, letterCounts[i + 1] - letterCounts[i] - 1, letterIndex + 1, letterCounts[i]);
  }

  return 0;
}