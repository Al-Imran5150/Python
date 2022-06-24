#include<fstream>
#include<iostream>

using namespace std;
int main()
{
FILE *file;
char op;
  double first, second;
  ofstream output("test.txt",ios::app);
  ifstream input("test.txt");
  printf("Enter an operator (+, -, *, /): ");
  scanf("%c", &op);
  printf("Enter two operands: ");
  scanf("%lf %lf", &first, &second);
  output<<first<<" "<<second;
  
//file=fopen("test.txt","w");
 switch (op) {
     double result;
    case '+':
      result=first + second;
      output<<" "<<result<<endl;
      printf("%.1lf + %.1lf = %.1lf", first, second,result) ;
      break;
    case '-':
      result=first - second;
      output<<" "<<result<<endl;
      printf("%.1lf - %.1lf = %.1lf", first, second,result) ;
      break;
    case '*':
      result=first * second;
      output<<" "<<result<<endl;
      printf("%.1lf * %.1lf = %.1lf", first, second,result) ;
      break;
    case '/':
      result=first / second;
      output<<" "<<result<<endl;
      printf("%.1lf / %.1lf = %.1lf", first, second,result) ;
      break;
    // operator doesn't match any case constant
    default:
      printf("Error! operator is not correct");

  }
  output.close();
if(file==NULL){
    //printf("file doesnot exist");


}