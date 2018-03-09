#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Kredyt{
  double kwota_c;
  double procent_r;
};
struct Czlowiek{
  double pensja;
  Kredyt* ptr;
};

double splac_rate(Czlowiek& c){
  if(c.ptr->kwota_c>c.pensja/2){
    double rata=c.ptr->kwota_c-c.pensja/2;

    return rata;
  }
  else{
    c.ptr->kwota_c=0;
    return c.ptr->kwota_c;
  }
}

int main(){
  srand(time(NULL));
  Kredyt kredyt;
  Czlowiek czlowiekA, czlowiekB;
  czlowiekA.ptr=&kredyt;

  cout<<"Wprowadz kwote kredytu:"<<endl;
  cin>>kredyt.kwota_c;
  cout<<"Wprowadz oprocentowanie w skali roku:"<<endl;
  cin>>kredyt.procent_r;
  cout<<"Twoja kwota to: "<<kredyt.kwota_c<<" i % w skali roku to : ";
  cout<<kredyt.procent_r<<endl;

  czlowiekA.pensja=rand()%2000+2000;
  czlowiekB.pensja=rand()%2000+2000;

  cout<<splac_rate(czlowiekA)<<endl;

return 0;
}
