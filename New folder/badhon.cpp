//Simple Security System//
#include<iostream>
#include<string.h>
#include<conio.h>
#include<fstream>
#include<windows.h>
using namespace std;
int main()
{
    int a;
    string line,Old_Pass,Pass,Pass1,Pass2,User1,User2;
    cout<<"***** SECURITY SYSTEM PROGRAM *****";
    do{
    cout<<endl<<endl<<"*************************************"<<endl;
    cout<<"* 1- >         Add New User             *"<<endl;
    cout<<"* 2 - >       Change The Password      *"<<endl;
    cout<<"* 3 - >  Go To Login Panel To See Data *"<<endl;
    cout<<"* 4 - >       Quit The Program         *"<<endl;

    cout<<"*************************************"<<endl<<endl;
    cout<<"Enter Your Choice : ";
    cin>>a;
    switch(a)
    {
         case 1:
        {
            ofstream outf1;
            outf1.open("Password.txt",ios::app);
            if (outf1.is_open())
            {
                cout<<"Enter Your User ID: ";
                cin>>User1;
                cout<<"Enter Your Password : ";
                cin>>User2;
                if(User1==User2)
                {
                    outf1<<User1<<" "<<User2<<"\n";
                    cout<<"New User Add Succesfully";
                }
            }
            outf1.close();
            break;
        }
        case 2:
        {
            ifstream outf2;
            outf2.open("Password.txt");
            cout<<"Enter The Old Password :-";
            cin>>Old_Pass;
            if (outf2.is_open())
            {
            	while(!outf2.eof())
            	{
             		outf2>>line;
            		if(Old_Pass==line)
            		{
                		outf2.close();
                		ofstream outf1;
                		outf1.open("Password.txt");
                		if (outf2.is_open())
             			{
             				cout<<"Enter Your New Password :-";
		                	cin>>Pass1;
             				cout<<"Enter Your Password Again :-";
             				cin>>Pass2;
             				if(Pass1==Pass2)
             				{
                 				outf1<<Pass1;
                 				cout<<"Password Change Succesfully";
             				}
             			}
            		}
            		else
            		{
              			cout<<"Please Enter Valid Password";
            		}
            	}
            }
           break;
        }
    case 3:
        {
            ifstream outf3;
            outf3.open("Password.txt");
            cout<<"Please Enter Your Password : ";
            cin>>User1;
            cout<<"Please Enter Password Again : ";
            cin>>Pass;
            int temp=0;
            if (outf3.is_open())
            {
            	while(!outf3.eof())
            	{
             		outf3>>User2;
             		outf3>>line;

           		if(Pass==line && User1==User2 )
           		{
               			cout<<"Acess Granted";
               			temp=1;
           		}
            	}
       	     }

       	     if(temp==0)
           		{
               			cout<<"Password Is Wrong"<<endl;
           		}
    	break;
       }
    case 4:
        {
            break;
        }

    	default:
        	cout<<"Enter Valid Choice";
    }
    }
    while(a != 5);
    return 0;
}