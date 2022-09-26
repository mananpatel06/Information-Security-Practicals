#include<math.h>
#include<iostream>
using namespace std;
int main()
{
int p,g,x,y;
cout<<"Enter value of p , g : ";
cin >>p>>g;
cout<<"Enter private key a for Lucious Fox : ";
cin>>x;
cout<<"Enter private key a for Bruce wayne : ";
cin>>y;

int a = pow(g,x);a=a%p;
int b = pow(g,y);b=b%p;

int ska =pow(b,x);
ska = ska%p;
int skb =pow(a,y);
skb = skb%p;

cout<<"\nSecret key for Lucious Fox is "<<ska<<"\nSecret key for Bruce wayne is "<<skb<<endl;
        cout<<endl<<"Made by: Manan Patel "<<endl;

return 0;
}
